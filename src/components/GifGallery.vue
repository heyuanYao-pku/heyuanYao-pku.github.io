<template>
    <div class="media-gallery-section">
      <h2>{{ title }}</h2>
      <div class="media-gallery-container">
        <div class="media-gallery">
          <div v-for="(item, index) in items" :key="index" class="media-item">
            <!-- Video content -->
            <video v-if="item.type === 'video'" 
                 :src="item.src" 
                 autoplay
                 muted
                 loop
                 playsinline
                 class="media-content">
              Your browser does not support the video tag.
            </video>
            <!-- GIF content -->
            <img v-else 
                 :src="item.src" 
                 :alt="item.caption" 
                 class="media-content">
            <p class="media-caption">{{ item.caption }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MediaGallery',
    props: {
      title: {
        type: String,
        default: 'Media Gallery'
      },
      items: {
        type: Array,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .media-gallery-section {
    margin: 2rem 0;
  }
  
  .media-gallery-section h2 {
    font-size: 1.8rem;
    margin-bottom: 1rem;
    font-weight: 600;
  }
  
  .media-gallery-container {
    position: relative;
    width: 100%;
    overflow: hidden;
  }
  
  .media-gallery {
    display: flex;
    overflow-x: auto;
    scroll-behavior: smooth;
    padding: 1rem 0;
    gap: 1.5rem;
    -webkit-overflow-scrolling: touch;
  }
  
  /* Custom scrollbar */
  .media-gallery::-webkit-scrollbar {
    height: 8px;
  }
  
  .media-gallery::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 4px;
  }
  
  .media-gallery::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 4px;
  }
  
  .media-gallery::-webkit-scrollbar-thumb:hover {
    background: #555;
  }
  
  .media-item {
    flex: 0 0 auto;
    width: 300px;
    margin-right: 1rem;
    display: flex;
    flex-direction: column;
  }
  
  .media-content {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .media-caption {
  color: rgba(255, 255, 255, 0.9); /* Almost white but slightly transparent */
  margin-top: 8px;
  font-size: 14px;
  font-weight: 500;
  text-align: center;
}
  
  @media (max-width: 768px) {
    .media-item {
      width: 250px;
    }
    
    .media-content {
      height: 160px;
    }
  }
  </style>
  
  