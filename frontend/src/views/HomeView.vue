<script setup> 
  import {RouterLink} from 'vue-router'
  import {gsap} from 'gsap'
  import { onMounted } from 'vue'
  // import { TextPlugin } from "gsap/TextPlugin";
  import PaytacaLogo from '../components/icons/paytaca_logo.png';
  
  // gsap.registerPlugin(TextPlugin);
  onMounted(async () => {
    var tl = gsap.timeline({repeat: -1, repeatDelay: 1});
    // var tween = gsap.to(".triangle", {rotation: 90, x: 0, duration: 10, ease: "elastic"})
    tl.to(".triangle", {rotation: 90, color:"#f00", x: -300,y: -400, duration: 900, ease: "power2.out"})
      .to(".triangle", {rotation: 360, x: 0, y: 0, duration: 900, ease: "power2.out"})
      .to(".triangle", {rotation: -90, x: 0, y: 0, duration: 900, ease: "power2.out"})
    tl.delay(1)
    tl.play()
    // tween.reverse()
  });
</script>

<template>
  <div class=" h-screen w-screen flex flex-col content-center justify-center">
    <div class="z-50 ">
      <RouterLink to="/option">
        <p class="lupad font-katibeh text-9xl text-center tracking-tight text-black ">Tap to Start</p>
      </RouterLink>
    </div>
    
    <div class="absolute z-0 -bottom-40 -right-11">
      
      <!-- <svg  fill="#DDF2F1" width="1500px" height="auto" viewBox="0 0 15 15" version="1.1" id="triangle" xmlns="http://www.w3.org/2000/svg">
        <path id="path21090-9"  d="M7.5385,2&#xA;&#x9;C7.2437,2,7.0502,2.1772,6.9231,2.3846l-5.8462,9.5385C1,12,1,12.1538,1,12.3077C1,12.8462,1.3846,13,1.6923,13h11.6154&#xA;&#x9;C13.6923,13,14,12.8462,14,12.3077c0-0.1538,0-0.2308-0.0769-0.3846L8.1538,2.3846C8.028,2.1765,7.7882,2,7.5385,2z"/>
      </svg> -->
      <svg class="triangle absolute z-0 bottom-0 -right-52 " width="1000px"  viewBox="0 0 776 773" fill="#DDF2F1" xmlns="http://www.w3.org/2000/svg">
        <path id="Polygon 1" d="M651.597 0.782541L775.364 772.316L0.760684 433.211L651.597 0.782541Z" fill="#DDF2F1"/>
      </svg>
    </div>
    <div class="absolute z-50 bottom-3 right-4">
      <img :src="PaytacaLogo" class="h-10 w-auto" alt="" loading="lazy">

    </div>
  </div>
</template>

<style scoped>
</style>

