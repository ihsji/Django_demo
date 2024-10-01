<template>
    <div id="header" class="h-12 py-1 bg-primary-100 flex items-center justify-center">
      <div class="w-full px-4" style="max-width:1440px;">
        <div class="flex justify-between">
          <div class="flex items-center">
            <a href="/">
              <img  src="../assets/images/logo.png" style="height:39px" >
            </a>
            <div id="nav" class="px-4">
              <ul class="hidden md:flex items-center space-x-4 ml-2">
                <li>
                    <a href="/">首页</a>
                </li>
                <li>热门</li>
                <li>电影</li>
                <li>电视剧</li>
                <li>综艺</li>
                <li>动漫</li>
                <li>纪录片</li>
                <li>短片</li>
              </ul>
            </div>
          </div>
          <div class="flex items-center space-x-2">
            <!-- 搜索 -->
            <div class="relative shrink">
                <form>
                    <input type="text" name="keyword" class="outline-0 h-9 rounded bg-primary-700 border border-gray-600 placeholder-gray-400 w-64 px-2 py-1 max-w-[180px]" placeholder="请输入关键词" value="">
                    <div class="absolute top-0 right-0 flex items-center h-full">
                        <div class="rounded text-xs text-gray-400 px-2 mr-2">
                            <button>
                                <svg xmlns="http://www.w3.org/20 00/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                                </svg>
                            </button>
                        </div>
                    </div>
                </form>
            </div>
            <!-- 登录和注册 -->
            <div class="text-white flex-shrink-0 pr-2">
                <a href="#">登录</a>
                / <a href="#">注册</a>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    name: 'Header',
}
</script>
