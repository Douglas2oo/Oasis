<template>
  <div>
    <el-table :data="article.slice((currentPage4 - 1) * pageSize4, currentPage4 * pageSize4)" 
      class="block">

      <el-table-column>
        <template #default="props">
          <div class="articlebox">
            <p class="content">{{ props.row.content }}</p>
            <div class="flex-container ">
              <div class="likescomments"><button v-on:click="props.row.likes.length++" class="likesbtn">👍</button>{{ props.row.likes.length }} 💬0</div>
            </div>
            <div class="btn">
              <el-button size="small" @click="handleEdit(props.$index, props.row)" type="success">Edit</el-button>
              <el-button size="small" @click="handleDelete(props.$index, props.row)">Delete</el-button>
            </div>
          </div>


        </template>
      </el-table-column>
    </el-table>


    <!-- 设置导航 -->
    <!-- 修改下面得属性 -->
    <el-pagination layout="total, sizes, prev, pager, next, jumper" :current-page="currentPage4" :total="article.length"
      @size-change="handleSizeChange" @current-change="handleCurrentChange" />

    <!-- 修改的弹出框 -->
    <Ud />

  </div>
</template>

<script lang="ts" setup>

import { ref, onMounted, reactive, watch } from "vue"
import Ud from "./UpdateDialog.vue"
import { useStore } from "vuex"
import { useRouter } from "vue-router"
import axios from 'axios'

let store = useStore()

// 设置需要的参数与方法
const currentPage4 = ref(1)
const pageSize4 = ref(10)

// 修改下面得方法
const handleSizeChange = (val: number) => {
  //一页显示多少条

  pageSize4.value = val;
}
const handleCurrentChange = (val: number) => {
  //页码更改方法

  currentPage4.value = val;
}

// 添加删除和修改按钮方法与接口
interface User {
  date: string;
  name: string;
  address: string;
}



const handleEdit = (index: number, row: User) => {
  console.log("selected article: ", index, row);
  store.commit("SET_DIALOG", row)
};

const handleDelete = (index: number, row: any) => {
  console.log(index, row);
  console.log(row.id)
  axios.delete(`http://localhost:8000/article/`, { data: { article_id: row.id }, withCredentials: true },)
  window.location.reload()
};
const article = ref([])
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
    const id = Userdata.id//拿到user_id
    const response = await axios.get(`http://127.0.0.1:8000/articlelist/user_id/${id}`)
    if (response.status == 200) {
      console.log("get article success")
      console.log("user's article: ", response.data)
      article.value = response.data
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


<style>
.likesbtn {
  background-color: white;
  padding: 0;
  border: none;
}


.block {
  border-radius: 20px;
}



.btn {
  position: absolute;
  top: 5px;
  right: 5px;
}

.likescomments {
  margin-right: -5px;
  margin-left: 5px;
}


.content {
  margin-bottom: 30px;
}

.articlebox {
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  margin-bottom: 5px;
  margin-top: 5px;
  border-radius: 10px;
  padding: 15px;
  position: relative;
}

.flex-container {
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  margin-bottom: -10px;
}

.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

.body {
  margin-bottom: 50px;
}
</style>
