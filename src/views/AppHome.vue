<template>
  <div class="home">
    <Introduction />
    <Publications />
    <MediaGallery :items="mediaItems" title="Gallery" />
    <Project />
  </div>
</template>

<script>
import Introduction from '@/components/MyIntroduction.vue'
import Publications from '@/components/MyPublications.vue'
// import Project from '@/components/MyProject.vue'
import MediaGallery from '@/components/GifGallery.vue'

export default {
  name: 'AppHome',
  components: {
    Introduction,
    Publications,
    // Project,
    MediaGallery
  },
  data() {
    return {
      mediaItems: [
       {
          type: 'gif',
          src: require('@/assets/motion_matching.gif'),
          caption: "A simple Motion Matching I implemented from scratch."
        },
        {
          type: 'video',
          src: require('@/assets/obstacle.mp4'),
          caption: "IsaacGym version of ControlVAE, finetuned on uneven terrian."
        },
        {
          type: 'video',
          src: require('@/assets/indoors.mp4'),
          caption: "Nevigate ControlVAE in the room."
        },
        {
          type: 'gif',
          src: require('@/assets/world_model.gif'),
          caption: "Visualization of World Model"
        },
        {
          type: 'gif',
          src: require('@/assets/dance.gif'),
          caption: "Let's dance in the simulator!"
        },
        
        // Add more items as needed
      ]
    }
  }
}
</script>
