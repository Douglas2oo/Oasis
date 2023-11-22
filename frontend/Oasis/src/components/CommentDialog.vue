<template>
  <el-dialog class="BOX" v-model="store.state.homeview.commentVisible" title="Write your comment!">
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
})

let store = useStore()



let closeDialog = (num: number) => {

  if (num == 1) {
    console.log(form.content) //要发表什么评论

    let data = {
      article_id: store.state.homeview.Comment.id,
      comment: form.content,
      user_id: Userdata.id,

    }

    axios.post('http://localhost:8000/comment/', data, { withCredentials: true })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

    window.location.reload()
  }
  store.commit("CLOSE_DIA")

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