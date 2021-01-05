<template>
  <v-app>
    <Navbar />
    <v-main class="mx-4 mb-4">
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>
import Navbar from "@/components/Navbar";

export default {
  name: 'App',
  components: {Navbar},
  comments: {
    Navbar
  },
  data: () => ({
    //
  }),
};
</script>
