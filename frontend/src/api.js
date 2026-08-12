import axios from "axios";

const api = axios.create({
  baseURL: "/api",
});

export function fetchTodos() {
  return api.get("/todos");
}

export function createTodo(title) {
  return api.post("/todos", { title });
}

export function updateTodo(id, data) {
  return api.patch(`/todos/${id}`, data);
}

export function deleteTodo(id) {
  return api.delete(`/todos/${id}`);
}
