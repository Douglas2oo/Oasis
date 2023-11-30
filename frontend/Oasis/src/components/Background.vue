<template>
  <div class="vanta_area" ref="Area"></div>
</template>
<script setup>
import * as THREE from 'three'
import GLOBE from 'vanta/src/vanta.globe'
import {onMounted,onBeforeUnmount,ref} from 'vue'

//Mounting area using ref reference
const Area=ref(null)

/**
In Vue 2, we used this.vantaEffect to create a specified 3D animation template. However, in Vue 3 setup, there is no 'this,' so a separate one needs to be created.
**/

let vantaEffect=null;

onMounted(()=>{
  vantaEffect=GLOBE({
      el:Area.value,
      THREE:THREE,
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
