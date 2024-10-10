<template>
    <div class="flex items-center justify-center">
      <div class="w-full px-2" style="max-width:1440px;">
          <div id="movie-list" class="p-2 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
            <div class="movie" v-for="movie in info.results" :key="movie.id">
                <a :href="'/movie/'+movie.id">
                    <div class="relative">
                        <div style="min-height:259px;max-height:300px;height:274px">
                        <img :src="movie.image_url" alt="" class="rounded h-full w-full" referrerPolicy="no-referrer">                 
                        </div>
                        <div v-if="movie.is_top" class="rounded absolute top-0 bg-purple-600 px-1 text-sm">置顶</div>
                        <div v-if="movie.quality==1" class="rounded absolute bottom-0 right-0 bg-blue-500 px-1 text-sm">720p</div>
                        <div v-else-if="movie.quality==2" class="rounded absolute bottom-0 right-0 bg-blue-500 px-1 text-sm">1080p</div>
                        <div v-else-if="movie.quality==3" class="rounded absolute bottom-0 right-0 bg-blue-500 px-1 text-sm">4K</div>
                    </div>
                    <p>{{movie.movie_name}} ({{movie.release_year}})
                    </p><p class="text-sm text-primary-200">{{movie.language}}</p>
                </a>
            </div>
          </div>  
      </div>
    </div>

    <Page :info="info"/>

</template>

<script>
import axios from 'axios'
import Page from '@/components/Page.vue'

export default{
    name:"MovileList",
    data:function(){
        return {
            info:''
        }
    },
    components:{ Page },
    mounted(){
        //axios发送请求
        this.get_movie_data();
    
    },

    methods:{
        get_movie_data:function() {
            let url = "/api/movie"; // /api/movie/?page=3&movie_name=我
            const page = Number(this.$route.query.page); // 获取page参数值
            const search = this.$route.query.search;// 获取search参数
            const category_id = this.$route.query.category_id;// 获取category_id参数
            const region = this.$route.query.region; // 获取region参数
            const params = new URLSearchParams();
            
            if (page){
                params.append('page',page);
            }
            if(search){
                params.append("movie_name",search);
            }
            if(region){
                params.append("region ",region );
            }   if(category_id){
                params.append("category_id",category_id);
            }

            // if(!isNaN(page)&&(page!==0)){
            //     url =url+'/?page='+page;
            // }
            // console.log(params)
            url = url +"?"+params.toString();
        
            axios.get(url)
                .then(Response => (this.info = Response.data))
                .catch(error => {
                    console.log(error)
        })
        },  
    },
    watch:{
        //监听路由的变化
        $route(){
            this.get_movie_data();
        },
    },
};
</script>