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
          注册
        </h1>
        <table cellpadding="0" cellspacing="0" border="0"
               class="form_table">
          <tr>
            <td valign="middle" align="right">
              用户名:
            </td>
            <td valign="middle" align="left">
              <input type="text" class="inputgri" name="username" v-model="username"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              真实姓名:
            </td>
            <td valign="middle" align="left">
              <input type="text" class="inputgri" name="name" v-model="real_name"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              密码:
            </td>
            <td valign="middle" align="left">
              <input type="password" class="inputgri" name="pwd" v-model="password"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              确认密码:
            </td>
            <td valign="middle" align="left">
              <input type="password" class="inputgri" name="pwd" v-model="confirm_pwd"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              性别:
            </td>
            <td valign="middle" align="left">
              男
              <input type="radio" class="inputgri" name="sex" value="m" @click="gender=0" checked="checked"/>
              女
              <input type="radio" class="inputgri" name="sex" value="f" @click="gender=1"/>
            </td>
          </tr>

        </table>
        <p>
          <el-button @click="register">注册</el-button>
          &nbsp;&nbsp;
          <router-link to="/login">
            <el-button>返回登录</el-button>
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
    name: "Register",
    data() {
      return {
        username: '',
        real_name: '',
        password: '',
        confirm_pwd: '',
        gender: 0
      }
    },
    methods: {
      error_alert(msg) {
        setTimeout(() => {
          this.$message({message: msg, type: 'error', showClose: true});
        }, 0);
      },
      register() {
        if (this.password === this.confirm_pwd) {
          this.$axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/api/register/',
            data: {
              username: this.username,
              real_name: this.real_name,
              password: this.password,
              gender: this.gender
            }
          }).then(res => {
            if (res.status === 201) {
              this.$message({message: '注册成功', type: 'success', showClose: true});
              this.$router.push('/login');
            }
          }).catch(error => {
            let error_data = error.response.data;
            if (error_data.username) {
              this.error_alert('用户名：' + error_data.username);
            }
            if (error_data.real_name) {
              this.error_alert('真实姓名：' + error_data.real_name);
            }
            if (error_data.password) {
              this.error_alert('密码：' + error_data.password);
            }
          });
        } else {
          this.$message({message: '两次输入密码不一致', type: 'warning', showClose: true});
        }
      }
    },
    props: ['time']
  }
</script>

<style scoped>

</style>
