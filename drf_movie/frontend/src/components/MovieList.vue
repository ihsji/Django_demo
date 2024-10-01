<template>
    <div class="flex items-center justify-center">
      <div class="w-full px-2" style="max-width:1440px;">
          <div id="movie-list" class="p-2 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
            <div class="movie" v-for="movie in info.results" :key="movie.id">
                <a href="/detail/443">
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
                let url = '/api/movie'
                const page = Number(this.$route.query.page)
                if(!isNaN(page)&&(page!==0)){
                    url =url+'/?page='+page;
                }
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