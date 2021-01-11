<template>
  <div>
    <v-app-bar
        color="deep-purple accent-4"
        dense
        dark
    >
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>LQ Highlights</v-toolbar-title>

    </v-app-bar>

    <v-navigation-drawer
        v-model="drawer"
        temporary
        app
    >

      <v-list-item>
        <v-list-item-avatar>
          <v-icon
              large
          >
            mdi-cricket
          </v-icon>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>LQ Highlights v1.0</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
          nav
          dense
      >
        <v-list-item-group
            v-model="group"
            active-class="deep-purple--text text--accent-4"
        >
          <v-list-item router to="/">
            <v-list-item-icon>
              <v-icon>mdi-view-dashboard</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>Dashboard</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item router to="/raw">
            <v-list-item-icon>
              <v-icon>mdi-filmstrip</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>Raw Footage</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-content-cut</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>Edited Clips</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-download</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>Download Center</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

        </v-list-item-group>
      </v-list>

    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data(){
    return {
      drawer: false,
      group: null,
    }
  },
  watch: {
    group () {
      this.drawer = false
    },
  },
}
</script>