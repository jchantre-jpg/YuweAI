const activityCategory = document.getElementById("activityCategory");
const activityBtn = document.getElementById("activityBtn");
const activityArea = document.getElementById("activityArea");
const activityScore = document.getElementById("activityScore");

let currentQuiz = [];

async function loadCategories() {
  const stats = await fetch("/api/stats").then((r) => r.json());
  const cats = Object.keys((stats || {}).category_distribution || {});
  const defaults = ["numeros", "colores", "animales", "saludos", "vocabulario_general", "alimentos"];
  const finalCats = cats.length ? cats : defaults;
  activityCategory.innerHTML = "";
  finalCats.forEach((c) => {
    const opt = document.createElement("option");
    opt.value = c;
    opt.textContent = c;
    activityCategory.appendChild(opt);
  });
}

function renderQuiz(questions) {
  activityArea.innerHTML = "";
  if (!questions?.length) {
    activityArea.innerHTML = "<div class='quiz-card'>No hay actividad disponible en esta categoría.</div>";
    return;
  }
  questions.forEach((q, idx) => {
    const card = document.createElement("div");
    card.className = "quiz-card";
    const options = q.options
      .map((op) => `<label><input type="radio" name="q_${idx}" value="${op}"/> ${op}</label>`)
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
    const data = await fetch(`/api/activity?category=${encodeURIComponent(category)}&limit=6`).then((r) => r.json());
    currentQuiz = data.questions || [];
    renderQuiz(currentQuiz);
  } catch (err) {
    activityArea.innerHTML = `<div class='quiz-card'>Error: ${err.message}</div>`;
  }
}

activityBtn.addEventListener("click", loadActivity);
loadCategories().then(loadActivity);
