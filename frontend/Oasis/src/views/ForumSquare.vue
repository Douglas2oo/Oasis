<template>
    <div class="Title">
        <h1>ForumSquare</h1>
    </div>
    <div class="demo-type">
    </div>
    <div class="block text-center">
        <span class="demonstration">The card Square</span>
        <el-carousel height="450px" indicator-position="outside">
            <el-carousel-item v-for="item in alist" :key="item">
                <!-- 幻灯片内容是在item 里面显示 -->
                <h3 class="small justify-center" text="2xl">{{ item }}</h3>
            </el-carousel-item>
        </el-carousel>
    </div>
</template>
    
<script setup lang="ts">

import { reactive, toRefs, watch, onMounted, ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router';

const alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] // 用来显示幻灯片的内容，通过列表，这是个样例，它的长度决定走马灯的页数，它的内容决定走马灯的内容



// 拿到所有文章的数据,进行整理并且加到列表里面
const articlelist = ref([])
const GetAllArticle = async () => {
    try {
        const response = await axios.get(`http://localhost:8000/articlelist/`)
        if (response.status == 200) {
            console.log("get article success")
            console.log(response.data)
            articlelist.value = response.data
        }
    } catch (error) {
        console.log(error)
    }
}



</script>
  
<style scoped>
#home {
    text-align: center;
    margin-top: 50px;
}

/* Basic styling */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

/* Center the main title */
h1 {
    text-align: center;
    color: #333;
    background-color: #f9f9f9;
    padding: 20px;
    margin-bottom: 20px;
}

/* 高度100% */
.el-container,
.common-layout,
#app,
body,
html {
    height: 100%;
}

.Title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    margin-bottom: 20px;
    margin-left: 25px;
}

.el-col {
    border-radius: 4px;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}


.demo-basic {
    text-align: center;
}

.demo-basic .demo-basic--circle,
.demo-basic .demo-basic--square {
    display: flex;
    align-items: center;

    margin-left: 190%;
}

.demo-basic .block:not(:last-child) {
    border-right: 1px solid var(--el-border-color);
}

.demo-basic .block {
    flex: 1;
}

.demo-basic .el-col:not(:last-child) {
    border-right: 1px solid var(--el-border-color);
}


.demonstration {
    color: var(--el-text-color-secondary);
    font-size: 20px;
    position: relative;
}

.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}


.demo-type {
    display: flex;
    margin-left: 95%;

}

.demo-type>div {
    flex: 1;
    text-align: center;
}

.demo-type>div:not(:last-child) {
    border-right: 1px solid var(--el-border-color);
}
</style>
    