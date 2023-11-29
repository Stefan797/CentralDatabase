<script setup>
</script>

<template>
    <div class="register-page">
        <div class="inside-container center">
            <div class="register-container">
                <h2>Neu registrieren</h2>
                <form @submit.prevent="saveData()">
                    <!-- Input Username -->
                    <!-- <input v-model="employee.username" placeholder="Gebe hier deinen Benutzernamen ein" type="text"
                        autocomplete="off" name="username">
                    <p v-if="isInvalid('username')" class="error">{{ getErrorMessage('username') }}</p> -->

                    <!-- Input Vorname -->
                    <input v-model="employee.first_name" placeholder="Gebe hier deinen Vornamen ein" type="text"
                        autocomplete="off" name="first_name">
                    

                    <!-- Input Nachname -->
                    <input v-model="employee.last_name" placeholder="Gebe hier deinen Nachnamen ein" type="text"
                        autocomplete="off" name="last_name">
                    

                    <!-- Input Email -->
                    <input v-model="employee.email" placeholder="Gebe hier deine E-Mail-Adresse ein" type="text"
                        autocomplete="off" name="email">
                    
                    
                    <!-- Input phone
                    <input v-model="employee.phone" placeholder="Gebe hier deine E-Mail-Adresse ein" type="text"
                        autocomplete="off" name="phone"> -->
                    
                    
                    <!-- Input Email -->
                    <input v-model="employee.current_experience" placeholder="Gebe hier deine experience ein" type="text"
                        autocomplete="off" name="current_experience">
                    
                    
                    <!-- Input Email -->
                    <input v-model="employee.city" placeholder="Gebe hier deine city ein" type="text"
                        autocomplete="off" name="city">
                    
                    
                    <!-- Input Email -->
                    <input v-model="employee.state" placeholder="Gebe hier deine state ein" type="text"
                        autocomplete="off" name="state">
                    
                    
                    <!-- Input Email -->
                    <input v-model="employee.gender" placeholder="Gebe hier deine gender ein" type="text"
                        autocomplete="off" name="gender">
                    

                    <!-- Input Password
                    <div class="password-input">
                        <input ref="passwordInput" @input="showPassword" v-model="registerForm.password"
                            placeholder="Gebe hier dein Passwort ein" type="password" autocomplete="off" name="password">
                        <img @click="togglePasswordVisibility" class="show" src="/images/checkbox-white.png"
                            alt="Show Password">
                    </div>
                    <p v-if="isInvalid('password')" class="error">{{ getErrorMessage('password') }}</p> -->

                    <button class="primary-button" type="submit">
                        Submit
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            'employee': {
                'first_name': '',
                'last_name': '',
                'email': '',
                'current_experience': '',
                'city': '',
                'state': '',
                'gender': ''
            }
        };
    },

    methods: {
        saveData() {
            axios.post('/employee/create', this.employee).then(
                response => {
                    console.log(response);
                }
            ). catch(error => {
                console.log('error');
            })
        }
    }
}
</script>
  
<style>
@import '@/sass/pages/register.sass';
</style>