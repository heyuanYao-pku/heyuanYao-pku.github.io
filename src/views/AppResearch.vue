<template>
  <div class="home">
    <Introduction />
    <Publications />
  </div>
</template>

<script>
import Introduction from '@/components/MyIntroduction.vue'
import Publications from '@/components/MyPublications.vue'
import Project from '@/components/MyProject'
export default {
  name: 'Home',
  components: {
    Introduction,
    Publications,
    Project
  }
}
</script>
