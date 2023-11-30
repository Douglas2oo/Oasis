<template>
    <el-menu default-active="2" class="el-menu-demo" mode="horizontal" :ellipsis="false" @select="handleSelect"
        active-text-color="rgb(100, 199, 180)" text-decoration="none" @open="handleOpen" @close="handleClose" router>
        <img src="../assets/images/circlelogo.png" alt="LOGO" />
        <div class="flex-grow" />
        <el-menu-item :index="path1" class="custom-menu-item">
            <div class="demo-type">
                <div style="padding-bottom: 15px; ">
                    <div style="font-weight: bold;">
                        ForumSquare
                    </div>
                </div>
            </div>
        </el-menu-item>
        <el-menu-item :index="path2" class="custom-menu-item">
            <div class="demo-type">
                <div style="padding-bottom: 15px;">

                    <img v-if="avatar == 'http://127.0.0.1:8000/media/avatar/default.png'"
                        src="../assets/images/default.png" alt="User Avatar" />
                    <el-avatar v-else :src="avatar" alt="User Avatar" />
                </div>

            </div>
        </el-menu-item>
    </el-menu>
</template>
  
<script lang="ts" setup>
import { ref, reactive } from 'vue'
import { onMounted } from "vue"
import axios from 'axios'
import { useRouter } from "vue-router";

const router = useRouter();

//retrieve user data from router
const Userdata = reactive({
    id: router.currentRoute.value.query.id,
    name: router.currentRoute.value.query.name,
    account: router.currentRoute.value.query.account,
    email: router.currentRoute.value.query.email,
    birthday: router.currentRoute.value.query.birthday,
})

//router to ForumSquare
const path1 = '/ForumSquare?id=' + Userdata.id + '&name=' + Userdata.name + '&account=' + Userdata.name + '&email=' + Userdata.email + '&birthday=' + Userdata.birthday;

//router to home
const path2 = '/home?id=' + Userdata.id + '&name=' + Userdata.name + '&account=' + Userdata.name + '&email=' + Userdata.email + '&birthday=' + Userdata.birthday;


//button function
const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}

const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}

const handleSelect = (key: string, keyPath: string[]) => {

}

//initialize avatar
let avatar = ref('')

//get avatar from backend
const GetAvatar = async () => {
    try {
        const response = await axios.post('http://127.0.0.1:8000/avatar/', {
            user_id: Userdata.id
        });
        if (response.status == 200) {
            avatar.value = response.data.data.avatar
        }
    } catch (error) {
        console.log(error)
    }
}

onMounted(() => {
    GetAvatar();
})

</script>
  
  
<style>
.flex-grow {
    flex-grow: 1;
}

img {
    width: 60px;
}


.custom-menu-item a {
    text-decoration: none;
}

.demo-type {
    display: flex;
}

.demo-type>div {
    flex: 1;
    text-align: center;
}

.demo-type>div:not(:last-child) {
    border-right: 1px solid var(--el-border-color);
}

.el-menu-demo {
    height: 60px;
    padding-left: 10px;
    border-radius: 4px;
    margin-bottom: 20px;
}
</style>
