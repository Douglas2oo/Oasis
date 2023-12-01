<template>
    <div class="common-layout" style="background: linear-gradient(to top, rgb(91, 194, 91),white);">

        <!-- Naviagation -->
        <Na />

        <el-main>
            <router-view />
        </el-main>

    </div>
</template>
    
<script setup lang="ts">
import { reactive, watch } from 'vue'
import { useRouter } from 'vue-router';
import Na from '../components/NavigatorBlock.vue'

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

.el-container,
.common-layout,
#app,
body,
html {
    height: 100%;
}
</style>
    
