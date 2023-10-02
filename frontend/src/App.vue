<script setup lang="ts">
import SearchBar from './components/SearchBar.vue';
import { RouterView } from 'vue-router';
</script>

<template>
  <div class="flex flex-col max-h-screen h-screen w-screen text-white bg-slate-950">
    <header class="border-b-[1px] border-slate-900">
      <search-bar />
    </header>
    <main class="p-5 h-full overflow-scroll">
      <router-view />
    </main>
    <footer class="border-t-[1px] border-slate-900">
    </footer>
  </div>
</template>