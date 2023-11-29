import { defineStore } from 'pinia'

export const useFilesStore = defineStore('files', {
    state: () => ({ 
        count: 0, 
        name: 'Eduardo' 
    }),
})

// state: () => ({ count: 0, name: 'Eduardo' }),
// getters: {
// doubleCount: (state) => state.count * 2,
// },
// actions: {
// increment() {
// this.count++
// },
// },

// import im script setup vue datei