<script setup>
</script>

<template>
    <div class="search center">
        <form class="form-container display-flex column">
            <div class="upper-part display-flex">
                <div class="text-container">
                    <textarea id="message" name="message" placeholder="Kopiere oder schreibe hier den Text" required>
                    </textarea>
                </div>

                <div class="choose-file-container">
                    <select id="category" name="category" required>
                        <option value="" disabled selected>Wähle hier die Datei aus</option>
                        <option value="Option 1">Option 1</option>
                        <option value="Option 2">Option 2</option>
                        <option value="Option 3">Option 3</option>
                    </select>
                </div>
            </div>


            <div class="add-btn-container flex-end">
                <img src="/images/loupe.png">
                <!-- <button class="cursor" type="submit">Hinzufügen</button> -->
            </div>
        </form>
    </div>
</template>

<script>
</script>
  
<style>
@import '@/sass/components/search.sass';   
</style>