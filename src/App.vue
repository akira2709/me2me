<script setup>
  import { onMounted, watch, ref, reactive, provide } from 'vue';
  import axios from 'axios'
  import CardList from './components/CardList.vue'
  import Header from './components/Header.vue'
  import Search from './components/Search.vue'

  const items = ref([])
  const user = ref('')
  const Auth = async () => {
    const {data} = await axios.get('http://0.0.0.0:5000/auth');
    const token = encodeURIComponent(data);
    document.cookie = `token=${token}`;
    window.location.href = `https://t.me/dfgvcxz_bot?start=${token}`;
  };

  const getItems = async () => {
    try {
      const {data} = await axios.get('http://0.0.0.0:5000/items')
      items.value = data
    } catch (err){
      console.log(err)
    }
  }
  const isRegister = async () => {
    let cookie = document.cookie.split('=')[1]
    try {
      const {data} = await axios.get(`http://0.0.0.0:5000/login/${cookie}`)
      if (data) {
        user.value = data
        items.value.map((el) => {
          if (user.value[0].buy.indexOf(el.id) !== -1){
            el['allowed'] = true
          } else (el['allowed'] = false)
        })
      }
    } catch (er) {console.log(er)}
  }
  onMounted(async () => {
    await getItems()
    await isRegister()
  })
</script>

<template>
  <div class="bg-black desktop:w-5/6 m-auto desktop:rounded-[30px] shadow-xl desktop:mt-14 @screen mt-0 w-full small:-z-10">
    <Header />
    <Search />
    <CardList :items="items"/>
    <button @click="Auth" v-if="!user">auth</button>
  </div>
</template>


<style scoped>

</style>
