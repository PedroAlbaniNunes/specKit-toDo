const STORAGE_KEY = 'todo-list-items';
const form = document.getElementById('task-form');
const input = document.getElementById('task-input');
const list = document.getElementById('task-list');
const feedback = document.getElementById('feedback');

let tasks = loadTasks();

function loadTasks() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) {
      return [];
    }

    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch (error) {
    console.error('Unable to load tasks', error);
    return [];
  }
}

function saveTasks() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

function showFeedback(message, isError = false) {
  feedback.textContent = message;
  feedback.style.color = isError ? '#b91c1c' : '#0f766e';
}

function updateEmptyState() {
  if (tasks.length === 0) {
    const emptyState = document.createElement('li');
    emptyState.className = 'empty-state';
    emptyState.textContent = 'Nenhuma tarefa por enquanto. Adicione a primeira!';
    list.appendChild(emptyState);
  }
}

function createTask(text) {
  return {
    id: crypto.randomUUID(),
    text: text.trim(),
    completed: false,
    createdAt: new Date().toISOString(),
  };
}

function isDuplicate(text) {
  const normalized = text.trim().toLowerCase();
  return tasks.some((task) => task.text.toLowerCase() === normalized);
}

function addTask(text) {
  const trimmedText = text.trim();

  if (!trimmedText) {
    showFeedback('Por favor, informe uma tarefa válida.', true);
    return false;
  }

  if (isDuplicate(trimmedText)) {
    showFeedback('Essa tarefa já existe na lista.', true);
    return false;
  }

  tasks.unshift(createTask(trimmedText));
  saveTasks();
  render();
  showFeedback('Tarefa adicionada com sucesso!');
  return true;
}

function toggleTask(id) {
  tasks = tasks.map((task) => {
    if (task.id === id) {
      return { ...task, completed: !task.completed };
    }
    return task;
  });
  saveTasks();
  render();
}

function deleteTask(id) {
  tasks = tasks.filter((task) => task.id !== id);
  saveTasks();
  render();
}

function render() {
  list.innerHTML = '';

  if (tasks.length === 0) {
    updateEmptyState();
    return;
  }

  const fragment = document.createDocumentFragment();

  tasks.forEach((task) => {
    const item = document.createElement('li');
    item.className = `task-item${task.completed ? ' completed' : ''}`;

    const taskMain = document.createElement('div');
    taskMain.className = 'task-main';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = task.completed;
    checkbox.className = 'task-checkbox';
    checkbox.setAttribute('aria-label', `Marcar tarefa como ${task.completed ? 'pendente' : 'concluída'}`);
    checkbox.addEventListener('change', () => toggleTask(task.id));

    const text = document.createElement('span');
    text.className = 'task-text';
    text.textContent = task.text;

    const actions = document.createElement('div');
    actions.className = 'task-actions';

    const deleteButton = document.createElement('button');
    deleteButton.type = 'button';
    deleteButton.textContent = '🗑️';
    deleteButton.setAttribute('aria-label', `Excluir tarefa ${task.text}`);
    deleteButton.addEventListener('click', () => deleteTask(task.id));

    taskMain.append(checkbox, text);
    actions.appendChild(deleteButton);
    item.append(taskMain, actions);
    fragment.appendChild(item);
  });

  list.appendChild(fragment);
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const result = addTask(input.value);
  if (result) {
    input.value = '';
    input.focus();
  }
});

render();
