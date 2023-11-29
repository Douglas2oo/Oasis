<template>
  <div class="box-container">
    <el-card class="box" style="width: 70%">
      <el-form :model="user" label-width="80px" style="padding-right: 20px">
        <div style="margin: 15px; text-align: center">
          <el-upload name="file" ref="upload" class="avatar-uploader" accept=".png,.jpg,.jpeg"
            :http-request="handleAvatarSuccess" :show-file-list="false">
            <img v-if="avatar == 'http://127.0.0.1:8000/media/avatar/default.png'" src="../assets/images/default.png"  class="avatar" />
              <el-avatar v-else class="el-icon-plus avatar-uploader-icon" :src="avatar"/>
            
          </el-upload>


        </div>
        <div class="block1">
          <el-form-item label="Email" prop="email" style="font-weight: bold;">
            <el-input class="smallinput" v-model="user.email" disabled></el-input>
          </el-form-item>
          <el-form-item label="Account" prop="account" style="font-weight: bold;">
            <el-input class="smallinput" v-model="user.account" disabled></el-input>
          </el-form-item>
          <el-form-item label="Username" prop="name" style="font-weight: bold;">
            <el-input class="smallinput" v-model="user.name" disabled></el-input>
          </el-form-item>
          <el-form-item label="Birthday" prop='birthday' style="font-weight: bold;">
            <el-date-picker v-model="user.birthday" type="date" disabled />
          </el-form-item>

        </div>

      </el-form>
    </el-card>
  </div>
</template>
  
<script setup>
import { reactive, ref, onMounted } from 'vue';
import axios from 'axios'
import { useRouter } from "vue-router"

const router = useRouter();
const Userdata = reactive({
  id: router.currentRoute.value.query.id,
})



// 处理头像上传成功
const handleAvatarSuccess = (response) => {
  console.log('Avatar uploaded successfully!');
  // 处理头像上传成功
  console.log('avatar', response.file);
   // 假设后端返回的头像 URL 存在 response.url 中
  uploadToBackend(response.file); // 调用上传到后端的函数
};


const uploadToBackend = (avatarFile) => {
  
  // 将头像上传到后端
  axios.put('http://localhost:8000/avatar/', {
    user_id: Userdata.id,
    avatar: avatarFile,
  }, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })
    .then(response => {
      console.log('Backend response:', response);
      // 可以在这里处理后端的其他响应
      console.log('avatar', avatarFile);
    })
    .catch(error => {
      console.error('Error uploading to backend:', error);
      // 处理上传到后端的错误
    });
    GetAvatar()
    window.location.reload()

    
};


let avatar = ref('')

const GetAvatar = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/avatar/', {
      user_id: Userdata.id
    });
    if (response.status == 200) {
      console.log("get avatar success")
      avatar.value = response.data.data.avatar
    }
  } catch (error) {
    console.log(error)
  }
}

onMounted(() => {
  GetAvatar();
})



const user = reactive({
  name: "",
  email: "",
});

// 向后端发起请求
axios.get('http://localhost:8000/login/')
  .then(response => {
    const targetUser = response.data.find(user => user.user_id === Userdata.id);

    if (targetUser) {
      // 在这里处理找到的目标用户数据
      console.log('Target user found');

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