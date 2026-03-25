<template>
  <div class="publications">
    <h2>Publications</h2>
    <div class="publication-list">
      <div 
        v-for="pub in publications" 
        :key="pub.title" 
        class="publication-item"
      >
        <div class="pub-image-container">
          <!-- YouTube 视频 -->
          <iframe 
            v-if="pub.mediaType === 'youtube'" 
            :src="pub.media" 
            frameborder="0" 
            allow="autoplay; encrypted-media" 
            allowfullscreen
            class="pub-image">
          </iframe>

          <!-- 本地 MP4 视频 -->
          <video 
            v-else-if="pub.mediaType === 'mp4'" 
            :src="pub.media" 
            autoplay muted loop playsinline
            class="pub-image">
          </video>

          <!-- 图片 / GIF -->
          <img 
            v-else 
            :src="pub.media" 
            :alt="pub.title" 
            class="pub-image">
        </div>

        <div class="pub-info">
          <h3>{{ pub.title }}</h3>
          <p class="authors">
            <span v-if="pub.customAuthorText">
              <strong>{{ pub.customAuthorText.split(',')[0] }}</strong>{{ pub.customAuthorText.includes(',') ? ',' + pub.customAuthorText.split(',').slice(1).join(',') : '' }}
            </span>
            <template v-else v-for="(author, index) in pub.authorsList" :key="index">
              <strong v-if="author.isCoFirst">{{ author.name }}*</strong>
              <template v-else>{{ author.name }}</template>
              {{ index < pub.authorsList.length - 1 ? ', ' : '' }}
            </template>
          </p>
          <p class="note" v-if="!pub.customAuthorText && pub.authorsList?.some(a => a.isCoFirst)">
            * denotes co-first authors
          </p>
          <p class="venue">{{ pub.venue }}</p>
          <div class="pub-links">
            <a 
              v-for="link in pub.links"
              :key="link.type"
              :href="link.url"
              class="pub-link" 
              target="_blank" 
              rel="noopener noreferrer">
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
          title: "Lumine: Building Generalist Agents in 3D Open Worlds",
          customAuthorText: "Core contributor, at Bytedance Seed",
          venue: "Technical Report",
          media: require("../assets/genshin_main_demo_540p.mp4"),
          mediaType: "mp4",
          links: [
            { type: "pdf", url: "https://www.lumine-ai.org/Lumine.pdf", icon: "fas fa-file-pdf" },
            { type: "github", url: "https://www.lumine-ai.org/", icon: "fab fa-github" },
            { type: "video", url: "https://www.youtube.com/watch?v=VXiTRGX7uWo&t=1s", icon: "fab fa-youtube" }
          ]
        },
        {
          title: "SRBTrack: Terrain-Adaptive Tracking of a Single-Rigid-Body Character Using Momentum-Mapped Space-Time Optimization",
          authorsList: [
            { name: "Hanyang Cao", isCoFirst: true },
            { name: "Heyuan Yao", isCoFirst: true },
            { name: "Libin Liu", isCoFirst: false },
            { name: "Taesoo Kwon", isCoFirst: false },
          ],
          venue: "December 2025 In SIGGRAPH Asia",
          media: require("../assets/SRBTrack.jpg"),
          mediaType: "image",
          links: [
            { type: "pdf", url: "https://hanyang9.github.io/SRBTrack/static/paper/saconferencepapers25-15.pdf", icon: "fas fa-file-pdf" },
            { type: "github", url: "https://hanyang9.github.io/SRBTrack/", icon: "fab fa-github" },
            { type: "video", url: "https://www.youtube.com/watch?v=yf_V8TVO71s", icon: "fab fa-youtube" }
          ]
        },
        {
          title: "Social Agent: Mastering Dyadic Nonverbal Behavior Generation via Conversational LLM Agents",
          authorsList: [{name:"Zeyi Zhang"}, {name:"Yanju Zhou"}, {name:"Heyuan Yao"}, {name:"Tenglong Ao"}, {name:"Xiaohang Zhan"}, {name:"Libin Liu"}],
          venue: "December 2025 In SIGGRAPH Asia",
          media: require("../assets/socialAgent.jpg"),
          mediaType: "image",
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
          media: require("../assets/scaling.png"),
          mediaType: "image",
          links: [
            { type: "pdf", url: "https://arxiv.org/abs/2510.23691", icon: "fas fa-file-pdf" },
            { type: "github", url: "https://seed-tars.com/game-tars/", icon: "fab fa-github" }
          ]
        },
      {
          title: "MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations",
          authorsList: [
          {name:"Heyuan Yao"}, {name:"Zhenhua Song"}, {name:"Yuyang Zhou"}, {name:"Tenglong Ao"}, {name:"Baoquan Chen"}, {name:"Libin Liu"}],
          venue: "August 2024 In SIGGRAPH (Journal Track)",
          media: require("../assets/moconvq.gif"),
          mediaType: "image",
          links: [
            { type: "pdf", url: "https://arxiv.org/abs/2310.10198", icon: "fas fa-file-pdf" },
            { type: "github", url: "https://github.com/heyuanYao-pku/MoConVQ", icon: "fab fa-github" },
            { type: "video", url: "https://www.bilibili.com/video/BV13D421N7zp/", icon: "fab fa-youtube" }
          ]
        },
        {
          title: "ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters",
          authorsList: [
            {name: "Heyuan Yao"}, {name: "Zhenhua Song"}, {name: "Baoquan Chen"}, {name: "Libin Liu"}],
          venue: "December 2022 In SIGGRAPH Asia (Journal Track), selected to Trailer",
          media: require("../assets/skill.gif"),
          mediaType: "image",
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

.pub-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 4px;
}

/* 保证 iframe 不会拉伸 */
.pub-image iframe {
  width: 100%;
  height: 100%;
  border: none;
}

</style>
