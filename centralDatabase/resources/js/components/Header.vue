<script setup>
</script>

<template>
    <div class="header center">
        <div class="icon-container-left">
            <img @click="logout()" src="/images/logout.png"/>
        </div>

        <router-link to="/v"><h1>CentralDatabase</h1></router-link>
        
        <div class="icon-container-right">
            <router-link to="/v/cooking"><img src="/images/kochmütze.png"/></router-link>
            <router-link to="/v/chat"><img src="/images/chat.png"/></router-link>
            <router-link to="/v/contacts"><img src="/images/contacts.png"/></router-link>
            <router-link to="/v/modules"><img src="/images/modules.png"/></router-link>
            <router-link to="/v/directory"><img src="/images/directory.png"/></router-link>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            //logoutresponse: null,
        };
    },
    methods: {
        logout() {
            const vm = this;
            axios.get('/user/logout', this.user).then(
                response => {
                    console.log('logoutresponse', response);
                    //vm.logoutresponse = response.logout
                    vm.clearInformations();
                    vm.$router.push('/v/login');
                },
            ).catch(error => {
                console.log('error');
            })
        },

        clearInformations() {
            localStorage.removeItem('token');
            localStorage.removeItem('CurrentUserID');
            sessionStorage.removeItem('token', this.token);
            sessionStorage.removeItem('CurrentUserID', this.user_id);
        }
    },
};
</script>
  
<style>
@import '@/sass/components/header.sass';
</style>