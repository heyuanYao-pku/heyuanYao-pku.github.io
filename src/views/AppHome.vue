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
          type: 'video',
          src: require('@/assets/lumine/combat.mp4'),
          caption: "Lumine Agent: Defeat the enemies ahead and open the chest"
        },
        {
          type: 'video',
          src: require('@/assets/lumine/npc.mp4'),
          caption: "Lumine Agent: Talk to NPC Grace"
        },
        {
          type: 'video',
          src: require('@/assets/lumine/defeat.mp4'),
          caption: "Lumine Agent: Defeat the Electro Hypostasis"
        },
        {
          type: 'video',
          src: require('@/assets/lumine/clear.mp4'),
          caption: "Lumine Agent: Clear the Domain"
        },
        {
          type: 'video',
          src: require('@/assets/lumine/Wind.mp4'),
          caption: "Lumine Agent: Collect the Wind Anemograna to activate a Wind Current, then enter the Wind Barrier to open the chest"
        },
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
          caption: "Navigate ControlVAE in the room."
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
