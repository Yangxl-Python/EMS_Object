<template>
  <router-view :time="time"/>
</template>

<script>
  export default {
    name: "Ems",
    props: ['time'],
    methods: {
      check_status() {
        let user = sessionStorage.getItem('username');
        if (!user) {
          this.$router.push('/login');
        }
      },
    },
    created() {
      this.check_status();
    }
  }
</script>

<style scoped>

</style>
