<script setup>
</script>

<template>
    <customheader></customheader>
    <div class="file-wrapper">

        <!-- <video src=""></video> -->
        <p>
            test
        </p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            editFile: false
        };
    },
    methods: {
        editFile() {
            console.log('test');
        }
    },
};
</script>
  
<style>
@import '@/sass/pages/file.sass';
</style>