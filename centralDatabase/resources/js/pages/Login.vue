<script setup>
import { set } from 'vue-demi';

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
export default {
    data() {
        return {
            'user': {
                'email': '',
                'password': ''
            },
            checkboxVisible: false,
            token: null,
            user_id: null,
            doNotMemorizeUserData: false
        };
    },
    methods: {
        login() {
            const vm = this;
            axios.post('/user/login', this.user).then(
                response => {
                    console.log('loginresponse', response);
                    vm.token = response.data.token
                    vm.user_id = response.data.user_id
                    vm.setInformations();
                    vm.$router.push('/v');
                },
            ).catch(error => {
                console.log('error');
            })
        },

        setInformations() {
            if (!this.doNotMemorizeUserData) {
                localStorage.removeItem('token');
                localStorage.removeItem('CurrentUserID');
                sessionStorage.setItem('token', this.token);
                sessionStorage.setItem('CurrentUserID', this.user_id);
            } else {
                localStorage.setItem('token', this.token);
                localStorage.setItem('CurrentUserID', this.user_id);
            }
        },

        showPassword() {
            const passwordInput = this.$refs.passwordInput;
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
            } else {
                passwordInput.type = 'password';
            }
        },

        rememberMe() {
            this.checkboxVisible = !this.checkboxVisible;
            if (this.checkboxVisible) {
                this.doNotMemorizeUserData = true;
            } else {
                this.doNotMemorizeUserData = false;
            }

            console.log(this.doNotMemorizeUserData);
        }
    },
};
</script>
  
<style>
@import '@/sass/pages/login.sass';
</style>