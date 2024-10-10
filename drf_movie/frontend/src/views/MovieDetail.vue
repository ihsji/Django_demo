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
         <button v-on:click="collect_or_cancle(movie.id)" 
         id="collect" :class="collectStatus ? 'bg-gray-500': 'bg-blue-500'" 
         class="copy text-white w-full px-4 py-1 mt-2 text-sm rounded border">
            {{collectMessage}}
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
import showMessage from '@/utils/message';

export default{
    name:'MovieDtail',
    data: function(){
        return{
            movie:{},
            collectStatus: false,
            collectMessage: "",
        };
    },
    components:{Header,Footer},
    mounted(){
        this.get_movie_info();
    // 判断一下用户是否登录
        if (!this.$store.state.isLogin) {
            this.collectStatus = false;
            this.collectMessage = "添加收藏";
        } else {
            const movie_id = this.$route.params.id;
            this.get_collect_status(movie_id);
        }
     },
    methods:{
        get_movie_info:function(){
            axios
            .get('/api/movie/'+this.$route.params.id)
            .then((response) =>(this.movie = response.data));
        },
        //获取收藏状态
        get_collect_status(movie_id) {
            axios
                .get("/api/collects/" + movie_id + "/is_collected/", )
                .then((response) => {
                this.collectStatus = response.data.is_collected;
                if (this.collectStatus) {
                    this.collectMessage = "取消收藏";
                } else {
                    this.collectMessage = "添加收藏";
                }
            });
        },
         // 收藏或取消收藏
        collect_or_cancle(movie_id){
            if(!this.$store.state.isLogin) {
                showMessage('请先登录','error', ()=> {
                    this.$router.push({
                        name: 'Login'
                    })
                    })
                return 
            }
            if (this.collectStatus) {
                this.cancle_collect_movie(movie_id);
            } else {
                this.collect_movie(movie_id);
            }
            
        },
        //收藏电影
        collect_movie(movie_id){
            const options={
                url:"/api/collects/",
                data:{ movie_id:movie_id },
                config:{
                    headers:{
                        Authorization: "JWT " + localStorage.getItem("token"),
                    }
                },
            };
            axios
                .post(options.url,options.data,options.config)
                .then((response) => {
                    const status_code = response.data.status_code;
                    const message = response.data.message;
                    if (status_code === 0) {
                        this.collectStatus = true;
                        this.collectMessage = "取消收藏";
                        showMessage(message, "info");
                    } else {
                        showMessage(message, "error");
                    }
                })
                .catch((error) => {
                    showMessage("收藏失败");
                });
            // window.location.reload();
                
        },
           // 取消收藏
        cancle_collect_movie(movie_id) {
            axios
                .delete("/api/collects/" + movie_id + "/",
              )
                .then((response) => {
                    const status_code = response.data.status_code;
                    const message = response.data.message;
                if (status_code === 0) {
                    this.collectStatus = false;
                    this.collectMessage = "添加收藏";
                    showMessage(message, "info");
                } else {
                    showMessage(message);
                }
                })
                .catch((error) => {
                    showMessage("取消收藏失败");
                });
            // window.location.reload();
            },
        },
};
</script>