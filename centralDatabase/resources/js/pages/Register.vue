<script setup>
import { ref } from 'vue';
import axios from 'axios';

const user = ref({
    username: '',
    first_name: '',
    last_name: '',
    email: '',
    password: ''
});

const saveData = () => {
    axios.post('/user/create', user.value)
        .then(response => {
            console.log(response);
            //login();
        })
        .catch(error => {
            console.error('Fehler', error);
        });
};

const showPassword = () => {
    const passwordInput = document.querySelector('#passwordInput');
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
};
</script>

<template>
    <div class="register-page">
        <div class="inside-container center">
            <div class="centralDatabase-title-container display-flex">
                <h1 class="headline cursor">CentralDatabase</h1>
            </div>

            <div class="register-container">
                <h2>Neu registrieren</h2>
                <form @submit.prevent="saveData()">
                    <!-- Input Username -->
                    <input v-model="user.username" placeholder="Gebe hier deinen Benutzernamen ein" type="text"
                        autocomplete="off" name="username">

                    <!-- Input Vorname -->
                    <input v-model="user.first_name" placeholder="Gebe hier deinen Vornamen ein" type="text"
                        autocomplete="off" name="first_name">


                    <!-- Input Nachname -->
                    <input v-model="user.last_name" placeholder="Gebe hier deinen Nachnamen ein" type="text"
                        autocomplete="off" name="last_name">


                    <!-- Input Email -->
                    <input v-model="user.email" placeholder="Gebe hier deine E-Mail-Adresse ein" type="text"
                        autocomplete="off" name="email">

                    <!-- Input Password -->
                    <div class="password-input">
                        <input v-model="user.password" ref="passwordInput" placeholder="Gebe hier dein Passwort ein"
                            type="password" autocomplete="off">
                        <img @click="showPassword" class="show" src="/images/eye.png">
                    </div>

                    <button class="primary-button" type="submit">
                        Submit
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>
  
<script>
</script>
  
<style>
@import '@/sass/pages/register.sass';
</style>
  