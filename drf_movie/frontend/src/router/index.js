import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieDetail from '@/views/MovieDetail.vue'
import Register from '@/views/Register.vue'
import ActivateEmail from "@/views/ActivateEmail.vue"
import Login from '@/views/Login.vue'
import ResetPassword from "@/views/ResetPassword.vue"
import PasswordReset from "@/views/PasswordReset.vue"
import store from '@/store'
import Personal from '../views/Personal.vue'
import ChangePassword from '../views/ChangePassword.vue'

const routes = [
  {//首页
    path: '/',
    name: 'home',
    component: HomeView
  },
  {//电影详情页
    path:'/movie/:id',
    name:'MovieDetail',
    component:MovieDetail
  },
  {//用户注册界面
    path:'/register',
    name:"Register",
    component:Register
  },
  {//用户邮箱激活界面
    path:'/activate/:uid/:token',
    name:"ActivateEmail",
    component:ActivateEmail
 },
  {//用户登录界面
    path:"/login",
    name:"Login",
    component:Login
  },
  {//用户重置密码界面
    path:'/reset_password',
    name:"ResetPassword",
    component:ResetPassword,
  },
  {//用户密码重置邮箱url:密码修改界面
    path: '/password_reset/:uid/:token',
    name: 'PasswordReset',
    component: PasswordReset
  },
  {//个人主页界面
    path: "/personal",
    name: "Personal",
    component: Personal,
    meta: {
      requireLogin: true
    }
  },
  {//个人主页-跳转--修改密码界面
    path: "/change_password",
    name: "ChangePassword",
    component: ChangePassword,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

//从本地存储中读取token
const token = localStorage.getItem('token')
//如果存在token，说明用户已经登陆，提交mutation设置登陆状态
if(token){
  store.commit('setLoginStatus',true)
}
//路由导航守卫
router.beforeEach((to, from ,next)=>{
  //如果访问的页面需要登陆，且未登录，跳转登录页
  if(to.matched.some(record => record.meta.requireLogin) &&!store.state.isLogin ){
    next({name:"Login",query:{jump:to.path}})
    //其他情况直接next
  }else{
    next()
  }

})

export default router
