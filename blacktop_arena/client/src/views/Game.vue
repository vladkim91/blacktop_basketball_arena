<template>
  <div class="game">
    <div class="draft">
      <Draft v-if="!gameReady"/>
      <GameUI v-else/>
    </div>
  </div>
</template>

<script>
import Draft from '../components/Draft.vue';
import GameUI from '../components/GameUI.vue';
export default {
  name: 'Game',
  components: {
    Draft,
    GameUI
  },

  data() {
    return {
      gameReady: false,
      legendTeam: {}
    };
  }
};
</script>