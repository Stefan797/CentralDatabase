<template>
    <customheader></customheader>
    <div class="board">
        <!-- <div v-if="smartphonemenu" class="scroll-container">
            <img @click="contentMoveLeft" src="assets/img/arrow-left.png" />
            <img @click="contentMoveRight" src="assets/img/arrow-right.png" />
        </div>

        <div class="board-container section2" id="scrolling_div">
            <div class="example-container">
                <h2>Ideas</h2>
                <div v-if="ideasList" ref="ideasList" class="example-list" @drop="dropEvent($event, 'ideas')">
                    <div v-for="item in ideas" :key="item.id" @click="openTask(item)" :class="{ 'example-box': isDragged }"
                        draggable="true" @dragstart="dragStart($event)" @dragend="dragEnd">
                        <div :style="checkTaskColor(item.color)">{{ item.text }}</div>
                    </div>
                </div>
            </div>

            <button @click="openDialog" class="btn-position btn-color" mat-fab matTooltip="Add New Ticket">
                add
            </button>
        </div> -->
    </div>
</template>
  
<script>
</script>
  
<style>
@import '@/sass/pages/board.sass';
</style>
  