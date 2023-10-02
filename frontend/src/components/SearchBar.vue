<script setup lang="ts">
import { computed, ref } from 'vue';
import { useRouter } from 'vue-router';

const search = ref<string>('');
const router = useRouter();

const error = computed(() => {
  return search.value.trim().length < 4 ? "text-red-500" : "text-white";
});

function submit() {
  if (search.value.trim().length < 4) return;
  router.push('/search/' + search.value.trim());
  search.value = '';
}
</script>

<template>
<div class="flex flex-row justify-between items-center p-5">
  <h1 class="text-xl">Library</h1>
  <div class="flex flex-col gap-1">
    <div class="flex flex-row items-center gap-3">
      <form @submit.prevent="submit">
        <input 
          :class="`${error} bg-transparent`" 
          v-model="search"
          placeholder="Search...."
          type="text"
        />
      </form>
      <button :class="error" @click="submit"><i class="bi bi-search"></i></button>
    </div>
  </div>
</div>
</template>