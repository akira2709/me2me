<script setup>


  defineProps({
    price: Number,
    fileUrl: String,
    allowed: Boolean,
  })
</script>

<template>
  <div class="h-[339px] w-[256px] border-0 rounded-[30px] relative z-0 cursor-pointer small:w-[370px] small:h-[300px] select-none">
    <img :src="fileUrl" alt="item" class="h-[266px] w-[256px] border-0 rounded-t-[30px] blur-[6px] small:w-[370px] small:h-[300px]" v-if="!allowed"/>
    <img :src="fileUrl" alt="item" class="h-[266px] w-[256px] border-0 rounded-t-[30px] small:w-[370px] small:h-[300px]" v-if="allowed"/>
    <img src="/notAllowed.svg" alt="not allowed" v-if="!allowed" class="absolute top-[111px] left-[105px] small:left-[140px] small:w-[100px]">
    <div class="h-[266px] w-[256px] border-[2px] border-white absolute top-0 rounded-t-[30px] small:w-[370px] small:h-[300px]"></div>
    <div class="h-[73px] w-[256px] bg-white rounded-b-[30px] absolute small:w-[370px]">
      <div class="text-gray-900 w-[120px]  ml-[124px] mt-[18px] flex small:ml-[224px]" v-if="!allowed">
        <p class="font-sans font-medium mr-[15px]">{{ price }} руб</p>
        <img src="/plus.svg" alt="plus">
      </div>

    </div>
  </div>
</template>

<style scoped>

</style>