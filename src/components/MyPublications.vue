<template>
  <div class="publications">
    <h2>Publications</h2>
    <div class="publication-list">
      <div v-for="pub in publications" :key="pub.title" class="publication-item">
        <div class="pub-image-container">
          <img :src="pub.image" :alt="pub.title" class="pub-image">
        </div>
        <div class="pub-info">
          <h3>{{ pub.title }}</h3>
          <p class="authors">
            <!-- 若 customAuthorText 存在，就直接显示 -->
            <span v-if="pub.customAuthorText">{{ pub.customAuthorText }}</span>

            <!-- 否则循环显示 authorsList -->
            <template v-else v-for="(author, index) in pub.authorsList" :key="index">
              <strong v-if="author.isCoFirst">{{ author.name }}*</strong>
              <template v-else>{{ author.name }}</template>
              {{ index < pub.authorsList.length - 1 ? ', ' : '' }}
            </template>
          </p>

          <!-- 如果有共同一作者标记 -->
          <p class="note" v-if="!pub.customAuthorText && pub.authorsList?.some(a => a.isCoFirst)">
            * denotes co-first authors
          </p>
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
      publications: [
        {
          title: "SRBTrack: Terrain-Adaptive Tracking of a Single-Rigid-Body Character Using Momentum-Mapped Space-Time Optimization",
          authorsList: [
            { name: "Hanyang Cao", isCoFirst: true },
            { name: "Heyuan Yao", isCoFirst: true },
            { name: "Libin Liu", isCoFirst: false },
            { name: "Taesoo Kwon", isCoFirst: false },
          ],
          venue: "December 2025 In SIGGRAPH Asia",
          image: require("../assets/SRBTrack.jpg"),
          links: [
            { type: "pdf", url: "https://hanyang9.github.io/SRBTrack/static/paper/saconferencepapers25-15.pdf", icon: "fas fa-file-pdf" },
            { type: "video", url: "https://www.youtube.com/watch?v=yf_V8TVO71s", icon: "fab fa-youtube" }
          ]
        },
        {
          title: "Social Agent: Mastering Dyadic Nonverbal Behavior Generation via Conversational LLM Agents",
          authorsList: [{name:"Zeyi Zhang"}, {name:"Yanju Zhou"}, {name:"Heyuan Yao"}, {name:"Tenglong Ao"}, {name:"Xiaohang Zhan"}, {name:"Libin Liu"}],
          venue: "December 2025 In SIGGRAPH Asia",
          image: require("../assets/socialAgent.jpg"),
          links: [
            { type: "pdf", url: "https://arxiv.org/abs/2510.04637", icon: "fas fa-file-pdf" },
            { type: "github", url: "https://pku-mocca.github.io/Social-Agent-Page/", icon: "fab fa-github" },
            { type: "video", url: "https://www.youtube.com/watch?v=fYv43x27zjw", icon: "fab fa-youtube" }
          ]
        },
        {
          title: "Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents",
          customAuthorText: "contributor, at Bytedance Seed",
          venue: "Technical Report",
          image: require("../assets/scaling.png"),
          links: [
            { type: "pdf", url: "https://arxiv.org/abs/2510.23691", icon: "fas fa-file-pdf" },
            { type: "github", url: "https://pku-mocca.github.io/Social-Agent-Page/", icon: "fab fa-github" },
            { type: "video", url: "https://www.youtube.com/watch?v=fYv43x27zjw", icon: "fab fa-youtube" }
          ]
        },
      {
          title: "MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations",
          authorsList: [
          {name:"Heyuan Yao"}, {name:"Zhenhua Song"}, {name:"Yuyang Zhou"}, {name:"Tenglong Ao"}, {name:"Baoquan Chen"}, {name:"Libin Liu"}],
          venue: "August 2024 In SIGGRAPH (Journal Track)",
          image: require("../assets/moconvq.gif"),
          links: [
            { type: "pdf", url: "https://arxiv.org/abs/2310.1019", icon: "fas fa-file-pdf" },
            { type: "github", url: "https://github.com/heyuanYao-pku/MoConVQ", icon: "fab fa-github" },
            { type: "video", url: "https://www.bilibili.com/video/BV13D421N7zp/", icon: "fab fa-youtube" }
          ]
        },
        {
          title: "ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters",
          authorsList: [
            {name: "Heyuan Yao"}, {name: "Zhenhua Song"}, {name: "Baoquan Chen"}, {name: "Libin Liu"}],
          venue: "December 2022 In SIGGRAPH Asia (Journal Track), selected to Trailer",
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

.pub-image-container {
  width: 280px; /* Adjust width as needed */
  position: relative;
  overflow: hidden;
}

.pub-image-container::before {
  content: "";
  display: block;
  padding-top: 56.25%; /* 16:9 aspect ratio (9/16 = 0.5625) */
}

.pub-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
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

@media (max-width: 768px) {
  .publication-item {
    flex-direction: column;
    gap: 1rem;
  }
  
  .pub-image-container {
    width: 100%;
  }
}
</style>
