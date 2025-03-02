<template>
  <div class="home">
    <Introduction />
    <Publications />
    <Project />
  </div>
</template>

<script>
import Introduction from '@/components/MyIntroduction.vue'
import Publications from '@/components/MyPublications.vue'
import Project from '@/components/MyProject.vue'
export default {
  name: 'AppHome',
  components: {
    Introduction,
    Publications,
    Project,
  }
}
</script>
