import Vue from 'vue';
import Router from 'vue-router';
import Login from "../components/Login";
import Register from "../components/Register";
import Ems from "../components/Ems";
import EmpList from "../components/ems_compnents/EmpList";
import AddEmp from "../components/ems_compnents/AddEmp";
import UpdateEmp from "../components/ems_compnents/UpdateEmp";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/register',
      component: Register
    },
    {
      path: '/ems',
      component: Ems,
      children: [
        {
          path: '',
          component: EmpList
        },
        {
          path: 'emp_list',
          component: EmpList
        },
        {
          path: 'add_emp',
          component: AddEmp
        },
        {
          path: 'update_emp/:id',
          component: UpdateEmp
        },
      ]
    },
    {
      path: '/*',
      redirect: '/'
    }
  ]
});
