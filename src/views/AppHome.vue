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
          poster: require('@/assets/optimized/lumine-combat.jpg'),
          caption: "Lumine Agent: Defeat the enemies ahead and open the chest"
        },
        {
          type: 'video',
          src: require('@/assets/lumine/npc.mp4'),
          poster: require('@/assets/optimized/lumine-npc.jpg'),
          caption: "Lumine Agent: Talk to NPC Grace"
        },
        {
          type: 'video',
          src: require('@/assets/lumine/defeat.mp4'),
          poster: require('@/assets/optimized/lumine-defeat.jpg'),
          caption: "Lumine Agent: Defeat the Electro Hypostasis"
        },
        {
          type: 'video',
          src: require('@/assets/lumine/clear.mp4'),
          poster: require('@/assets/optimized/lumine-clear.jpg'),
          caption: "Lumine Agent: Clear the Domain"
        },
        {
          type: 'video',
          src: require('@/assets/lumine/Wind.mp4'),
          poster: require('@/assets/optimized/lumine-wind.jpg'),
          caption: "Lumine Agent: Collect the Wind Anemograna to activate a Wind Current, then enter the Wind Barrier to open the chest"
        },
       {
          type: 'video',
          src: require('@/assets/optimized/motion_matching.mp4'),
          poster: require('@/assets/optimized/motion_matching.jpg'),
          caption: "A simple Motion Matching I implemented from scratch."
        },
        {
          type: 'video',
          src: require('@/assets/obstacle.mp4'),
          poster: require('@/assets/optimized/obstacle.jpg'),
          caption: "IsaacGym version of ControlVAE, finetuned on uneven terrian."
        },
        {
          type: 'video',
          src: require('@/assets/indoors.mp4'),
          poster: require('@/assets/optimized/indoors.jpg'),
          caption: "Navigate ControlVAE in the room."
        },
        {
          type: 'video',
          src: require('@/assets/optimized/world_model.mp4'),
          poster: require('@/assets/optimized/world_model.jpg'),
          caption: "Visualization of World Model"
        },
        {
          type: 'video',
          src: require('@/assets/optimized/dance.mp4'),
          poster: require('@/assets/optimized/dance.jpg'),
          caption: "Let's dance in the simulator!"
        },
        
        // Add more items as needed
      ]
    }
  }
}
</script>
