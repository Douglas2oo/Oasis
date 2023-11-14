<template>
    <div class="common-layout">

        <Na />

        <el-main>
            <router-view />
        </el-main>



    </div>
</template>
    
<script setup lang="ts">
import { reactive, toRefs, watch, onMounted, ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router';


import { UserFilled } from '@element-plus/icons-vue'
const alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


const articlelist = ref([])

const router = useRouter();
const Userdata = reactive({
    id: router.currentRoute.value.query.id,
    name: router.currentRoute.value.query.name,
    account: router.currentRoute.value.query.account,
    email: router.currentRoute.value.query.email,
    birthday: router.currentRoute.value.query.birthday,
})

watch(router.currentRoute, (to, from) => {
    Userdata.id = to.query.id
    Userdata.name = to.query.name
    Userdata.account = to.query.account
    Userdata.email = to.query.email
    Userdata.birthday = to.query.birthday
})


const GetArticle = async () => {
    try {
        console.log("user data is " + Userdata)
        const id = Userdata.id//拿到user_id
        console.log("id is " + id)
        const response = await axios.get(`http://localhost:8000/articlelist/user_id/${id}`)
        if (response.status == 200) {
            console.log("get article success")
            console.log(response.data)

            // 文章数据在里面,长这个样，只要content(3) [{…}, {…}, {…}]
            // 0
            // : 
            // {id: 2, author: '7b7b94ce-0638-46f7-aacd-318f4e2418ac', content: 'sdfgdff43853475834753fd', create_time: '2023-11-02T09:57:04.022852Z', likes: Array(0)}
            // 1
            // : 
            // {id: 3, author: '7b7b94ce-0638-46f7-aacd-318f4e2418ac', content: 'sf发货及时反馈和按附件啊', create_time: '2023-11-12T13:03:17.185224Z', likes: Array(0)}
            // 2
            // : 
            // {id: 4, author: '7b7b94ce-0638-46f7-aacd-318f4e2418ac', content: 'sf发货及时反馈哈克警方哈哈发和按附件啊', create_time: '2023-11-12T13:03:22.973755Z', likes: Array(0)}


        }
    } catch (error) {
        console.log(error)
        console.log("get article failed")
    }

}

onMounted(() => {
    GetArticle()

})








import Na from '../components/NavigatorBlock.vue'


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
</style>
    
