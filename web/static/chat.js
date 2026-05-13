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

let currentMode = "estudiante";

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
  pushAVIMessage("Walek ✨ Soy AVI, tu acompañante para aprender Nasa Yuwe.");
  pushAVIMessage("Puedes hacer preguntas, practicar traducciones y recibir guía pedagógica.");
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
      <div class="meta">ID: ${ctx.id} | Categoria: ${ctx.categoria} | Tipo: ${ctx.record_type} | Fuente: ${ctx.fuente_nombre} | Confianza: ${ctx.nivel_confianza || "n/a"} | Score: ${ctx.score}</div>
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
    pushAVIMessage("Ocurrió un error consultando el modelo.");
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
resetChat();
