<script setup>
//import { set } from 'vue-demi';
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const user = ref({
    email: '',
    password: ''
});
const checkboxVisible = ref(false);
let token = null;
let user_id = null;
let doNotMemorizeUserData = ref(false);

const router = useRouter();

const login = async () => {
    try {
        const response = await axios.post('/user/login', user.value);
        console.log('Login-Response', response);
        //token = response.data.token;
        user_id = response.data.user.id;
        sessionStorage.setItem('CurrentUserID', user_id);
        //setInformations();
        router.push('/v');
    } catch (error) {
        console.error('Fehler', error);
    }
};

const setInformations = () => {
    if (!doNotMemorizeUserData.value) {
        localStorage.removeItem('token');
        localStorage.removeItem('CurrentUserID');
        sessionStorage.setItem('token', token);
        sessionStorage.setItem('CurrentUserID', user_id);
    } else {
        localStorage.setItem('token', token);
        localStorage.setItem('CurrentUserID', user_id);
    }
};

const showPassword = () => {
    const passwordInput = document.querySelector('#passwordInput');
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
};

const rememberMe = () => {
    checkboxVisible.value = !checkboxVisible.value;
    doNotMemorizeUserData.value = checkboxVisible.value;

    console.log(doNotMemorizeUserData.value);
};

</script>

<template>
    <div class="login-page">
        <div class="inside-container center">
            <div class="centralDatabase-title-container display-flex">
                <h1 class="headline cursor">CentralDatabase</h1>
            </div>

            <div class="login-container">
                <h2>Einloggen</h2>
                <form @submit.prevent="login()">
                    <input v-model="user.email" placeholder="Gebe hier deine E-Mail-Adresse ein" type="text" name="email"
                        autocomplete="off">

                    <div class="password-input">
                        <input v-model="user.password" ref="passwordInput" placeholder="Gebe hier dein Passwort ein"
                            type="password" autocomplete="off">
                        <img @click="showPassword" class="show" src="/images/eye.png">
                    </div>

                    <button class="primary-button" type="submit">Login</button>
                </form>

                <div class="save-user-data">
                    <div @click="rememberMe()" class="show-checkbox"
                        :class="{ 'show-checkbox': !checkboxVisible, 'hide-checkbox': checkboxVisible }">
                        <img class="cursor-pointer" :style="{ 'display': checkboxVisible ? 'block' : 'none' }"
                            src="/images/checkbox-white.png">
                    </div>
                    <p>Benutzerdaten merken</p>
                </div>

                <span>Erstes mal hier? <router-link to="/v/register">Jetzt registrieren</router-link></span>
            </div>
        </div>
    </div>
</template>
  
<script>
</script>
  
<style>
@import '@/sass/pages/login.sass';
</style>