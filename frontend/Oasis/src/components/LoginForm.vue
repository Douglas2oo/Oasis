<template>
  <el-form ref="ruleFormRef" label-width="120px" :model="ruleform" :rules="rules" class="loginForm sign-in-form">
    <el-form-item label="account" prop="account">
      <el-input v-model="ruleform.account" placeholder="Enter your account" type="text" />
    </el-form-item>
    <el-form-item label="password" prop="password">
      <el-input v-model="ruleform.password" placeholder="Enter your password" type="password" />
    </el-form-item>
    <el-form-item>
      <el-button type="success" class="submit-btn" @click="submitform">Sign in</el-button>
    </el-form-item>
  </el-form>


</template>



<script setup lang="ts">
import { defineProps, defineEmits, watch } from 'vue'
import { ref, reactive } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
import axios from 'axios'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

const store = useStore()

const ruleFormRef = ref<FormInstance>()
const router = useRouter();
const emit = defineEmits(['update:ruleform'])

const { rules, ruleform } =
  defineProps({
    rules: {
      type: Object,
      required: true
    },
    ruleform: {
      type: Object,
      required: true
    }
  })

const Userdata = reactive({
  id: '',
  name: '',
  account: '',
  email: '',
  birthday: '',
})


watch(ruleform, (newval) => {
  emit('update:ruleform', newval)
})

let dialogFormVisible= ref('0')

const submitform = async () => {
  try {
    // create a new axios instance
    const postdata = {
      account: ruleform.account,
      password: ruleform.password
    }

    const response = await axios.post('http://127.0.0.1:8000/login/', postdata, { withCredentials: true })
    // output the response
    if (response.status == 200) {
      console.log("login success")
      Userdata.id = response.data['data']['user_id']
      Userdata.name = response.data['data']['name']
      Userdata.account = response.data['data']['account']
      Userdata.email = response.data['data']['email']
      Userdata.birthday = response.data['data']['birthday']

      router.push({
        name: 'ForumSquare',
        query: {
          id: Userdata.id,
          name: Userdata.name,
          account: Userdata.account,
          email: Userdata.email,
          birthday: Userdata.birthday,
        }
      })
    }
    else {
      console.log("login failed")
      store.state.homeview.loginVisible = '1'
    }
  }
  catch (error) {
    console.log("login failed")
    console.log(error)
    store.state.homeview.loginVisible = '1'
  }



}
</script>

<style>
/* 控制login & register显示 */
form {
  padding: 0rem 5rem;
  transition: all 0.2s 0.7s;
  overflow: hidden;
}

form.sign-in-form {
  z-index: 2;
}

form.sign-up-form {
  opacity: 0;
  z-index: 1;
}

.submit-btn {
  background-color: #37bd76;
}

.submit-btn:hover {
  background-color: #3cc47b;
}

.submit-btn:hover {
  background-color: #3cc47b;
}

.submit-btn {
  width: 100%;
}

.loginForm {
  margin-top: 20px;
  background-color: #fff;
  padding: 20px 40px 20px 20px;
  border-radius: 5px;
  box-shadow: 0px 5px 10px #cccc;
}

.submit-btn {
  width: 100%;
}

.tiparea {
  text-align: right;
  font-size: 12px;
  color: #333;
}


</style>