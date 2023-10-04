<template>
    <el-form 
    ref="ruleFormRef" 
    label-width="120px" 
    :model="registerForm" 
    :rules="registerrules"
    class="registerForm sign-up-form">
        <el-form-item label="name" prop="name">
            <el-input v-model="registerForm.name" placeholder="Enter your name" type="text" />
        </el-form-item>
        <el-form-item label="account" prop="account">
            <el-input v-model="registerForm.account" placeholder="Enter your account" type="text" />
        </el-form-item>
        <el-form-item label="email" prop="email">
            <el-input v-model="registerForm.email" placeholder="Enter your email" type="text" />
        </el-form-item>
        <el-form-item label="Birthday">
            <el-col :span="11">
                <el-date-picker v-model="registerForm.birthday" type="date" placeholder="Pick a date" />
            </el-col>
            <el-col :span="2" class="text-center">
                <span class="text-gray-500">-</span>
            </el-col>
        </el-form-item>
        <el-form-item label="password" prop="password">
            <el-input v-model="registerForm.password" placeholder="Enter your password" type="password" />
        </el-form-item>
        <el-form-item label="password2" prop="password2">
            <el-input v-model="registerForm.password2" placeholder="Enter your password again" type="text" />
        </el-form-item>
        <el-form-item>
            <el-button type="primary" class="submit-btn" @click="registersubmit">Sign up</el-button>
        </el-form-item>
    </el-form>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'
import { ref, reactive } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'


defineProps({
    registerrules: {
        type: Object,
        required: true
    },
    registerForm: {
        type: Object,
        required: true
    }
})

const ruleFormRef = ref<FormInstance>()
const registersubmit = () => {
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
.registerForm {
    margin-top: 20px;
    background-color: #fff;
    padding: 20px 40px 20px 20px;
    border-radius: 5px;
    box-shadow: 0px 5px 10px #cccc;
  }

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
  
.text-center {
    text-align: center;
  }
  
.text-gray-500 {
    color: #a0aec0;
  }
    

<style scoped></style>