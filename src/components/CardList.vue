<script setup>
  import Card from '@/components/Card.vue'

  defineProps({
    items: Array,
  })

</script>
<template>
  <div class="grid desktop:grid-cols-3 desktop:gap-y-[38px] justify-items-center desktop:w-[880px]
  ml-auto mr-auto mt-32 small:grid-cols-1 small:gap-y-[100px] pb-[40px]">
    <Card v-for="item in items"
          :key="item.id"
          :fileUrl="item.fileurl"
          :price="item.price"
          :allowed="item.allowed"
    />
  </div>

</template>

