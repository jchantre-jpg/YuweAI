const scrollButtons = document.querySelectorAll("[data-scroll-target]");
const modeButtons = document.querySelectorAll(".mode-chip");
const quickButtons = document.querySelectorAll(".quick-chip");

const chatForm = document.getElementById("chatForm");
const clearChatBtn = document.getElementById("clearChat");
const queryInput = document.getElementById("query");
const chatMessages = document.getElementById("chatMessages");
const statusEl = document.getElementById("status");
const answerEl = document.getElementById("answer");
const contextsEl = document.getElementById("contexts");

const categorySelect = document.getElementById("categorySelect");
const lessonBtn = document.getElementById("lessonBtn");
const lessonEl = document.getElementById("lesson");

const activityCategory = document.getElementById("activityCategory");
const activityBtn = document.getElementById("activityBtn");
const activityArea = document.getElementById("activityArea");
const activityScore = document.getElementById("activityScore");

let currentMode = "estudiante";
let currentQuiz = [];

function smoothScrollTo(selector) {
  const target = document.querySelector(selector);
  if (!target) return;
  const top = target.getBoundingClientRect().top + window.scrollY - 76;
  window.scrollTo({ top, behavior: "smooth" });
}

scrollButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const s = btn.getAttribute("data-scroll-target");
    if (s) smoothScrollTo(s);
  });
});

modeButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    modeButtons.forEach((b) => b.classList.remove("is-active"));
    btn.classList.add("is-active");
    currentMode = btn.getAttribute("data-mode") || "estudiante";
    pushAVIMessage(`Modo actualizado a ${currentMode}.`);
  });
});

quickButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const type = btn.getAttribute("data-quick");
    const map = {
      saludo: "Quiero practicar saludos en nasa yuwe",
      vocabulario: "Enseñame vocabulario basico de animales",
      actividad: "Sugerir actividad para aprender colores",
      docente: "Soy docente, dame una estrategia para clase",
    };
    queryInput.value = map[type] || "";
    queryInput.focus();
  });
});

function createMessage(role, text, meta = "") {
  const div = document.createElement("div");
  div.className = `msg ${role}`;
  div.innerHTML = `<div>${text}</div>${meta ? `<small>${meta}</small>` : ""}`;
  return div;
}

function pushUserMessage(text) {
  chatMessages.appendChild(createMessage("user", text));
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function pushAVIMessage(text, meta = "") {
  chatMessages.appendChild(createMessage("avi", text, meta));
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function resetChat() {
  chatMessages.innerHTML = "";
  pushAVIMessage("Walek ✨ Soy AVI, tu acompanante para aprender Nasa Yuwe.");
  pushAVIMessage("Puedes usar chat, diccionario interactivo o actividades por categoria.");
}

function renderContexts(contexts) {
  contextsEl.innerHTML = "";
  if (!contexts?.length) {
    contextsEl.innerHTML = "<div class='ctx'>Sin contextos recuperados.</div>";
    return;
  }
  contexts.forEach((ctx) => {
    const div = document.createElement("div");
    div.className = "ctx";
    div.innerHTML = `
      <div class="row1">${ctx.espanol} -> ${ctx.nasa_yuwe}</div>
      <div class="meta">Categoria: ${ctx.categoria} | Tipo: ${ctx.record_type} | Fuente: ${ctx.fuente_nombre} | Score: ${ctx.score}</div>
    `;
    contextsEl.appendChild(div);
  });
}

async function askAVI(message) {
  statusEl.textContent = "Consultando al AVI...";
  try {
    const res = await fetch(`/api/search?q=${encodeURIComponent(message)}&top_k=5`);
    const data = await res.json();
    answerEl.textContent = data.answer || "Sin respuesta.";
    renderContexts(data.contexts || []);
    const m = data.meta || {};
    statusEl.textContent = `Candidatos: ${m.candidates ?? 0} | Recuperados: ${m.retrieved ?? 0} | Cache: ${m.cache_hit ? "si" : "no"}`;
    pushAVIMessage(data.answer || "No tengo respuesta.");
  } catch (err) {
    statusEl.textContent = `Error: ${err.message}`;
    pushAVIMessage("Ocurrio un error consultando el modelo.");
  }
}

function renderLesson(data) {
  lessonEl.innerHTML = "";
  if (!data.terms?.length) {
    lessonEl.innerHTML = "<div class='term'>No hay terminos para esta categoria.</div>";
    return;
  }
  data.terms.forEach((t) => {
    const div = document.createElement("div");
    div.className = "term";
    div.innerHTML = `
      <div class="nasa">${t.nasa_yuwe}</div>
      <div class="esp">${t.espanol}</div>
      <small>Fuente: ${t.fuente_nombre}</small>
    `;
    lessonEl.appendChild(div);
  });
}

async function loadCategories() {
  try {
    const stats = await fetch("/api/stats").then((r) => r.json());
    const cats = Object.keys((stats || {}).category_distribution || {});
    // fallback categories if backend not returning list
    const defaults = ["numeros", "colores", "animales", "saludos", "vocabulario_general", "alimentos"];
    const finalCats = cats.length ? cats : defaults;
    categorySelect.innerHTML = "";
    activityCategory.innerHTML = "";
    finalCats.forEach((c) => {
      const opt1 = document.createElement("option");
      opt1.value = c;
      opt1.textContent = c;
      categorySelect.appendChild(opt1);
      const opt2 = document.createElement("option");
      opt2.value = c;
      opt2.textContent = c;
      activityCategory.appendChild(opt2);
    });
  } catch {
    const defaults = ["numeros", "colores", "animales", "saludos", "vocabulario_general", "alimentos"];
    defaults.forEach((c) => {
      const o1 = document.createElement("option");
      o1.value = c; o1.textContent = c; categorySelect.appendChild(o1);
      const o2 = document.createElement("option");
      o2.value = c; o2.textContent = c; activityCategory.appendChild(o2);
    });
  }
}

async function loadLesson() {
  const category = categorySelect.value;
  lessonEl.innerHTML = "<div class='term'>Cargando vocabulario...</div>";
  try {
    const data = await fetch(`/api/dictionary?category=${encodeURIComponent(category)}&limit=12`).then((r) => r.json());
    renderLesson(data);
  } catch (err) {
    lessonEl.innerHTML = `<div class='term'>Error: ${err.message}</div>`;
  }
}

function renderQuiz(questions) {
  activityArea.innerHTML = "";
  if (!questions?.length) {
    activityArea.innerHTML = "<div class='quiz-card'>No hay actividad disponible en esta categoria.</div>";
    return;
  }
  questions.forEach((q, idx) => {
    const card = document.createElement("div");
    card.className = "quiz-card";
    const options = q.options
      .map(
        (op, i) => `
          <label><input type="radio" name="q_${idx}" value="${op}"/> ${op}</label>
        `
      )
      .join("");
    card.innerHTML = `<strong>${idx + 1}. ${q.prompt}</strong><div class="quiz-options">${options}</div>`;
    activityArea.appendChild(card);
  });

  const btn = document.createElement("button");
  btn.className = "btn btn-primary";
  btn.textContent = "Calificar actividad";
  btn.addEventListener("click", gradeQuiz);
  activityArea.appendChild(btn);
}

function gradeQuiz() {
  let score = 0;
  currentQuiz.forEach((q, idx) => {
    const checked = document.querySelector(`input[name="q_${idx}"]:checked`);
    if (checked && checked.value === q.answer) score += 1;
  });
  activityScore.textContent = `Resultado: ${score}/${currentQuiz.length}`;
}

async function loadActivity() {
  const category = activityCategory.value;
  activityArea.innerHTML = "<div class='quiz-card'>Generando actividad...</div>";
  activityScore.textContent = "";
  try {
    const data = await fetch(`/api/activity?category=${encodeURIComponent(category)}&limit=5`).then((r) => r.json());
    currentQuiz = data.questions || [];
    renderQuiz(currentQuiz);
  } catch (err) {
    activityArea.innerHTML = `<div class='quiz-card'>Error: ${err.message}</div>`;
  }
}

chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const msg = queryInput.value.trim();
  if (!msg) return;
  pushUserMessage(msg);
  queryInput.value = "";
  await askAVI(msg);
});

clearChatBtn.addEventListener("click", resetChat);
lessonBtn.addEventListener("click", loadLesson);
activityBtn.addEventListener("click", loadActivity);

resetChat();
loadCategories().then(() => {
  loadLesson();
  loadActivity();
});
