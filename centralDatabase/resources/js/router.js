import { createRouter, createWebHistory } from 'vue-router'

// Erstelle eine neue Instanz von Vue Router
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/v',
      name: 'Home',
      component: () => import('./pages/Home.vue')
    },
    {
      path: '/v/directory',
      name: 'Directory',
      component: () => import('./pages/Directory.vue')
    },
    {
      path: '/v/modules',
      name: 'Modules',
      component: () => import('./pages/Modules.vue')
    },
    {
      path: '/v/contacts',
      name: 'Contacts',
      component: () => import('./pages/Contacts.vue')
    },
    {
      path: '/v/chat',
      name: 'Chat',
      component: () => import('./pages/Chat.vue')
    },
    {
      path: '/v/projects',
      name: 'Projects',
      component: () => import('./pages/Projects.vue')
    },
    {
      path: '/v/board',
      name: 'Board',
      component: () => import('./pages/Board.vue')
    },
    // {
    //   path: '/v/file',
    //   name: 'File',
    //   component: () => import('./pages/File.vue')
    // },
    {
      path: '/v/file/:filename', // Verwenden Sie ein dynamisches Segment für den Dateinamen
      name: 'File', // Optional: Name der Route
      component: () => import('./pages/File.vue'), // Beispielansicht, in der der Dateiname angezeigt wird
    },
    {
      path: '/v/cooking',
      name: 'Cooking',
      component: () => import('./pages/Cooking.vue')
    },
    {
      path: '/v/index-cards',
      name: 'IndexCards',
      component: () => import('./pages/IndexCards.vue')
    },
    {
      path: '/v/login',
      name: 'Login',
      component: () => import('./pages/Login.vue')
    },
    {
      path: '/v/register',
      name: 'Register',
      component: () => import('./pages/Register.vue')
    },
    {
      path: '/v/registerEmployee',
      name: 'RegisterEmployee',
      component: () => import('./pages/RegisterEmployee.vue')
    }
  ]
})


export default router