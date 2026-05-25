const categorySelect = document.getElementById("categorySelect");
const lessonBtn = document.getElementById("lessonBtn");
const lessonEl = document.getElementById("lesson");
const statusEl = document.getElementById("status");
const imageCache = new Map();

function emptyLocalImage() {
  const svg =
    "<svg xmlns='http://www.w3.org/2000/svg' width='640' height='420' viewBox='0 0 640 420'>" +
    "<rect width='100%' height='100%' fill='%23f4efe6'/>" +
    "<text x='50%' y='50%' dominant-baseline='middle' text-anchor='middle' fill='%238a7a68' font-size='22' font-family='system-ui'>Sin imagen</text>" +
    "</svg>";
  return {
    ok: false,
    image_url: `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`,
    source_url: "#",
    license: "sin imagen",
  };
}

async function getFreeImage(word, category, termId = "") {
  const baseWord = (word || "").toLowerCase().trim();
  const cat = (category || "").toLowerCase().trim();
  const tid = (termId || "").trim();
  const key = `${baseWord}|${cat}|${tid}`;
  if (!key.replace(/\|/g, "")) return emptyLocalImage();
  if (imageCache.has(key)) return imageCache.get(key);
  try {
    const idq = tid ? `&id=${encodeURIComponent(tid)}` : "";
    const data = await fetch(
      `/api/image?q=${encodeURIComponent(baseWord)}&category=${encodeURIComponent(cat)}${idq}`,
    ).then((r) => r.json());
    const result =
      data.ok && data.image_url ? data : emptyLocalImage();
    imageCache.set(key, result);
    return result;
  } catch (_) {
    const result = emptyLocalImage();
    imageCache.set(key, result);
    return result;
  }
}

async function renderLesson(data) {
  lessonEl.innerHTML = "";
  if (!data.terms?.length) {
    lessonEl.innerHTML = "<div class='term'>No hay términos para esta categoría.</div>";
    return;
  }

  const termsWithImages = await Promise.all(
    data.terms.map(async (t) => {
      const img = await getFreeImage(t.espanol, data.category, t.id || "");
      return { ...t, img };
    })
  );

  termsWithImages.forEach((t) => {
    const div = document.createElement("div");
    div.className = "term";
    div.innerHTML = `
      <div class="term-image-wrap">
        <img class="term-image" src="${t.img.image_url}" alt="Imagen de ${t.espanol}" loading="lazy" />
      </div>
      <div class="nasa">${t.nasa_yuwe}</div>
      <div class="esp">${t.espanol}</div>
      <small>Fuente término: ${t.fuente_nombre}</small>
      <small>Imagen: <a href="${t.img.source_url}" target="_blank" rel="noopener noreferrer">${t.img.license}</a></small>
    `;
    const imageEl = div.querySelector(".term-image");
    imageEl?.addEventListener("error", () => {
      imageEl.src = emptyLocalImage().image_url;
    });
    lessonEl.appendChild(div);
  });
}

async function loadCategories() {
  const stats = await fetch("/api/stats").then((r) => r.json());
  const cats = Object.keys((stats || {}).category_distribution || {});
  const defaults = ["numeros", "colores", "animales", "saludos", "vocabulario_general", "alimentos"];
  const finalCats = cats.length ? cats : defaults;
  categorySelect.innerHTML = "";
  finalCats.forEach((c) => {
    const opt = document.createElement("option");
    opt.value = c;
    opt.textContent = c;
    categorySelect.appendChild(opt);
  });
}

async function loadLesson() {
  const category = categorySelect.value;
  lessonEl.innerHTML = "<div class='term'>Cargando vocabulario...</div>";
  try {
    const data = await fetch(`/api/dictionary?category=${encodeURIComponent(category)}&limit=24`).then((r) => r.json());
    await renderLesson(data);
    statusEl.textContent = `Categoría: ${category} | Términos: ${data.terms?.length || 0}`;
  } catch (err) {
    lessonEl.innerHTML = `<div class='term'>Error: ${err.message}</div>`;
  }
}

lessonBtn.addEventListener("click", loadLesson);
loadCategories().then(loadLesson);
