<template>
    <v-data-table
        :headers="headers"
        :items="footage"
        class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar
            flat
        >
          <v-toolbar-title>Raw Footage</v-toolbar-title>
          <v-divider
              class="mx-4"
              inset
              vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog
              v-model="dialog"
              max-width="500px"
          >
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                        cols="12"
                        sm="6"
                        md="4"
                    >
                      <v-text-field
                          v-model="editedItem.name"
                          label="Dessert name"
                      ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        sm="6"
                        md="4"
                    >
                      <v-text-field
                          v-model="editedItem.calories"
                          label="Calories"
                      ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        sm="6"
                        md="4"
                    >
                      <v-text-field
                          v-model="editedItem.fat"
                          label="Fat (g)"
                      ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        sm="6"
                        md="4"
                    >
                      <v-text-field
                          v-model="editedItem.carbs"
                          label="Carbs (g)"
                      ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        sm="6"
                        md="4"
                    >
                      <v-text-field
                          v-model="editedItem.protein"
                          label="Protein (g)"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="blue darken-1"
                    text
                    @click="close"
                >
                  Cancel
                </v-btn>
                <v-btn
                    color="blue darken-1"
                    text
                    @click="save"
                >
                  Save
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="headline">Are you sure you want to delete this item?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogPlay" max-width="1000px" :key="editedRow.key">
            <v-card>
              <vue-plyr>
                <video
                    controls
                    crossorigin
                    playsinline
                >
                  <source
                      size="1080"
                      :src="editedRow.url"
                      type="video/mp4"
                  />
                </video>
              </vue-plyr>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon
            medium
            class="mr-2"
            @click="playItem(item)"
        >
          mdi-play
        </v-icon>
        <v-icon
            small
            class="mr-2"
            @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
            small
            @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn
            color="primary"
            @click="initialize"
        >
          Reset
        </v-btn>
      </template>
    </v-data-table>
</template>

<script>
import axios from "axios";

export default {
  name: "RawFootage",
  data: () => ({
    dialog: false,
    dialogPlay: false,
    dialogDelete: false,
    headers: [
      {
        text: 'Footage',
        align: 'start',
        sortable: false,
        value: 'key',
      },
      { text: 'Actions', value: 'actions', sortable: false },
    ],
    footage: [],
    editedIndex: -1,
    editedRow: {
      key: '',
      url: ''
    },
    editedItem: {
      key: '',
      url: ''
    },
    defaultItem: {
      key: '',
      url: ''
    },
  }),

  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    },
  },

  watch: {
    dialog (val) {
      val || this.close()
    },
    dialogDelete (val) {
      val || this.closeDelete()
    },
    dialogPlay (val) {
      val || this.closePlay()
    }
  },

  created () {
    this.initialize()
  },

  methods: {
    initialize () {
      axios({
        method: "get",
        url: "http://127.0.0.1:5000/api/v1/raw/all"
      })
          .then(response => (this.footage = response.data.footage))
    },

    editItem (item) {
      this.editedIndex = this.footage.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      this.editedRow = item
      this.editedIndex = this.footage.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    playItem (item) {
      console.log("Play Item", item)
      this.editedRow = item
      this.editedIndex = this.footage.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogPlay = true
    },

    deleteItemConfirm () {
      axios({
        method: "delete",
        url: `http://127.0.0.1:5000/api/v1/raw/${this.editedRow.key}`
      })
      .then(() => (
          this.footage.splice(this.editedIndex, 1)
      ))
      this.closeDelete()
    },

    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedRow = Object.assign({}, this.defaultItem)
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    closePlay () {
      console.log("Before Close", this.editedRow)
      this.dialogPlay = false
      this.$nextTick(() => {
        this.editedRow = Object.assign({}, this.defaultItem)
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
        console.log("After Close", this.editedRow)
      })
    },

    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.footage[this.editedIndex], this.editedItem)
      } else {
        this.footage.push(this.editedItem)
      }
      this.close()
    },
  },
}
</script>

<style scoped>

</style>