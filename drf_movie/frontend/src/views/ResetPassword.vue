<template>
  <div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4">
    <Header />
    <div class="text-center text-2xl p-8">重置密码</div>
    <div class="flex items-center justify-center">
      <div class="w-1/4 p-4 bg-gray-100 rounded-lg shadow-lg">
        <div class="text-black text-center p-4">
          <p class="font-bold py-4">请输入注册时的邮箱</p>
          <div>
            <input
              v-model="email"
              class="outline-0 h-9 rounded border border-green-600 placeholder-gray-400 w-64 px-2 py-1 max-w-[280px]"
              type="text"
            />
          </div>
        </div>
        <div class="flex justify-center">
          <button
            v-on:click="resetPassword"
            class="bg-green-500 text-white px-4 py-2 rounded"
          >
            发送邮件
          </button>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import axios from "axios";
import showMessage from "@/utils/message.js";

export default{
    name:"ResetPassword",
    data:function(){
        return{
            emali : "",
        };
    },
    components:{Header, Footer},

    methods:{
        resetPassword(){
            const email = this.email.trim();
            axios
                .post('/api/users/reset_password/',{email:email})
                .then((response) => {
                    showMessage('邮箱已发送，请确认',"info",()=>{
                        this.$router.push({
                            name:"Login"
                        });
                    });
                })
                .catch((error) =>{
                    const errorData = error.response.data;
                    const errorMessage = Object.values(errorData).flat();
                    for (let i=0; i<errorMessage.length; i++ ){
                        let customMessage;
                        switch(errorMessage[i]){
                            case 'User with given email does not exist.':
                            customMessage="指定邮箱地址的用户不存在。"
                            break;

                            //设置默认提示错误
                            default:
                            customMessage=errorMessage[i]
                        }
                        showMessage(customMessage);
                    }
                });
        },
    },
};
</script>