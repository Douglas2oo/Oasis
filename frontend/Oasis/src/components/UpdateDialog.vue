<template>
  <el-dialog class="BOX" v-model="store.state.homeview.dialogFormVisible" title="Edit your article.">
    <el-form :model="form" :label-width="formLabelWidth">


      <el-form-item label="content" :label-width="formLabelWidth">
        <el-input v-model="form.content" autocomplete="off" type="textarea" style="margin-right: 80px;" />
      </el-form-item>

    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="closeDialog(0)">Cancel</el-button>
        <el-button type="success" @click="closeDialog(1)">Confirm</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup lang="ts">
import { reactive, ref, watchEffect } from 'vue'
import { useStore } from 'vuex';
import { useRouter } from "vue-router"
import axios from 'axios'


const router = useRouter();
const Userdata = reactive({
  id: router.currentRoute.value.query.id,
})

const form = reactive({
  content: '',
  article_id: '',
})

let store = useStore()

// 监听 uplistData 的变化

watchEffect(() => {
  const content1 = store.state.homeview.uplistData.content;
  const id = store.state.homeview.uplistData.id;
  console.log("content: ", content1)
  // 将数据存储在localStorage中
  localStorage.setItem('content', JSON.stringify(content1))
  localStorage.setItem('id', JSON.stringify(id))
  // 获取localStorage中的数据
  const contentString = localStorage.getItem('content')
  const idString = localStorage.getItem('id')
  if (contentString) {
    form.content = contentString.replace(/^"|"$/g, '')
  }

  if (idString !== null) {
    form.article_id = idString;
  }

});


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



let closeDialog = (num: number) => {

  if (num == 1) {

    // 获取当前北京时间并格式化为 "YYYY-MM-DD HH:mm" 格式
    const currentDate = getBeijingTime();
    const formattedDate = formatDateTime(currentDate);

    console.log(store.state.homeview.uplistData)
    console.log(store.state.homeview.uplistData.content)
    console.log(form.content) //要修改成什么
    console.log(formattedDate) //修改时间


    let data = {

      content: form.content,
      article_id: form.article_id,
      author: Userdata.id,
      create_time: formatDateTime,
      likes: Array(0)

    }

    axios.put('http://127.0.0.1:8000/article/', data, { withCredentials: true })

  }
  store.commit("DIALOG")
  window.location.reload()
}


const formLabelWidth = '140px'


</script>

<style scoped>
.el-button--text {
  margin-right: 15px;
}

.el-select {
  width: 300px;
}

/* .el-input {
  width: 300px;
} */
.dialog-footer button:first-child {
  margin-right: 10px;
}

.BOX {
  border-radius: 40px;
}
</style>