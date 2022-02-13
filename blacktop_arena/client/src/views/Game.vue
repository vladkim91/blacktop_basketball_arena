<template>
  <div class="game">
    <div class="draft">
      <Draft />
    </div>
  </div>
</template>

<script>
import Draft from '../components/Draft.vue';
export default {
  name: 'Game',
  components: {
    Draft
  },

  data() {
    return {
      draftInProgress: true
    };
  }
};
</script>