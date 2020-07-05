<template>
  <div id="app">
    <router-view :time="time"/>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        time: '',
      }
    },
    methods: {
      get_time() {
        this.$axios.get('http://127.0.0.1:8000/api/get_time/').then(res => {
          this.time = res.data.time;
        }).catch(error => {
          console.log(error);
        });
      }
    },
    created() {
      this.get_time();
    }
  }
</script>

<style>

</style>
