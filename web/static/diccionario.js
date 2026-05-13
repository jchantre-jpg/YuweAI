const categorySelect = document.getElementById("categorySelect");
const lessonBtn = document.getElementById("lessonBtn");
const lessonEl = document.getElementById("lesson");
const statusEl = document.getElementById("status");
const imageCache = new Map();
const COLOR_MAP = {
  rojo: "#c62828",
  azul: "#1565c0",
  verde: "#2e7d32",
  amarillo: "#f9a825",
  negro: "#212121",
  blanco: "#fafafa",
  naranja: "#ef6c00",
  morado: "#6a1b9a",
  rosado: "#e91e63",
  cafe: "#6d4c41",
  marron: "#6d4c41",
  gris: "#757575",
};

function fallbackImage(text = "") {
  const safe = (text || "Nasa Yuwe").replace(/</g, "").replace(/>/g, "");
  return `https://placehold.co/640x420/EDDFC8/6B3E1F?text=${encodeURIComponent(safe)}`;
}

function buildColorSwatchImage(word) {
  const tone = COLOR_MAP[(word || "").toLowerCase().trim()];
  if (!tone) return null;
  const hex = tone.replace("#", "");
  return {
    ok: true,
    image_url: `https://singlecolorimage.com/get/${hex}/640x420`,
    source_url: "#",
    license: "muestra de color",
  };
}

async function getFreeImage(word, category) {
  const baseWord = (word || "").toLowerCase().trim();
  const cat = (category || "").toLowerCase().trim();
  const key = `${baseWord}|${cat}`;
  if (!key) return { image_url: fallbackImage("Nasa Yuwe"), source_url: "#", license: "N/A" };
  if (imageCache.has(key)) return imageCache.get(key);
  if (cat === "colores") {
    const swatch = buildColorSwatchImage(baseWord);
    if (swatch) {
      imageCache.set(key, swatch);
      return swatch;
    }
  }
  try {
    const data = await fetch(`/api/image?q=${encodeURIComponent(baseWord)}&category=${encodeURIComponent(cat)}`).then((r) => r.json());
    const result = data.ok && data.image_url
      ? data
      : { image_url: fallbackImage(baseWord), source_url: "#", license: "placeholder" };
    imageCache.set(key, result);
    return result;
  } catch (_) {
    const result = { image_url: fallbackImage(baseWord), source_url: "#", license: "placeholder" };
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
      const img = await getFreeImage(t.espanol, data.category);
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
      imageEl.src = fallbackImage(t.espanol);
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
