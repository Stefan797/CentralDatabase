<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
// import { usehandleroutingManager } from '@/composables/handleroutingManager.js';
// const routingManager = usehandleroutingManager();

const user = ref({});;
const router = useRouter();

const logout = async () => {
  try {
    const response = await axios.get('/user/logout', user.value);
    console.log('Logout-Reaktion', response);
    // clearInformations();
    router.push('/v/login');
  } catch (error) {
    console.error('Fehler', error);
  }
};

const openInNewTab = (path) => {
  const routeData = router.resolve({ path });
  window.open(routeData.href, '_blank');
};

// const clearInformations = () => {
//   localStorage.removeItem('token');
//   localStorage.removeItem('CurrentUserID');
//   sessionStorage.removeItem('token');
//   sessionStorage.removeItem('CurrentUserID');
// };
</script>

<template>
  <div class="header center">
    <div class="icon-container-left">
      <img @click="logout()" src="/images/logout.png" />
    </div>

    <router-link to="/v">
      <h1>CentralDatabase</h1>
    </router-link>

    <div class="icon-container-right">
      <a href="#" @click="openInNewTab('/v/cooking')"><img src="/images/kochmütze.png" /></a>
      <a href="#" @click="openInNewTab('/v/chat')"><img src="/images/chat.png" /></a>
      <a href="#" @click="openInNewTab('/v/contacts')"><img src="/images/contacts.png" /></a>
      <a href="#" @click="openInNewTab('/v/modules')"><img src="/images/modules.png" /></a>
      <a href="#" @click="openInNewTab('/v/directory')"><img src="/images/directory.png" /></a>
    </div>
  </div>
</template>

<script>
</script>
  
<style>
@import '@/sass/components/header.sass';
</style>