<template>
  <BaseLayout>
    <Navbar/>
      <router-view/>
    <Footer/>
  </BaseLayout>
</template>

<script setup>
import Navbar from './components/Navbar.vue'
import BaseLayout from './components/BaseLayout.vue'
import Footer from './components/Footer.vue'
</script>

<style>
</style>
