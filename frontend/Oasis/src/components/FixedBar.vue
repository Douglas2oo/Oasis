<!-- components/FixedBar.vue -->
<template>
    <div class="fixed-bar">
        <textarea v-model="articleText" placeholder="Write your new article here..."></textarea>
        <button @click="publishArticle">Publish</button>
    </div>
</template>

<script setup>
import { ref,reactive } from 'vue'
import axios from 'axios'
import { useRouter } from "vue-router"

const router = useRouter();
const Userdata = reactive({
    id: router.currentRoute.value.query.id,
})
console.log("get id:", Userdata.id)

// 创建 ref 包装的文本框数据
const articleText = ref('');

// 获取北京时间
const getBeijingTime = () => {
    const beijingOffset = 0; // 北京的时区偏移为+8
    const currentUTC = new Date();
    const beijingTime = new Date(currentUTC.getTime() + (beijingOffset * 60 * 60 * 1000));
    return beijingTime;
};

// 格式化日期时间为 "YYYY-MM-DD HH:mm" 格式
const formatDateTime = (dateTime) => {
    const year = dateTime.getFullYear();
    const month = String(dateTime.getMonth() + 1).padStart(2, '0'); // 月份从0开始
    const day = String(dateTime.getDate()).padStart(2, '0');
    const hours = String(dateTime.getHours()).padStart(2, '0');
    const minutes = String(dateTime.getMinutes()).padStart(2, '0');

    return `${year}-${month}-${day} ${hours}:${minutes}`;
};

// 获取当前北京时间并格式化为 "YYYY-MM-DD HH:mm" 格式
const currentDate = getBeijingTime();
const formattedDate = formatDateTime(currentDate);



// 点击按钮时执行的函数
const publishArticle = async () => {

    // 构建请求数据
    let data = {
        content: articleText.value, // 使用文本框中的内容
        author: Userdata.id, // 使用当前用户的 ID

    };

    try {

        const response = await axios.post('http://127.0.0.1:8000//article/', data, { withCredentials: true })


        // 发送请求给后端
        // const response = await link(url.postarticle, 'post', data);
        console.log(response);
    } catch (error) {
        console.error(error);
        console.log('error');
    }

    window.location.reload()
};


</script>

<style scoped>
/* 这里可以添加针对 FixedBar 组件的样式 */
/* Fixed bar at the bottom for new article */
.fixed-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #4CAF50;
    padding: 0px;
    display: flex;
    justify-content: space-between;
    color: white;
    z-index: 3;
}

/* Larger textarea */
.fixed-bar textarea {
    width: 110%;
    height: 60px;
    border-radius: 8px;
    padding: 5px;
    resize: none;
    font-size: 18px;
}

/* Larger placeholder text */
.fixed-bar textarea::placeholder {
    font-size: 18px;
    color: #aaa;
}

/* Publish button styling */
.fixed-bar button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 26px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 8px;
}</style>
