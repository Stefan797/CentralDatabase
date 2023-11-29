<template>
    <!-- Hier kommt deine Vue-Komponente -->
</template>
  
<script>
export default {
    mounted() {
        // Event Listener für Key Down hinzufügen
        window.addEventListener('keydown', this.handleKeyDown);

        // Event Listener für Key Up hinzufügen
        window.addEventListener('keyup', this.handleKeyUp);
    },
    beforeDestroy() {
        // Event Listener entfernen, um Speicherleck zu verhindern
        window.removeEventListener('keydown', this.handleKeyDown);
        window.removeEventListener('keyup', this.handleKeyUp);
    },
    methods: {
        handleKeyDown(event) {
            // Hier kannst du die Logik für Key Down implementieren
            // Beispiel: Wenn die Taste 'A' gedrückt wird
            if (event.key === 'a') {
                // Führe eine Aktion aus
                debugger;
                console.log('Taste A wurde gedrückt');
                
                startSpeechToTxt();
            }
        },
        handleKeyUp(event) {
            // Hier kannst du die Logik für Key Up implementieren
            // Beispiel: Wenn die Taste 'A' losgelassen wird
            if (event.key === 'a') {
                // Führe eine Aktion aus
                console.log('Taste A wurde losgelassen');
            }
        }
    }
}
</script>
  
<style>
/* Hier kannst du CSS für deine Komponente hinzufügen, falls benötigt */
</style>