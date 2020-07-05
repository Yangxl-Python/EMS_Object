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
            <a href="#">Main</a>
          </h1>
        </div>
        <div id="navigation">
        </div>
      </div>
      <div id="content">
        <p id="whereami">
        </p>
        <h1>
          update Emp info:
        </h1>
        <table cellpadding="0" cellspacing="0" border="0"
               class="form_table">
          <tr>
            <td valign="middle" align="right">
              id:
            </td>
            <td valign="middle" align="left">
              {{emp_id}}
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              name:
            </td>
            <td valign="middle" align="left">
              <input type="text" class="inputgri" name="name" v-model="emp_name"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              photo:
            </td>
            <td valign="middle" align="left">
              <input type="file" name="photo" ref="photo"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              salary:
            </td>
            <td valign="middle" align="left">
              <input type="text" class="inputgri" name="salary" v-model="salary"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              age:
            </td>
            <td valign="middle" align="left">
              <input type="text" class="inputgri" name="age" v-model="age"/>
            </td>
          </tr>
        </table>
        <p>
          <el-button @click="update_emp">提交</el-button>
          &nbsp;&nbsp;
          <router-link to="/ems">
            <el-button>返回</el-button>
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
    name: "UpdateEmp",
    props: ['time'],
    data() {
      return {
        emp_id: this.$route.params.id,
        emp_name: '',
        age: '',
        salary: ''
      }
    },
    methods: {
      get_emp() {
        this.$axios.get(`http://127.0.0.1:8000/api/emp/${this.emp_id}/`).then(res => {
          this.emp_name = res.data.emp_name;
          this.age = res.data.age;
          this.salary = res.data.salary;
        }).catch(error => {
          console.log(error);
        });
      },
      error_alert(msg) {
        setTimeout(() => {
          this.$message({message: msg, type: 'error', showClose: true});
        }, 0);
      },
      update_emp() {
        let formData = new FormData();
        let img_file = this.$refs.photo.files[0];
        formData.append("emp_name", this.emp_name);
        if (img_file) {
          formData.append("img", img_file);
        }
        formData.append("salary", this.salary);
        formData.append("age", this.age);
        this.$axios({
          url: `http://127.0.0.1:8000/api/emp/${this.emp_id}/`,
          method: 'patch',
          data: formData,
          headers: {
            'content-type': 'multipart/form-data'
          },
        }).then(res => {
          if (res.data.message) {
            this.$message({message: '修改成功', type: 'success', showClose: true});
            this.$router.push('/ems');
          }
        }).catch(error => {
          let error_data = error.response.data;
          if (error_data.emp_name) {
            this.error_alert('员工姓名：' + error_data.emp_name);
          }
          if (error_data.age) {
            this.error_alert('年龄：' + error_data.age);
          }
          if (error_data.salary) {
            this.error_alert('工资：' + error_data.salary);
          }
        });
      }
    },
    created() {
      this.get_emp();
    }
  }
</script>

<style scoped>

</style>
