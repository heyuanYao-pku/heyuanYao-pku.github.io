<template>
  <header class="header">
    <div class="container">
      <div class="logo">
        <router-link to="/" class="logo-link">Heyuan Yao(姚贺源)</router-link>
      </div>
      <nav class="nav">
        <router-link to="/" class="nav-link">Home</router-link>
        <!-- <router-link to="/research" class="nav-link">Research</router-link>
        <router-link to="/publications" class="nav-link">Publications</router-link>
        <router-link to="/projects" class="nav-link">Projects</router-link>
        <router-link to="/contact" class="nav-link">Contact</router-link> -->
      </nav>
    </div>
  </header>
</template>

<style scoped>
.header {
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo a {
  font-size: 1.5rem;
  font-weight: 700;
  color: #2c3e50;
  text-decoration: none;
}

.nav {
  display: flex;
  gap: 1.5rem;
}

.nav-link {
  color: #2c3e50;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.nav-link:hover,
.router-link-active {
  color: #42b983;
}

@media (max-width: 768px) {
  .container {
    flex-direction: column;
    gap: 1rem;
  }
  
  .nav {
    flex-wrap: wrap;
    justify-content: center;
  }
}

.logo-link {
  font-size: 24px;  /* 可以调整大小 */
  font-weight: bold;
  /* 可以添加其他样式 */
  text-decoration: none;  /* 移除下划线 */
  color: #333;  /* 设置颜色 */
}
</style>

