<template>
  <div class="container" :class="{ 'sign-up-mode': signUpMode }">
    <div class="forms-container">
      <Background />
      <div class="signin-signup">
        <LoginForm :ruleform="ruleform" :rules="rules" />
        <RegisterForm :registerrules="registerrules" :registerForm="registerForm" />

      </div>
    </div>

    <div class="panels-container">
      <div class="panel left-panel">
        <div class="content">
          <h3>Life is a journey</h3>
          <button @click="signUpMode = !signUpMode" class="btn transparent">Sign up</button>
        </div>
        <img src="@/assets/images/circlelogo.png" class="image" alt="" />
      </div>

      <div class="panel right-panel">
        <div class="content">
          <h3>Feel the world</h3>
          <button @click="signUpMode = !signUpMode" class="btn transparent">Sign in</button>
        </div>
        <img src="@/assets/images/circlelogo.png" class="image" alt="" />
      </div>
    </div>
  </div>
  <el-dialog class="BOX" v-model="store.state.homeview.loginVisible" title="Login failed." style="border-radius: 2vh;">
    <span>Invalid account or password!</span>

  </el-dialog>
  <el-dialog class="BOX" v-model="store.state.homeview.registerVisible" title="Register failed."
    style="border-radius: 2vh;">
    <span>Please verify the entered information for accuracy.</span>

  </el-dialog>
</template>



<script setup lang="ts">
import { reactive, ref, onMounted } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
import LoginForm from '../components/LoginForm.vue'
import RegisterForm from '../components/RegisterForm.vue'
import Background from '../components/background.vue'
import { useStore } from 'vuex'

const store = useStore()

// Verification rules
const ruleFormRef = ref<FormInstance>()
const signUpMode = ref(false)


// login rules
const ruleform = ref({
  account: '',
  password: ''
})

const registerForm = ref(
  {
    name: '',
    account: '',
    email: '',
    birthday: '',
    password: '',
    password2: ''
  }
)


const rules: FormRules = {
  account: [
    { required: true, message: 'Please input account', trigger: 'blur' },
    { type: 'string', message: 'Please input correct account', trigger: ['blur', 'change'] }
  ],
  password: [
    { required: true, message: 'Please input password', trigger: 'blur' },
    { type: 'string', min: 6, max: 20, message: 'Length should be 6 to 20', trigger: 'blur' },
    { pattern: /^[a-zA-Z0-9_]+$/, message: 'Only support letters, numbers and underline', trigger: 'blur' }
  ]
}


// password verification

const validatorpass = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('Please input password again'))
  } else if (value !== registerForm.value.password) {
    callback(new Error('Two passwords are inconsistent'))
  } else {
    callback()
  }
}


const registerrules: FormRules = {
  name: [
    { required: true, message: 'Please input name', trigger: 'blur' },
    { type: 'string', message: 'Please input correct name', trigger: ['blur', 'change'] }
  ],
  account: [
    { required: true, message: 'Please input account', trigger: 'blur' },
    { type: 'string', message: 'Please input correct account', trigger: ['blur', 'change'] }
  ],
  email: [
    { required: true, message: 'Please input email', trigger: 'blur' },
    { type: 'email', message: 'Please input correct email', trigger: ['blur', 'change'] }
  ],

  password: [
    { required: true, message: 'Please input password', trigger: 'blur' },
    { type: 'string', min: 6, max: 20, message: 'Length should be 6 to 20', trigger: 'blur' },
    { pattern: /^[a-zA-Z0-9_]+$/, message: 'Only support letters, numbers and underline', trigger: 'blur' }
  ],
  password2: [
    { required: true, message: 'Please input password again', trigger: 'blur' },
    { validator: validatorpass, trigger: ['blur', 'change'] }
  ]
}





</script>


<style>
.container {
  position: relative;
  width: 100%;
  background-color: #ffffff;
  min-height: 100vh;
  overflow: hidden;
}

.loginForm {
  margin-top: 20px;
  background-color: #fff;
  padding: 20px 40px 20px 20px;
  border-radius: 5px;
  box-shadow: 0px 5px 10px #cccc;
}

.forms-container {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
}

.signin-signup {
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  left: 75%;
  width: 44%;
  transition: 1s 0.7s ease-in-out;
  display: grid;
  grid-template-columns: 1fr;
  z-index: 5;
}

/* 左右切换动画 */
.social-text {
  padding: 0.7rem 0;
  font-size: 1rem;
}

.social-media {
  display: flex;
  justify-content: center;
}

.social-icon {
  height: 46px;
  width: 46px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 0.45rem;
  color: #333;
  border-radius: 50%;
  border: 1px solid #333;
  text-decoration: none;
  font-size: 1.1rem;
  transition: 0.3s;
}

.social-icon:hover {
  color: #3db173;
  border-color: #4BA474;
}

.btn {
  width: 15px;
  border: none;
  outline: none;
  height: 49px;
  border-radius: 49px;
  color: #fff;
  text-transform: uppercase;
  font-weight: 600;
  margin: 10px 0;
  cursor: pointer;
  transition: 0.5s;

}

.btn:hover {
  background-color: #4BA474;
}

.panels-container {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}

/* 大板块 */
.container:before {
  content: "";
  position: absolute;
  height: 2000px;
  width: 2000px;
  top: -10%;
  right: 48%;
  transform: translateY(-50%);
  background-image: linear-gradient(-30deg, rgb(93, 203, 145, 0.6) 0%, #7de0ab 100%);
  transition: 1.8s ease-in-out;
  border-radius: 50%;
  z-index: 6;
}

.image {
  width: 30%;
  transition: transform 1.1s ease-in-out;
  transition-delay: 0.4s;

}

.panel {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: space-around;
  text-align: center;
  z-index: 6;
}

.left-panel {
  pointer-events: all;
  padding: 3rem 17% 2rem 12%;
}

.right-panel {
  pointer-events: none;
  padding: 3rem 12% 2rem 17%;
}

.panel .content {
  color: #fff;
  transition: transform 0.9s ease-in-out;
  transition-delay: 0.6s;
}

.panel h3 {
  font-weight: 600;
  line-height: 1;
  font-size: 1.5rem;
}

.panel p {
  font-size: 0.95rem;
  padding: 0.7rem 0;
}

.btn.transparent {
  margin: 0;
  background: none;
  border: 2px solid #fff;
  width: 130px;
  height: 41px;
  font-weight: 600;
  font-size: 0.8rem;

}

.right-panel .image,
.right-panel .content {
  transform: translateX(800px);
}

/* ANIMATION */

.container.sign-up-mode:before {
  transform: translate(100%, -50%);
  right: 52%;
}

.container.sign-up-mode .left-panel .image,
.container.sign-up-mode .left-panel .content {
  transform: translateX(-800px);
}

.container.sign-up-mode .signin-signup {
  left: 25%;
}

.container.sign-up-mode form.sign-up-form {
  opacity: 1;
  z-index: 2;
}

.container.sign-up-mode form.sign-in-form {
  opacity: 0;
  z-index: 1;
}

.container.sign-up-mode .right-panel .image,
.container.sign-up-mode .right-panel .content {
  transform: translateX(0%);
}

.container.sign-up-mode .left-panel {
  pointer-events: none;
}

.container.sign-up-mode .right-panel {
  pointer-events: all;
}

@media (max-width: 870px) {
  .container {
    min-height: 800px;
    height: 100vh;
  }

  .signin-signup {
    width: 100%;
    top: 95%;
    transform: translate(-50%, -100%);
    transition: 1s 0.8s ease-in-out;
  }

  .signin-signup,
  .container.sign-up-mode .signin-signup {
    left: 50%;
  }

  .panels-container {
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 2fr 1fr;
  }

  .panel {
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    padding: 2.5rem 8%;
    grid-column: 1 / 2;
  }

  .right-panel {
    grid-row: 3 / 4;
  }

  .left-panel {
    grid-row: 1 / 2;
  }

  .image {
    width: 200px;
    transition: transform 0.9s ease-in-out;
    transition-delay: 0.6s;
  }

  .panel .content {
    padding-right: 15%;
    transition: transform 0.9s ease-in-out;
    transition-delay: 0.8s;
  }

  .panel h3 {
    font-size: 1.2rem;
  }

  .panel p {
    font-size: 0.7rem;
    padding: 0.5rem 0;
  }

  .btn.transparent {
    width: 110px;
    height: 35px;
    font-size: 0.7rem;
  }

  .container:before {
    width: 1500px;
    height: 1500px;
    transform: translateX(-50%);
    left: 30%;
    bottom: 68%;
    right: initial;
    top: initial;
    transition: 2s ease-in-out;
  }

  .container.sign-up-mode:before {
    transform: translate(-50%, 100%);
    bottom: 32%;
    right: initial;
  }

  .container.sign-up-mode .left-panel .image,
  .container.sign-up-mode .left-panel .content {
    transform: translateY(-300px);
  }

  .container.sign-up-mode .right-panel .image,
  .container.sign-up-mode .right-panel .content {
    transform: translateY(0px);
  }

  .right-panel .image,
  .right-panel .content {
    transform: translateY(300px);
  }

  .container.sign-up-mode .signin-signup {
    top: 5%;
    transform: translate(-50%, 0);
  }
}

/* register */

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


@media (max-width: 570px) {
  form {
    padding: 0 1.5rem;
  }

  .image {
    display: none;
  }

  .panel .content {
    padding: 0.5rem 1rem;
  }

  .container {
    padding: 1.5rem;
  }

  .container:before {
    bottom: 72%;
    left: 50%;
  }

  .container.sign-up-mode:before {
    bottom: 28%;
    left: 50%;
  }
}

.btn {
  background-color: #4BA474;
}
</style>