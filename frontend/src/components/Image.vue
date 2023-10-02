<script setup lang="ts">
import { onBeforeMount, ref } from 'vue';
import { getImage } from '@/helpers/helpers';

const props = defineProps({
  url: {
    required: true,
    type: String
  },
  source: {
    required: true,
    type: String
  },
});

const image = ref<string>('');

onBeforeMount(async () => {
  console.log("hello");
  image.value = await getImage(props.url, props.source);
})

</script>

<template>
<img :src="image" />
</template>