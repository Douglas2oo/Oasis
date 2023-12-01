<template>
  <div class="box-container">
    <el-card class="box" style="width: 70%">
      <el-form :model="user" label-width="80px" style="padding-right: 20px">
        <div style="margin: 15px; text-align: center">
          <el-upload name="file" ref="upload" class="avatar-uploader" accept=".png,.jpg,.jpeg"
            :http-request="handleAvatarSuccess" :show-file-list="false">
            <img v-if="avatar == 'http://127.0.0.1:8000/media/avatar/default.png'" src="../assets/images/default.png"
              class="avatar" />
            <el-avatar v-else class="el-icon-plus avatar-uploader-icon" :src="avatar" />
            <span class="hint" style="position: absolute; bottom: -42px; ">Click here to upload your avatar!</span>
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



// Handle successful avatar upload
const handleAvatarSuccess = (response) => {
  console.log('Avatar uploaded successfully!');
  console.log('avatar', response.file);
  //upload the avatar file to backend
  uploadToBackend(response.file);
};


const uploadToBackend = (avatarFile) => {

  // upload the avatar file to backend
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
      console.log('avatar', avatarFile);
    })
    .catch(error => {
      console.error('Error uploading to backend:', error);
    });
  GetAvatar1();

};


let avatar = ref('')

//Initial avatar retrieval function
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

//The retrieval function after changing the avatar
const GetAvatar1 = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/avatar/', {
      user_id: Userdata.id
    });
    if (response.status == 200) {
      console.log("get avatar success")
      avatar.value = response.data.data.avatar
      window.location.reload()
    }
  } catch (error) {
    console.log(error)
  }
}


// User data
const user = reactive({
  name: "",
  email: "",
});

const GetUserData = async () => {
    axios.get('http://localhost:8000/login/')
  .then(response => {
    const targetUser = response.data.find(user => user.user_id === Userdata.id);

    if (targetUser) {
      // Handle the found target user data here
      console.log('Target user found');

    } else {
      console.log('Target user not found');
    }

    // data get from backend
    const name = targetUser.name;
    const email = targetUser.email;
    const birthday = targetUser.birthday;
    const account = targetUser.account;

    // Store the data in localStorage
    localStorage.setItem('name', JSON.stringify(name))
    localStorage.setItem('email', JSON.stringify(email))
    localStorage.setItem('birthday', JSON.stringify(birthday))
    localStorage.setItem('account', JSON.stringify(account))

  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
  }


// retrieve data from localStorage
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

onMounted(() => {
  GetAvatar();
  GetUserData();
})

</script>

  
<style scoped>

.hint:hover {
  color: rgb(44, 182, 60);
  cursor: pointer;
  
}

.hint {
  font-weight: bold;
  font-size: 15px;
}

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
  top: 5vh
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