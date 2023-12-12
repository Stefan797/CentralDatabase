<script setup>
</script>

<template>
    <div class="add center">
        <form class="form-container column">

            <div class="text-container">
                <textarea class="textarea-focus-settings" id="message" name="message" required>
                </textarea>
            </div>

            <div class="button-container">
                <div class="choose-file-container">
                    <select class="primary-button" id="category" name="category" required>
                        <option value="" disabled selected>Wähle hier die Datei aus</option>
                        <option value="Option 1">Option 1</option>
                        <option value="Option 2">Option 2</option>
                        <option value="Option 3">Option 3</option>
                    </select>
                </div>
                <div class="submit-btn-container">
                    <button class="primary-button" type="submit">Hinzufügen</button>
                </div>
                
            </div>
        </form>
    </div>
</template>

<script>
</script>
  
<style>
@import '@/sass/components/add.sass';
</style>