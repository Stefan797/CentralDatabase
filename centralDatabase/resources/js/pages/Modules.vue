<script setup>
import { usehandleroutingManager } from '@/composables/handleroutingManager.js';

const { goToPath } = usehandleroutingManager();
</script>

<template>
    <customheader></customheader>
    <div class="wrapper">
        <div class="module">
            <div @click="goToPath('/v/projects')" class="cards kanbanbg">
            </div>

            <div @click="goToPath('/v/index-cards')" class="cards indexcardsbg">
            </div>
        </div>
    </div>
</template>

<script>
</script>
  
<style>
@import '@/sass/pages/modules.sass';
</style>

