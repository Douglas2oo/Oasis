<template>
    <el-form 
    ref="ruleFormRef" 
    label-width="120px" 
    :model="ruleform" 
    :rules="rules" 
    class="loginForm sign-in-form">
        <el-form-item label="account" prop="account">
            <el-input v-model="ruleform.account" placeholder="Enter your account" type="text" />
        </el-form-item>
        <el-form-item label="password" prop="password">
            <el-input v-model="ruleform.password" placeholder="Enter your password" type="password" />
        </el-form-item>
        <el-form-item>
            <el-button type="primary" class="submit-btn" @click="submitform">Sign in</el-button>
        </el-form-item>
        <div class="tiparea">
            <a> find password </a>
        </div>
    </el-form>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'
import {ref, reactive} from 'vue'
import type { FormInstance, FormRules } from 'element-plus'


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
const ruleFormRef = ref<FormInstance>()
const submitform = () =>{
    ruleFormRef.value?.validate((valid: any) => {
        if (valid) {
            console.log("submit success")
        } else {
            console.log('error submit!!')
            return false
        }
    })
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
.tiparea p a {
  color: #409eff;
}

</style>