<template>
  <div class="introduction">
    <div class="profile">
      <img src="../assets/myprofile.jpg" alt="Heyuan Yao" class="profile-image">
      <div class="profile-info">
        <h1>Heyuan Yao 姚贺源</h1>
        <p class="bio">
          I am currently a fourth-year Ph.D. student in the School of Computer Science at Peking University, under the supervision of Assistant Professor Libin Liu. I received my bachelor's degree from Peking University in 2021.
        </p> <p class="bio">  
          My research interests focus on developing human-like agents for both simulated and real-world environments. My previous work has centered on physics-based character animation, and currently I am exploring vision-language-action (VLA) models.
        </p>
        <div class="contact-links">
          <a href="mailto:heyuanyao@pku.edu.cn" class="link">
            <i class="fas fa-envelope"></i> heyuanyao@pku.edu.cn
          </a>
          <!-- <a href="#" class="link">
            <i class="fas fa-file"></i> Resume
          </a> -->
          <!-- <a href="#" class="link">
            <i class="fas fa-blog"></i> Blog
          </a> -->
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.introduction {
  margin-top: 2rem;
}

.profile {
  display: flex;
  gap: 2rem;
  align-items: flex-start;
}

.profile-image {
  width: 250px;
  border-radius: 8px;
}

.profile-info {
  flex: 1;
}

h1 {
  font-size: 3rem; /* 从2.5rem增加到3rem */
  margin: 0 0 1rem 0;
}

.bio {
  font-size: 1.3rem; /* 从1.1rem增加到1.3rem */
  line-height: 1.2; /* 适当增加行高 */
  margin-bottom: 1rem; /* 增加段落间距 */
}

.contact-links {
  margin-top: 1.5rem;
  display: flex;
  gap: 1.5rem;
}

.link {
  color: var(--link-color);
  text-decoration: none;
  font-size: 1.2rem; /* 增加链接文字大小 */
}

.link:hover {
  text-decoration: underline;
}
</style>