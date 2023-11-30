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

//retrieve user id from router
const Userdata = reactive({
  id: router.currentRoute.value.query.id,
})

const form = reactive({
  content: '',
  article_id: '',
})

let store = useStore()

// Listen for changes in uplistData

watchEffect(() => {
  const content1 = store.state.homeview.uplistData.content;
  const id = store.state.homeview.uplistData.id;

  // Store data in localStorage
  localStorage.setItem('content', JSON.stringify(content1))
  localStorage.setItem('id', JSON.stringify(id))

  // Retrieve data from localStorage
  const contentString = localStorage.getItem('content')
  const idString = localStorage.getItem('id')
  if (contentString) {
    form.content = contentString.replace(/^"|"$/g, '')
  }

  if (idString !== null) {
    form.article_id = idString;
  }

});


let closeDialog = (num: number) => {

  if (num == 1) {
    let data = {
      content: form.content,
      article_id: form.article_id,
      author: Userdata.id,
    }
    axios.put('http://127.0.0.1:8000/article/', data, { withCredentials: true })
    window.location.reload()
  }
  store.commit("DIALOG")

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