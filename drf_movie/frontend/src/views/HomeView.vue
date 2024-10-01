<template>
  <div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4"> 
    <!-- 头部部分 -->
    <Header/>
     <!-- 头部部分结束 -->

    <!-- 电影信息 -->
    <MovieList/>
     <!-- 电影结束 -->

    <!-- 尾巴部部分 -->
    <Footer/>
    <!-- 尾部部部分结束 -->

  </div>
</template>

<script>
// 添加代码
// 添加代码
import Footer from '@/components/Footer.vue'
import Header from '@/components/Header.vue'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'HomeView',
  components: {
    Header, Footer,MovieList
  }
}
</script>