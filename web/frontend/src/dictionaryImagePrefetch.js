import { apiAssetUrl } from './api'

const loaded = new Set()
/** @type {Map<string, Promise<boolean>>} */
const inflight = new Map()

const MAX_CONCURRENT = 8
const PRIORITY = { high: 30, auto: 15, low: 5 }

let activeLoads = 0
/** @type {Array<{ url: string, priority: number, resolve: (ok: boolean) => void, reject?: () => void }>} */
const waitQueue = []

export function resolveDictImageUrl(src) {
  return apiAssetUrl(src)
}

export function isDictionaryImageCached(src) {
  const url = resolveDictImageUrl(src)
  return Boolean(url && loaded.has(url))
}

export function markDictionaryImageLoaded(srcOrUrl) {
  const raw = String(srcOrUrl || '')
  const url = raw.startsWith('http') || raw.startsWith('/') ? apiAssetUrl(raw) || raw : resolveDictImageUrl(srcOrUrl)
  if (url) loaded.add(url)
}

function priorityScore(priority) {
  return PRIORITY[priority] ?? PRIORITY.auto
}

function runLoad(job) {
  activeLoads += 1
  return new Promise((resolve) => {
    const img = new Image()
    img.decoding = 'async'
    if (job.priority >= PRIORITY.high && 'fetchPriority' in img) {
      img.fetchPriority = 'high'
    } else if (job.priority <= PRIORITY.low && 'fetchPriority' in img) {
      img.fetchPriority = 'low'
    }
    const done = (ok) => {
      activeLoads = Math.max(0, activeLoads - 1)
      if (ok) loaded.add(job.url)
      inflight.delete(job.url)
      resolve(ok)
      pumpQueue()
    }
    img.onload = () => done(true)
    img.onerror = () => done(false)
    img.src = job.url
  })
}

function pumpQueue() {
  while (activeLoads < MAX_CONCURRENT && waitQueue.length) {
    waitQueue.sort((a, b) => b.priority - a.priority)
    const job = waitQueue.shift()
    if (!job) break
    if (loaded.has(job.url)) {
      job.resolve(true)
      continue
    }
    if (inflight.has(job.url)) {
      inflight.get(job.url).then(job.resolve)
      continue
    }
    const p = runLoad(job)
    inflight.set(job.url, p)
    p.then(job.resolve)
  }
}

function enqueueLoad(url, priority) {
  if (!url) return Promise.resolve(false)
  if (loaded.has(url)) return Promise.resolve(true)

  const pending = inflight.get(url)
  if (pending) {
    const queued = waitQueue.find((j) => j.url === url)
    if (queued) queued.priority = Math.max(queued.priority, priority)
    return pending
  }

  const queued = waitQueue.find((j) => j.url === url)
  if (queued) {
    queued.priority = Math.max(queued.priority, priority)
    return new Promise((resolve) => {
      const prev = queued.resolve
      queued.resolve = (ok) => {
        prev(ok)
        resolve(ok)
      }
    })
  }

  return new Promise((resolve) => {
    waitQueue.push({ url, priority, resolve })
    pumpQueue()
  })
}

export function prefetchDictionaryImage(src, { priority = 'auto' } = {}) {
  const url = resolveDictImageUrl(src)
  return enqueueLoad(url, priorityScore(priority))
}

export async function prefetchDictionaryImages(sources, { urgentCount = 12, concurrency = 6 } = {}) {
  const seen = new Set()
  const ordered = []
  for (const src of sources || []) {
    const url = resolveDictImageUrl(src)
    if (!url || seen.has(url)) continue
    seen.add(url)
    ordered.push(src)
  }
  if (!ordered.length) return

  const urgent = ordered.slice(0, urgentCount)
  const rest = ordered.slice(urgentCount)

  await Promise.all(urgent.map((src) => prefetchDictionaryImage(src, { priority: 'high' })))

  for (let i = 0; i < rest.length; i += concurrency) {
    const batch = rest.slice(i, i + concurrency)
    // eslint-disable-next-line no-await-in-loop
    await Promise.all(batch.map((src) => prefetchDictionaryImage(src, { priority: 'low' })))
  }
}

const PRELOAD_LINK_ID = 'yuwe-dict-img-preload-root'

export function preloadDictionaryImageLinks(sources, count = 6) {
  const urls = []
  const seen = new Set()
  for (const src of sources || []) {
    const url = resolveDictImageUrl(src)
    if (!url || seen.has(url)) continue
    seen.add(url)
    urls.push(url)
    if (urls.length >= count) break
  }
  if (!urls.length) return () => {}

  let root = document.getElementById(PRELOAD_LINK_ID)
  if (!root) {
    root = document.createElement('div')
    root.id = PRELOAD_LINK_ID
    root.hidden = true
    document.head.appendChild(root)
  }
  root.replaceChildren()
  for (const href of urls) {
    const link = document.createElement('link')
    link.rel = 'preload'
    link.as = 'image'
    link.href = href
    root.appendChild(link)
  }

  return () => {
    root?.replaceChildren()
  }
}

export function preloadDictionaryImageLink(src) {
  return preloadDictionaryImageLinks(src ? [src] : [], 1)
}

export function bumpDictionaryImagePriority(src) {
  const url = resolveDictImageUrl(src)
  if (!url || loaded.has(url)) return
  const queued = waitQueue.find((j) => j.url === url)
  if (queued) {
    queued.priority = Math.max(queued.priority, PRIORITY.high)
    waitQueue.sort((a, b) => b.priority - a.priority)
    return
  }
  void prefetchDictionaryImage(src, { priority: 'high' })
}
