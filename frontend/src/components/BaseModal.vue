<script setup>
import { ref } from 'vue';
// import PaySuccess from './PaySuccess.vue';
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue';
import { ExclamationTriangleIcon } from '@heroicons/vue/24/outline';
import PaySuccess from "../components/PaySuccess.vue";
import PayError from "../components/PayError.vue";
import PaytacaLogo from './icons/paytaca_logo.png';
import VQrcode, { ErrorCorrectLevel, RenderOptions } from 'qrcode-vuejs';

const open = ref(false)
const success = ref(null)
const fail = ref(null)
const closeModal =  function() {
    open.value = false
}
const openModal = function() {
    open.value = true
}
const openSuccess = () => {
    success.value.openSuccess()
    closeModal()
}
const openFail = () => {
    fail.value.openFail()
    closeModal()
}
defineExpose({
  openModal,
  closeModal
})
</script>

<template>
    <TransitionRoot appear :show="open" as="template" >
      <Dialog as="div" class="relative z-10" @close="closeModal">
        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity">
          </div>
        </TransitionChild>
  
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel class="relative transform overflow-hidden rounded-2xl bg-white/75 text-left shadow-xl transition-all min-h-96 sm:my-8 sm:w-full sm:max-w-md">
                <div class="bg-white min-h-96 px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                  <div class="">
                    <!-- <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                      <ExclamationTriangleIcon class="h-6 w-6 text-red-600" aria-hidden="true" />
                    </div> -->
                    <div class="mt-3 text-center sm:mt-0 sm:text-left">
                      <!-- <DialogTitle as="h3" class="text-xl font-dela font-normal leading-6 bg-cyan-300 text-white/95 w-52 py-2 text-center mx-auto tracking-tight">Scan to Pay</DialogTitle>
                      <div class="w-full min-h-20 flex flex-col items-center justify-center">
                        <p class="text-sm text-gray-500">-QR code here></p>                      
                      </div> -->
                      <slot />
                    </div>
                  </div>
                </div>
                
                <div class="bg-gray-50 px-4 py-3 flex items-center justify-center gap-2 sm:px-6"> 
                  <button type="button" class="inline-flex w-full justify-center rounded-md bg-lime-400 px-5 py-3 text-sm font-dela font-normal text-black shadow-sm hover:bg-cyan-400 hover:text-white transition-colors sm:ml-3 sm:w-auto" @click="openSuccess">Success</button> 
                  <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-5 py-3 text-sm font-dela font-normal text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="closeModal" ref="cancelButtonRef">Cancel</button>
                  <button type="button" class="inline-flex w-full justify-center rounded-md bg-red-500 px-5 py-3 text-sm font-dela font-normal text-white shadow-sm hover:bg-zinc-200 hover:text-black transition-colors  sm:w-auto" @click="openFail">Fail</button> 
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
    <PaySuccess ref="success">
      <p class="text-normal font-dela text-black">Thank you for using Paytaca</p>          
      <small class="font-space text-gray-500">Dropping your item in just a bit...</small> 
    </PaySuccess>
    <PayError ref="fail">
      <div class="mt-3 text-center sm:mt-0 sm:text-left">
          <DialogTitle as="h3" class="text-xl font-dela font-normal leading-6 bg-[#ff5151] text-white w-52 p-3 text-center mx-auto tracking-normal">
            Error!
          </DialogTitle>
          <div class="w-full min-h-80 flex flex-col items-center justify-between">  
              <div class="mt-20">
                  <img :src="PaytacaLogo" class="h-24 w-auto" alt="" loading="lazy">
                  <ExclamationTriangleIcon class="absolute right-44 top-48  h-10 text-[#ff5151] mt-10 " aria-hidden="true" />
              </div>
              <div class="text-center mb-3">
                <p class="text-normal font-dela text-black">Transaction Failed</p>          
                <small class="font-space text-gray-500">Please try again</small> 
              </div>              
          </div>
      </div>
    </PayError>
</template>
  
