<template>
  <div id="wrap">
    <div id="top_content">
      <div id="header">
        <div id="rightheader">
          <p>
            {{time}}
            <br/>
          </p>
        </div>
        <div id="topheader">
          <h1 id="title">
            <a href="#">main</a>
          </h1>
        </div>
        <div id="navigation">
        </div>
      </div>
      <div id="content">
        <p id="whereami">
        </p>
        <h1>
          login
        </h1>
        <table cellpadding="0" cellspacing="0" border="0"
               class="form_table">
          <tr>
            <td valign="middle" align="right">
              username:
            </td>
            <td valign="middle" align="left">
              <input type="text" class="inputgri" name="name" v-model="username"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              password:
            </td>
            <td valign="middle" align="left">
              <input type="password" class="inputgri" name="pwd" v-model="password"/>
            </td>
          </tr>
        </table>
        <p>
          <el-button @click="login">登录</el-button>
          &nbsp;&nbsp;
          <router-link to="/register">
            <el-button>注册</el-button>
          </router-link>
        </p>
      </div>
    </div>
    <div id="footer">
      <div id="footer_bg">
        ABC@126.com
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "login",
    data() {
      return {
        username: '',
        password: '',
      }
    },
    props: ['time'],
    methods: {
      login() {
        this.$axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/api/login/',
          data: {
            username: this.username,
            password: this.password
          }
        }).then(res => {
          if (res.data.message) {  // res.data.message -> true or false
            sessionStorage['username'] = this.username;
            this.$message({message: '登录成功', type: 'success', showClose: true});
            this.$router.push('/ems');
          } else {
            this.$message({message: '用户名或密码错误', type: 'error', showClose: true});
          }
        }).catch(error => {
          console.log(error);
        });
      },
      check_status() {
        let user = sessionStorage.getItem('username');
        if (user) {
          this.$router.push('/ems');
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
