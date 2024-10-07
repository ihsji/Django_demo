<template>
    <!-- 这是头部信息 -->
    <Header/>
    <!-- 这是头部信息结束 -->
    <div class="flex items-center justify-center">
     <div class="w-full px-2" style="max-width:1440px">
      <div id="main" class="bg-primary-300 p-6 text-black">
       <div class="flex rounded bg-white mx-4 py-6">
        <div class="mx-6">
         <div style="min-height:259px;max-height:300px;height:274px">
            <img :src="movie.image_url" class="h-full w-full" referrerpolicy="no-referrer">
         </div>
         <button id="collect" class="bg-blue-500 copy text-white w-full px-4 py-1 mt-2 text-sm rounded border">
            添加收藏
        </button>
        </div>
        <div id="info" data-movie-id="443">
         <ul>
        <li class="text-lg font-semibold">
                {{ movie.movie_name }} ({{ movie.release_year }})
        </li>
        <li>导演: {{ movie.director }}</li>
        <li>编剧: {{ movie.scriptwriter }}</li>
        <li>主演: {{ movie.actors }}</li>
        <li>语言: {{ movie.language }}</li>

        <li>首播: {{ movie.release_date }}</li>
        <li>集数: {{ movie.duration }}</li>

        <li>类型: {{ movie.types }}</li>
        <li> 制片国家/地区: 
            <span v-if="movie.region === 1">中国大陆</span>
            <span v-else-if="movie.region === 2">中国香港</span>
            <span v-else-if="movie.region === 3">中国台湾</span>
            <span v-else-if="movie.region === 4">美国</span>
            <span v-else-if="movie.region === 5">韩国</span>
            <span v-else-if="movie.region === 6">日本</span>
            <span v-else>其他</span>
        </li>
   
        <li>又名: {{movie.alternate_name}}</li>
        <li>豆瓣评分: {{ movie.rate }}</li>
         </ul>
        </div>
       </div>
       <div class="rounded bg-white mx-4 my-4 py-6">
        <div class="px-6">
         <h1 class="text-lg mb-6 font-semibold">简介</h1>
         <p>{{ movie.review }}</p>
        </div>
       </div>
       <div id="download_info" class="rounded bg-white mx-4 mt-4 py-6">
        <h1 class="text-lg mb-6 font-semibold px-6">网盘地址</h1>
        <div class="px-6">
         <div>
          百度网盘:http://www.baidu.com 提取码:8888 阿里云盘: http://www.aliyunpan.com 提取码:99999
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
    <footer class="fixed bottom-0 w-full flex justify-center items-center bg-primary-100 py-4">
     <p class="text-gray-500">&copy; 2023 大熊课堂 All rights reserved.</p>
    </footer>

    <!-- 这是尾部信息 -->
    <Footer/>
     <!-- 这是尾部信息结束 -->
</template>

<script>
import Footer from '@/components/Footer.vue'
import Header from '@/components/Header.vue'
import axios from 'axios';

export default{
    name:'MovieDtail',
    data: function(){
        return{
            movie:{},
        };
    },
    components:{Header,Footer},
    mounted(){
        this.get_movie_info();
    },
    methods:{
        get_movie_info:function(){
            axios
            .get('/api/movie/'+this.$route.params.id)
            .then((response) =>(this.movie = response.data));
        },
    },
};
</script>