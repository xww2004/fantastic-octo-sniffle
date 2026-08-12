<template>
  <div class="card">
    <h1>待办清单</h1>
    <p class="subtitle">Flask + MySQL + Vue 简单示例</p>

    <div v-if="error" class="error">{{ error }}</div>

    <form class="add-form" @submit.prevent="handleAdd">
      <input
        v-model="newTitle"
        type="text"
        placeholder="输入新的待办事项..."
        :disabled="loading"
      />
      <button class="btn-primary" type="submit" :disabled="loading || !newTitle.trim()">
        添加
      </button>
    </form>

    <ul v-if="todos.length" class="todo-list">
      <li v-for="todo in todos" :key="todo.id" class="todo-item">
        <input
          type="checkbox"
          :checked="todo.completed"
          @change="toggleComplete(todo)"
        />
        <span class="todo-title" :class="{ done: todo.completed }">
          {{ todo.title }}
        </span>
        <button class="btn-danger" @click="handleDelete(todo.id)">删除</button>
      </li>
    </ul>
    <div v-else class="empty">暂无待办，添加一条吧</div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { createTodo, deleteTodo, fetchTodos, updateTodo } from "./api";

const todos = ref([]);
const newTitle = ref("");
const loading = ref(false);
const error = ref("");

async function loadTodos() {
  loading.value = true;
  error.value = "";
  try {
    const { data } = await fetchTodos();
    todos.value = data;
  } catch (err) {
    error.value = "加载失败，请确认后端和数据库已启动";
  } finally {
    loading.value = false;
  }
}

async function handleAdd() {
  const title = newTitle.value.trim();
  if (!title) return;

  try {
    const { data } = await createTodo(title);
    todos.value.unshift(data);
    newTitle.value = "";
  } catch (err) {
    error.value = "添加失败";
  }
}

async function toggleComplete(todo) {
  try {
    const { data } = await updateTodo(todo.id, { completed: !todo.completed });
    const index = todos.value.findIndex((item) => item.id === todo.id);
    if (index !== -1) todos.value[index] = data;
  } catch (err) {
    error.value = "更新失败";
  }
}

async function handleDelete(id) {
  try {
    await deleteTodo(id);
    todos.value = todos.value.filter((item) => item.id !== id);
  } catch (err) {
    error.value = "删除失败";
  }
}

onMounted(loadTodos);
</script>
