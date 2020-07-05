<template>
  <div id="wrap">
    <div id="top_content">
      <div id="header">
        <div id="rightheader">
          <p>
            {{time}}
            <br/>
            <a href="javascript:void(0);" @click="logout">安全退出</a>
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
          欢迎{{username}}使用百知员工管理系统
        </h1>
        <table class="table">
          <tr class="table_header">
            <td>ID</td>
            <td>Name</td>
            <td>Photo</td>
            <td>Salary</td>
            <td>Age</td>
            <td>Operation</td>
          </tr>
          <tr v-for="(emp, index) in emp_list" :key="emp.id" :class="index%2?'row2':'row1'">
            <td>{{emp.id}}</td>
            <td>{{emp.emp_name}}</td>
            <td><img :src="emp.img_url" style="height: 60px;"></td>
            <!--<td><img :src="`${emp.img_url}`" style="height: 60px;"></td>-->
            <td>{{emp.salary}}</td>
            <td>{{emp.age}}</td>
            <td>
              <router-link :to="`/ems/update_emp/${emp.id}/`">修改员工</router-link>
              <a href="javascript:void(0);" @click="delete_emp(emp.id, emp.emp_name)">删除员工</a>
            </td>
          </tr>
        </table>
        <p>
          <router-link to="/ems/add_emp">
            <el-button>添加员工</el-button>
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
    name: "EmpList",
    props: ['time'],
    data() {
      return {
        username: sessionStorage.getItem('username'),
        emp_list: [],
      }
    },
    methods: {
      logout() {
        sessionStorage.removeItem('username');
        this.$message({type: 'success', message: '已退出!', showClose: true});
        this.$router.push('login/');
      },
      get_emp_list() {
        this.$axios.get('http://127.0.0.1:8000/api/emp/').then(res => {
          this.emp_list = res.data;
        }).catch(error => {
          console.log(error);
        });
      },
      delete_emp(id, name) {
        this.$confirm(`此操作将永久删除员工${name}, 是否继续?`, '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$axios({
            'method': 'delete',
            'url': `http://127.0.0.1:8000/api/emp/${id}/`,
          }).then(res => {
            if (res.status === 204) {
              this.$message({type: 'success', message: '删除成功!', showClose: true});
              this.get_emp_list();
            }
          }).catch(error => {
            this.$message({type: 'error', message: '删除失败：' + error.response.data.detail, showClose: true});
            this.get_emp_list();
          });
        }).catch(() => {
          this.$message({type: 'info', message: '已取消删除', showClose: true});
        });
      }
    },
    created() {
      this.get_emp_list();
    }
  }
</script>

<style scoped>

</style>
