<template>
  <div class="projects">
    <h2>Galleries</h2>
    <div class="publication-list">
      <div v-for="pub in publications" :key="pub.title" class="publication-item">
        <img :src="pub.image" :alt="pub.title" class="pub-image">
        <div class="pub-info">
          <h3>{{ pub.title }}</h3>
          <p class="authors">{{ pub.authors }}</p>
          <p class="venue">{{ pub.venue }}</p>
          <div class="pub-links">
            <a v-for="link in pub.links" 
               :key="link.type" 
               :href="link.url" 
               class="pub-link">
              <i :class="link.icon"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      projects: [
      {
          title: "MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations",
          authors: "Heyuan yao, Zhenhua Song, Yuyang Zhou, Tenglong Ao, Baoquan Chen, Libin Liu",
          venue: "August 2024 In SIGGRAPH",
          image: require("../assets/skill.gif"),
          links: [
            { type: "pdf", url: "https://arxiv.org/abs/2310.1019", icon: "fas fa-file-pdf" },
            { type: "github", url: "https://github.com/heyuanYao-pku/MoConVQ", icon: "fab fa-github" },
            { type: "video", url: "https://www.bilibili.com/video/BV13D421N7zp/", icon: "fab fa-youtube" }
          ]
        },
        {
          title: "ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters",
          authors: "Heyuan yao, Zhenhua Song, Baoquan Chen, Libin Liu",
          venue: "December 2022 In SIGGRAPH Asia",
          image: require("../assets/skill.gif"),
          links: [
            { type: "pdf", url: "https://arxiv.org/abs/2210.06063", icon: "fas fa-file-pdf" },
            { type: "github", url: "https://github.com/heyuanYao-pku/Control-VAE", icon: "fab fa-github" },
            { type: "video", url: "https://www.youtube.com/watch?v=ELZ7m4rLCgk", icon: "fab fa-youtube" }
          ]
        },
        // 添加更多出版物...
      ]
    }
  }
}
</script>

<style scoped>
.publications {
  margin-top: 4rem;
}

.publication-item {
  display: flex;
  gap: 2rem;
  margin-bottom: 2rem;
  padding: 1rem;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.05);
}

.pub-image {
  width: 200px;
  border-radius: 4px;
}

.pub-info {
  flex: 1;
}

h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.2rem;
}

.authors {
  color: #ccc;
  margin: 0.5rem 0;
}

.venue {
  color: #999;
  font-style: italic;
}

.pub-links {
  margin-top: 1rem;
  display: flex;
  gap: 1rem;
}

.pub-link {
  color: var(--link-color);
  text-decoration: none;
}

.pub-link:hover {
  color: #fff;
}
</style>
