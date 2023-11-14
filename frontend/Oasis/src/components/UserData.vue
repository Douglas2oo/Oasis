<template>
  <div class="box-container">
    <el-card class="box" style="width: 70%">
      <el-form :model="user" label-width="80px" style="padding-right: 20px">
        <div style="margin: 15px; text-align: center">
          <el-upload class="avatar-uploader" action=" http://localhost:8000/user" :show-file-list="false"
            :on-success="handleAvatarSuccess">
            <img v-if="user.avatar" :src="user.avatar" class="avatar" />
            <div v-else style="padding-bottom: 15px;">
              <el-avatar class="el-icon-plus avatar-uploader-icon" src="用户头像" />
            </div>

          </el-upload>
        </div>
        <div class="block1">
          <el-form-item label="email" prop="email">
            <el-input class="smallinput" v-model="user.email" disabled></el-input>
          </el-form-item>
          <el-form-item label="account" prop="account">
            <el-input class="smallinput" v-model="user.account" disabled></el-input>
          </el-form-item>
          <el-form-item label="username" prop="name">
            <el-input class="smallinput" v-model="user.name" disabled></el-input>
          </el-form-item>
          <el-form-item label="Birthday" prop='birthday'>
            <el-date-picker v-model="user.birthday" type="date" disabled/>
          </el-form-item>

        </div>

      </el-form>
    </el-card>
  </div>
</template>
  
<script setup>
import { reactive } from 'vue';
import axios from 'axios'
import { useRouter } from "vue-router"

const router = useRouter();
const Userdata = reactive({
  id: router.currentRoute.value.query.id,
})
console.log("get id:", Userdata.id)

// 处理头像上传成功
const handleAvatarSuccess = (file) => {
  // 把user的头像属性换成上传的图片的链接
  user.value.avatar = URL.createObjectURL(file.raw);
};
// const handleAvatarSuccess = (file) => {
//   // 把user的头像属性换成上传的图片的链接
//   user.value.avatar = URL.createObjectURL(file.raw);
// };

const user = reactive({
  name: "",
  email: "",
});
// 向后端发起请求
axios.get('http://localhost:8000/login/')
  .then(response => {
    console.log('userdata', response.data);
    const targetUser = response.data.find(user => user.user_id === Userdata.id);

    if (targetUser) {
      // 在这里处理找到的目标用户数据
      console.log('Target user found:', targetUser);

    } else {
      console.log('Target user not found');
    }
    // 获取到后端返回的数据
    const name = targetUser.name;
    const email = targetUser.email;
    const birthday = targetUser.birthday;
    const account = targetUser.account;
    // 将数据存储在localStorage中
    localStorage.setItem('name', JSON.stringify(name))
    localStorage.setItem('email', JSON.stringify(email))
    localStorage.setItem('birthday', JSON.stringify(birthday))
    localStorage.setItem('account', JSON.stringify(account))

  })
  .catch(error => {
    console.error('Error fetching data:', error);
    // 处理请求错误
  });

// 从localStorage中获取数据
const nameString = localStorage.getItem('name');
const name = nameString.replace(/^"|"$/g, '');
user.name = name

const emailString = localStorage.getItem('email');
const email = emailString.replace(/^"|"$/g, '');
user.email = email

const birthdayString = localStorage.getItem('birthday');
const birthday = birthdayString.replace(/^"|"$/g, '');
user.birthday = birthday

const accountString = localStorage.getItem('account');
const account = accountString.replace(/^"|"$/g, '');
user.account = account

</script>

  
<style scoped>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

.box-container {
  display: flex;
  justify-content: center;
}


.biginput {
  width: 100%;

  margin-top: 10px;
}


.el-button {
  text-align: center;
}

.block2 {
  position: absolute;
  top: 32vh;
  margin-top: -50px;
  left: 4vh;
  right: 4vh;
}

.smallinput {
  width: 100%;

}

.block1 {
  position: absolute;
  right: 5vh;
  margin-bottom: 200px;

}

.avatar-uploader {
  position: absolute;
  left: 20vh;
  top: 7vh
}

.box {
  position: relative;
  min-height: 500vh;
  min-height: 30vh;
  border-radius: 20px;


}

.el-form-item__label {
  font-weight: bold;
}

.el-upload {
  border-radius: 50%;
}

.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  cursor: pointer;
  overflow: hidden;
  border-radius: 50%;
}

.avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 150px;
  height: 150px;
  line-height: 120px;
  text-align: start;
  border-radius: 50%;
}

.avatar {
  width: 150px;
  height: 150px;
  display: block;
  border-radius: 50%;
}
</style>