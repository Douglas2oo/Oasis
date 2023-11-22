<template>
  <div style=" margin-top: 10px;">

    <div class="articlebox" style="background-color: white;">

      <div class="flex-container ">
        <el-collapse v-model="activeName" accordion style="width:100%; ">
          <el-collapse-item v-for="(articleItem, index) in activeArticles" class="comment"
            style="width:100%;margin-right:-10px; margin-bottom: 10px;position: relative; "
            @click="GetComment((articleItem as any).author, (articleItem as any).id)">
            <template #title>
              <p class="content">{{ (articleItem as any).content }}</p>
              <div class="btn">
                <el-button size="small" @click="handleEdit(index, articleItem)"
                  style="background-color: #5ccf5c; color: white;">Edit</el-button>
                <el-button size="small" @click="handleDelete(index, articleItem)">Delete</el-button>
              </div>
              <div class="likescomments" style="position: absolute; right: 5vh;"><button class="likesbtn"
                  style="margin-right: 5px;">👍</button>{{ (articleItem as any).likes_count }} 💬{{ (articleItem as
                    any).comments_count }}
              </div>

            </template>
            <p class="content" v-if="Switch == (articleItem as any).id" v-for="(comment, index) in (Comments as any).data"
              :key="`${comment.id}-${index}`" style="min-width: 100%;margin-bottom: 20px;"> Comment {{ index + 1 }}:
            <div style="font-weight: bold;;">
              {{ comment.comment }}
            </div>
            </p>

          </el-collapse-item>
        </el-collapse>




      </div>

    </div>



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

let activeName = ref(['1'])

// 设置需要的参数与方法
const currentPage4 = ref(1)
const pageSize4 = ref(10)


const activeArticles = ref([]); // 添加这行代码



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
      console.log(article.value)
    }
  } catch (error) {
    console.log(error)
    console.log("get article failed")
  }

}
watch([currentPage4, pageSize4, article], () => {
  const startIndex = (currentPage4.value - 1) * pageSize4.value;
  const endIndex = startIndex + pageSize4.value;
  activeArticles.value = article.value.slice(startIndex, endIndex);
});

const Comments = ref([])
const Switch = ref('')
console.log(Switch.value)
const GetComment = async (author: any, article_id: number) => {
  try {
    const response = await axios.get(`http://localhost:8000/commentlist/user_id/${author}/article_id/${article_id}`)
    if (response.status == 200) {
      console.log("get comment success")
      console.log(response.data)
      Comments.value = response.data
      console.log(Comments.value)

      if (Switch.value == '') {
        Switch.value = `${article_id}`
      } else {
        Switch.value = `${article_id}`
      }
      console.log('comment show now:', Switch.value)

    }
  } catch (error) {
    console.log(error)
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
  top: 0px;
  right: 12vh;
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
}</style>
