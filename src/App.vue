<template>
  <div class="app">
    <Header />
    <main class="main-content">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import Header from './components/AppHeader.vue'

export default {
  name: 'App',
  components: {
    Header
  }
}
</script>

<style>
:root {
  --background-color: #1a1a1a;
  --text-color: #ffffff;
  --link-color: #4a9eff;
}

body {
  margin: 0;
  padding: 0;
  background-color: var(--background-color);
  color: var(--text-color);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}
</style>
