<template>
    <el-form ref="ruleFormRef" label-width="120px" :model="registerForm" :rules="registerrules"
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
        <el-form-item label="birthday" prop='birthday'>
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
            <el-input v-model="registerForm.password2" placeholder="Enter your password again" type="password" />
        </el-form-item>
        <el-form-item>
            <el-button type="success" class="submit-btn" @click="registersubmit">Sign up</el-button>
        </el-form-item>
    </el-form>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, watch } from 'vue'
import { ref, reactive } from 'vue'
import { dateEquals, type FormInstance, type FormRules } from 'element-plus'
import { useRouter } from 'vue-router';
import axios from 'axios'
import { useStore } from 'vuex';

const store = useStore()

const emit = defineEmits(['update:registerForm'])
const router = useRouter()

const ruleFormRef = ref<FormInstance>()
const Userdata = reactive({
    id: '',
    name: '',
    account: '',
    email: '',
    birthday: '',
})

const { registerrules, registerForm } =
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


watch(registerForm, (newValue) => {
    emit('update:registerForm', newValue)
})


/*
change the date format
*/
const changedate = (birthdaydate) => {
    const birthdate = new Date(birthdaydate)
    const year = birthdate.getFullYear()
    const month = birthdate.getMonth() + 1
    const day = birthdate.getDate()

    const formattedBirthday = ref(`${year}-${month < 10 ? '0' : ''}${month}-${day < 10 ? '0' : ''}${day}`)
    return formattedBirthday
}


const registersubmit = async () => {
    const postdata = {
        name: registerForm.name,
        account: registerForm.account,
        email: registerForm.email,
        birthday: changedate(registerForm.birthday).value,
        password: registerForm.password,
        password2: registerForm.password2,
    }
    try {
        const response = await axios.post('http://localhost:8000/register/', postdata, { withCredentials: true })
        console.log("status", response.data)
        if (response.data.success) {
            console.log("register success")
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
            console.log("register failed")
            store.state.homeview.registerVisible = '1'
        }
    } catch (error) {
        console.log("register failed")
        store.state.homeview.registerVisible = '1'
        console.log(error)
    }
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