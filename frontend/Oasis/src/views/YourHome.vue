<template>
  <div class="common-layout" >


   


      <el-header class="head">
        <h1>Your Home</h1>
      </el-header>
      <el-main>
        <div>
          <PersonalData style="margin-top: 50px;" />
        </div>
        <h2>Your Articles</h2>
        <ArticleList />
        <!-- Fixed bar at the bottom -->
        <FixedBar />
      </el-main>



    

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
  background-color: #9a8383;
  display: flex;
  align-items: center;

}

/* Center the main title */
h1 {
  text-align: center;
  color: #333;
  background: linear-gradient(to top left, #5ccf5c, #3ab156);
  padding: 20px;
  margin-bottom: 50px;
  border-radius: 60px;
  width: 50%;

}

h2 {

  color: #333;
  background: linear-gradient(to top left, #5ccf5c, #3ab156);
  padding: 20px;
  margin-bottom: 0px;
  border-radius: 60px;
  margin-top: 20px;
  width: 8%;
  font-size: 30px;
  font-weight: bold;

}

.head {
  text-align: center;
  font-size: 50px;
  font-weight: bold;
  margin-bottom: -15px;
  display: flex;
  flex-direction: column;
  align-items: center;
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
    