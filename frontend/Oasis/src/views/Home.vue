<template>
    <div class="Title">
        <h1>Home</h1>
    </div>
    <div class="demo-type">
        <div>
            <el-avatar :icon="UserFilled" />
        </div>
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
import { reactive, toRefs, watch, onMounted,ref} from 'vue'
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


const GetArticle = async () =>{
    try {
        console.log("user data is " + Userdata)
        const id = Userdata.id//拿到user_id
        console.log("id is " + id)
        const response = await axios.get(`http://localhost:8000/articlelist/user_id/${id}`)
        if (response.status == 200){
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








</script>

<style scoped>
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
.demo-type > div {
  flex: 1;
  text-align: center;
}

.demo-type > div:not(:last-child) {
  border-right: 1px solid var(--el-border-color);
}
</style>