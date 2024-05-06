<script setup>
import { ref, watch } from 'vue';
import  {useCounterStore}  from '../stores/counter'
import { gsap } from 'gsap'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue';
import CameraScan from "./CameraScan.vue"

// import { CheckCircleIcon } from '@heroicons/vue/24/solid';
// import PaytacaLogo from './icons/paytaca_logo.png';
const open = ref(false)
const isLoading = ref(false)
const num = ref()
const error1 = ref(false)
const tempNum = ref(0)
const animatedDiv = ref(null)
const counter = useCounterStore()

const closeSuccess =  function() {
  open.value = false
  isLoading.value=false
  error1.value= false
  setTimeout(() => {
    num.value = '';
  }, 500);  
  // clearDetectedCodes()
}
const openSuccess = function() {
  open.value = true
}


const submitBtn = function() {
  if ((num.value % 20 == 0 || num.value % 50 == 0) && num.value != 0) {
    console.log((num.value % 20))
    console.log("divisible by 20")
    counter.fetchData()
    counter.$patch({submittedData: num.value}); // Store submitted data in Pinia store
    closeSuccess()
    openModal()
  } else {
    tempNum.value = num.value
    error1.value = true
    errorDisp()
    console.log("not divisible by 20")
  }
}

const errorDisp = function() {
  var tl = gsap.timeline();
        tl.to(animatedDiv.value, { opacity: 1, duration: .5,  scale:1, y:-10, ease: "back.out" })
        .to(animatedDiv.value, { duration: .5, opacity: 1, scale:1, y:0, ease: "elastic" })
}

const isDivisibleBy20Or50 = (value) => {
  return  (value != '' && value != 0) && (value % 20 === 0 || value % 50 === 0);
};
// Debounce function
const debounce = (func, delay) => {
  let timeoutId;
  return (...args) => {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }
    timeoutId = setTimeout(() => {
      func(...args);
    }, delay);
  };
};

watch(num, debounce((newValue) => {
  error1.value = !isDivisibleBy20Or50(newValue);
  errorDisp()
}, 800)); // Wait for 500 milliseconds after user stops typing

// watch(num, debounce(() => {
//   // error1.value = !isDivisibleBy20Or50(newValue);
//   errorDisp()
// }, 1500)); // Wait for 500 milliseconds after user stops typing

const modal = ref(null)
const openModal = () => {
    modal.value.openSuccess()
}
defineExpose({
  openSuccess,
  closeSuccess
})
</script>

<script>


// export default {
//   beforeRouteLeave(to, from, next) {
//     // const tl = gsap.timeline({
//     //   onComplete: () => {
//     //     next();
//     //   }
//     // });
//     // tl.to(".vendoMach", { duration: .2,  scale:1, y:-20, ease: "back.in" })
//     //     .to(".vendoMach", { duration: .4, opacity: 0, scale:1, y:300, ease: "back.in" })
//     //     .to(".cashIn", { duration: .2,  scale:1, y:-20, ease: "back.out" }, "-=0.2")
//     //     .to(".cashIn", { duration: .4, opacity: 0, y:200, scale:1,ease: "back.in" }, "-=0.2")
//     //     .to(".background1", { duration: .3, opacity: 0, ease: "back" }, "-=0.001")
//   }
// }
</script>

<template>
    <TransitionRoot appear :show="open" as="template" >
      <Dialog as="div" class="relative z-10" @close="closeSuccess">
        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity">
          </div>
        </TransitionChild>
  
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel class="relative transform overflow-hidden rounded-2xl bg-white/75 text-left shadow-xl transition-all sm:max-h-max  sm:my-8 sm:w-full sm:max-w-xl">
                <div class="bg-white min-h-96 px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                  <div class="">
                    <!-- <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                      <ExclamationTriangleIcon class="h-6 w-6 text-red-600" aria-hidden="true" />
                    </div> -->
                    <div class="mt-3 text-center sm:mt-0 sm:text-left min-h-80">
                        <DialogTitle as="h3" class="text-2xl font-dela font-normal leading-6 mt-3 w-fit text-black px-2 mb-2 text-left tracking-normal">
                          Hello there!
                        </DialogTitle>
                        <!-- <p class="text-stone-950 font-space mt-7  text-2xl mb-1 leading-5 pl-2 ">Hello there!</p> -->
                        <p class="text-stone-950 font-space  mb-2 text-lg leading-5 pl-2 font-light"> How much are we cashing-in today?</p>
                        <div v-if="isLoading==false" class="flex flex-col justify-center mt-20">
                            <!-- <p class="text-7xl font-space font-medium text-center p-2">₱</p> -->
                            <div class="block text-center">
                              <span class="font-space p-2 font-bold text-6xl">₱</span>
                              <input type="number" class="font-dela text-5xl text-center min-w-60 max-w-72 font-normal rounded border-2 border-black " v-model="num"  placeholder="---"/>
                            </div>
                            <div class="mx-auto text-center mt-4 w-72 ">
                              <p class="font-space font-thin ">Note: Input amount in bills, or in 20s or 50s. (ex: 20, 50, 120, 150...)</p>
                            </div>
                            <div ref="animatedDiv" class="yey opacity-0 flex flex-col justify-center text-center mx-auto mt-6 transition-opacity duration-500 ease-in-out ">
                              <div v-if="error1" class="font-space text-pretty text-white text-center max-w-96 px-5 py-3 rounded bg-red-500 ring-red-700 ring-1">
                               <p>Your amount is invalid. Please input amount in bills, in 20s or in 50s.</p> 
                              </div>
                              <div v-else class="font-mono text-pretty text-black text-center max-w-72 px-5 py-3 rounded bg-lime-300 ring-lime-200 ring-1">
                                Would you like to proceed?
                              </div>
                            </div>
                            
                        </div>
                        <div v-else class="my-auto mx-auto">
                          <svg  class="w-28 h-28 text-black/25 animate-spin my-auto mx-auto" fill="none"
                              viewBox="0 0 24 24"
                              xmlns="http://www.w3.org/2000/svg">
                            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                            <path class="opacity-75"
                                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                                  fill="currentColor">
                            </path>
                          </svg>    
                        </div>
                        
                        <!-- <div v-for="(qrs, index) in detectedCodes" :key="index">
                            <p> {{ qrs }}</p>
                        </div> -->
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 flex items-center justify-center sm:px-6 gap-5"> 
                  <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-5 py-3 text-sm font-dela font-normal text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="closeSuccess" ref="cancelButtonRef">Close</button>
                  <button type="button" :class="[error1 ? 'bg-gray-400 text-gray-600': ' bg-lime-400 text-gray-900 hover:bg-lime-300 hover:text-white ' , 'mt-3 inline-flex w-full justify-center rounded-md px-5 py-3 text-sm font-dela font-normal shadow-sm transition-colors sm:mt-0 sm:w-auto']" :disabled="error1" @click="submitBtn" ref="submitButtonRef">Continue</button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
    <CameraScan ref="modal">

    </CameraScan>
</template>
