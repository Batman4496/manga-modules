<script setup lang="ts">
import { watch, ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { RouterLink } from 'vue-router';
import axios from 'axios';
import { API_URL, SOURCES } from "@/constants/routes";
import { getImage } from '@/helpers/helpers';

console.log(API_URL);

type Search = {
  id?: string,
  image: any,
  title: string,
  url: string
};

const route = useRoute();
const router = useRouter();
const loading = ref(true);
const items = ref<Search[]>([]);
const source = ref('');

async function search() {
  const keyword = route.params.keyword;
  if (keyword == null) {
    router.push('/');
  }
  
  const { data } = await axios.get(API_URL + `/${route.query.source ?? SOURCES[0].id}/search/` + keyword);
  source.value = data.source;
  
  const images = data.result.map(async (e: Search) => {
    const image = await getImage(e.image, source.value);
    return {
      ...e,
      image
    }
  });

  items.value = await Promise.all(images);
  loading.value = false;
}


watch(route, () => search());

onMounted(() => search());
</script>

<template>
<div class="flex flex-col gap-5">
  <template v-if="loading">
    <h1>Searching for <span class="text-red-500">'{{ route.params.keyword }}'</span></h1>
  </template>
  <template v-else-if="items.length < 1">
    <h1>No Results found!</h1>
  </template>
  <template v-else>
    <div class="flex flex-col md:grid md:grid-cols-3 gap-2">
      <template v-for="(item, index) in items" :key="index">
        <div class="flex flex-col p-5 items-center justify-center rounde-md hover:rounded-lg transition-all">
          <!-- <image :url="item.image" :source="source" /> -->
          <img :src="item.image" alt="">
          <h1 v-html="item.title"></h1>

        </div>
      </template>
    </div>
  </template>
  <!-- <RouterLink :to="`/manga?url=${}&source=${}`" /> -->
</div>
</template>