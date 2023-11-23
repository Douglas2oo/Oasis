<template>
  <div class="vanta_area" ref="Area"></div>
</template>
<script setup>
//导入vanta.js和three.js，以及ref等hooks
import * as THREE from 'three'
import GLOBE from 'vanta/src/vanta.globe'
import {onMounted,onBeforeUnmount,ref} from 'vue'

//使用ref引用挂载区域
const Area=ref(null)
//创建一个全局的变量来使用vanta.js
/**
*因为在vue2中，是使用this.vantaEffect来创建指定的3d动画模板的
*但是vue3 setup中是没有this，所以要另外创建一个
**/
let vantaEffect=null;
//在两个生命周期钩子内创建vantaEffect
onMounted(()=>{
  vantaEffect=GLOBE({
      el:Area.value,
      THREE:THREE,
      //如果需要改变样式，要写在这里
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 200.00,
      minWidth: 200.00,
      scale: 1.00,
      scaleMobile: 1.00,
      color: 0x7de0ab,
      size: 1.30,
      backgroundColor: 0xffffff
      //因为这里vantaEffect是没有setOptions这个方法的

  })
})

onBeforeUnmount(()=>{
  if(vantaEffect){
      vantaEffect.destroy()
  }
})
</script>
<style  scoped>
.vanta_area {
width:100vw;
height:100vh;
}
</style>
