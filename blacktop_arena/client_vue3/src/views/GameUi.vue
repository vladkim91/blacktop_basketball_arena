<template>
  <div class="game-ui">
    <div v-for="player in players" :key="player.id">
      {{player.name}}
    </div>
    </div>  
</template>

<script>


export default {

name: "GameUi",
  computed: {
    players() {
      return this.$store.state.players
    }
  }


}
</script>
