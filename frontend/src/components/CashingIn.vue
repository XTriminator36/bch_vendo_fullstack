<script setup>
import { ref, onMounted } from 'vue';
import { inject } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue';
// import { QrcodeStream, QrcodeCapture } from 'vue-qrcode-reader'
// import { CheckCircleIcon } from '@heroicons/vue/24/solid';
import BitcoinGif from './icons/bitcoin.gif';
import { useCounterStore } from '../stores/counter';
const counter = useCounterStore();


const open = ref(false)
const detectedCodes = ref([])
const isLoading = ref(false)

const closeSuccess =  function() {
  open.value = false
  isLoading.value=false
  clearDetectedCodes()
}
const openSuccess = function() {
  open.value = true
}
const onDetect = (code) => {
  detectedCodes.value.push(code);
  if (detectedCodes.value.length > 0){
    // const rawValue = detectedCodes.value
    // counter.qrcodeObj
    counter.$patch({qrcodeObj: detectedCodes.value});
    console.log(counter.qrcodeObj)
    isLoading.value=true
  }
  getList()
}
const clearDetectedCodes = () => {
  detectedCodes.value = [];
}
const axios = inject('axios'); // inject axios
const getList = () => {
  axios
    .post('https://jsonplaceholder.typicode.com/posts', {
        detectedCodes
    })
    // .then(response => {
    //     console.log(response.data);
    // });
};

//Get Confirmation that the cashing in has been successful
const getConfirmation = () => {
  axios
    .post('https://jsonplaceholder.typicode.com/posts', {
        detectedCodes
    })
    .then(response => {
      console.log(response.data);
    });
};
const gif = ref(null);
let replayCount = 0;

onMounted(() => {
  if (gif.value) {
    gif.value.addEventListener('animationiteration', handleAnimationIteration);
  }
});

const handleAnimationIteration = () => {
  replayCount++;
  if (replayCount >= 3) {
    if (gif.value) {
      gif.value.style.animationPlayState = 'paused'; // Pause the animation after three replays
    }
  }
};

defineExpose({
  openSuccess,
  closeSuccess
})
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
                    <div class="mt-3 text-center sm:mt-0 sm:text-left min-h-96">
                        <DialogTitle as="h3" class="text-xl font-dela font-normal leading-6 bg-[#C7FF51] w-10/12 text-black p-3 text-left tracking-normal">
                          Insert your bill now
                        </DialogTitle>
                        <div class="mt-3">
                          <p class="font-space ml-4">Hey, ready as you are...</p>
                          <div class="flex justify-center">
                            <img ref="gif" class="w-56" :src="BitcoinGif" alt="Your GIF" />
                          </div>
                        </div>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 flex items-center justify-center sm:px-6"> 
                  <!-- <button type="button" class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto" @click="open = false">Deactivate</button>  -->
                  <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-5 py-3 text-sm font-dela font-normal text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="closeSuccess" ref="cancelButtonRef">Close</button>
                  <button type="button" class="ml-3 mt-3 w-full justify-center rounded-md bg-[#53A0FB] px-5 py-3 text-md font-dela font-normal text-white shadow-sm  hover:bg-lime-300 hover:text-black sm:mt-0 sm:w-auto transition-colors" disabled  @click="openModal" >Done</button>

                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
    
</template>
