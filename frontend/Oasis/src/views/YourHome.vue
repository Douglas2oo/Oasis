<template>
  <div class="common-layout">


    <el-container>


      <el-header class="head">
        <h1>Your Home</h1>
      </el-header>
      <el-main>
        <div>

          <PersonalData />
        </div>
        <h2>Your Articles</h2>
        <ArticleList />
        <!-- Fixed bar at the bottom -->
        <FixedBar />
      </el-main>



    </el-container>

  </div>
</template>
    
<script setup lang="ts">
import PersonalData from '../components/UserData.vue'
import ArticleList from '../components/ArticleList.vue'
import FixedBar from '../components/FixedBar.vue'


</script>
  
<style scoped>
.head {
  margin-top: -20px;
}


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

.common-layout {
  margin-bottom: 50px;
}
</style>
    