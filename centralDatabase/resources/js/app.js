import { createApp } from 'vue'
import { createPinia } from 'pinia'
// import the root component App from a single-file component.
import App from './components/App.vue'
import Search from './components/Search.vue'
import Add from './components/Add.vue'
import Header from './components/Header.vue'
import Speech from './components/Speech.vue'
import Upload from './components/Upload.vue'
import Keyboard from './components/Keyboard.vue'
import CodeDisplay from './components/CodeDisplay.vue'
import Directory from './pages/Directory.vue'
import Home from './pages/Home.vue'
import Modules from './pages/Modules.vue'
import Contacts from './pages/Contacts.vue'
import Chat from './pages/Chat.vue'
import Login from './pages/Login.vue'
import Register from './pages/Register.vue'
import RegisterEmployee from './pages/RegisterEmployee.vue'
import Projects from './pages/Projects.vue'
import Board from './pages/Board.vue'
import File from './pages/File.vue'
import Cooking from './pages/Cooking.vue'
import IndexCards from './pages/IndexCards.vue'


import router from './router.js'

import './bootstrap';


import { basicSetup } from 'codemirror'
import VueCodemirror from 'vue-codemirror'

const pinia = createPinia()
const app = createApp();
app.use(router);
app.use(pinia)
app.use(VueCodemirror, {
    // optional default global options
    autofocus: true,
    disabled: false,
    indentWithTab: true,
    tabSize: 2,
    placeholder: 'Code goes here...',
    extensions: [basicSetup]
    // ...
});

app.component('app', App);
app.component('search', Search);
app.component('add', Add);
app.component('customheader', Header);
app.component('directory', Directory);
app.component('home', Home);
app.component('modules', Modules);
app.component('contacts', Contacts);
app.component('chat', Chat);
app.component('speech', Speech);
app.component('login', Login);
app.component('register', Register);
app.component('registerEmployee', RegisterEmployee);
app.component('upload', Upload);
app.component('Projects', Projects);
app.component('board', Board);
app.component('file', File);
app.component('cooking', Cooking);
app.component('keyboard', Keyboard);
app.component('indexcards', IndexCards);
app.component('codeDisplay', CodeDisplay);

app.mount('#app');