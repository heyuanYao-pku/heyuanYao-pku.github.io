<template>
  <div ref="container" class="lazy-video">
    <video
      ref="video"
      :src="nearViewport ? src : undefined"
      :poster="nearViewport ? poster : undefined"
      :aria-label="alt"
      preload="none"
      muted
      loop
      playsinline
      controls
    >
      Your browser does not support the video tag.
    </video>
  </div>
</template>

<script>
export default {
  name: 'LazyVideo',
  props: {
    src: { type: String, required: true },
    poster: { type: String, default: undefined },
    alt: { type: String, default: '' }
  },
  data() {
    return { nearViewport: false, visible: false }
  },
  mounted() {
    this.motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)')
    this.motionPreference.addEventListener('change', this.syncPlayback)
    document.addEventListener('visibilitychange', this.syncPlayback)

    if (!('IntersectionObserver' in window)) {
      this.nearViewport = true
      // Keep native controls available without autoplay on older browsers.
      return
    }

    this.loadObserver = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        this.nearViewport = true
        this.loadObserver.disconnect()
        this.$nextTick(this.syncPlayback)
      }
    }, { rootMargin: '240px' })

    this.playObserver = new IntersectionObserver(([entry]) => {
      this.visible = entry.isIntersecting && entry.intersectionRatio >= 0.25
      this.$nextTick(this.syncPlayback)
    }, { threshold: [0, 0.25] })

    this.loadObserver.observe(this.$refs.container)
    this.playObserver.observe(this.$refs.container)
  },
  beforeUnmount() {
    this.loadObserver?.disconnect()
    this.playObserver?.disconnect()
    this.motionPreference?.removeEventListener('change', this.syncPlayback)
    document.removeEventListener('visibilitychange', this.syncPlayback)
    this.$refs.video.pause()
  },
  methods: {
    shouldPlay() {
      return this.nearViewport && this.visible && !document.hidden && !this.motionPreference?.matches
    },
    syncPlayback() {
      const video = this.$refs.video
      if (!video) return
      if (this.shouldPlay()) {
        // Set the property as well as the attribute for Safari autoplay.
        video.muted = true
        video.play()?.then(() => {
          if (!this.shouldPlay()) video.pause()
        }).catch(() => {
          // Native controls allow playback if autoplay is blocked.
        })
      } else {
        video.pause()
      }
    }
  }
}
</script>

<style scoped>
.lazy-video {
  width: 100%;
  height: 100%;
  background: #171717;
}

video {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
