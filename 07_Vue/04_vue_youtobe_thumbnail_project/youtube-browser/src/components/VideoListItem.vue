<template>
  <li @click="onVideoSelect" class="list-group-item">

    <!-- VideoListItem -->
    <!-- <img :src="video.snippet.thumbnails.default.url" alt="youtube-thumbail-image"> -->
    <img :src="thumbnailUrl" class="mr-3" alt="youtube-thumbail-image">
    <div class="media-body">
      {{ video.snippet.title }}
    
    </div>

  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props : {
    video: {
      type: Object,
      required: true,
    }
  },

  computed: {
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url
    }
  },
  methods: {
    onVideoSelect() {
      this.$emit('videoSelect', this.video)
    }
  }

}
</script>

<style scoped>
  li {
    display : flex;
    cursor: pointer;
  }
  li:hover {
    background-color: #eeeeee
  }

</style>