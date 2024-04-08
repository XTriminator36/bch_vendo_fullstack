<script setup>
import { ref,  defineExpose } from 'vue';
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue';
import { CheckCircleIcon } from '@heroicons/vue/24/solid';
import PaytacaLogo from './icons/paytaca_logo.png';


const open = ref(false)
  
const closeSuccess =  function() {
    open.value = false
}
const openSuccess = function() {
    open.value = true
}
  
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
              <DialogPanel class="relative transform overflow-hidden rounded-2xl bg-white/75 text-left shadow-xl transition-all min-h-96  sm:my-8 sm:w-full sm:max-w-md">
                <div class="bg-white min-h-96 px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                  <div class="">
                    <!-- <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                      <ExclamationTriangleIcon class="h-6 w-6 text-red-600" aria-hidden="true" />
                    </div> -->
                    <div class="mt-3 text-center sm:mt-0 sm:text-left">
                        <DialogTitle as="h3" class="text-xl font-dela font-normal leading-6 bg-[#C7FF51] text-black w-52 p-3 text-center mx-auto tracking-normal">
                          Successful!
                        </DialogTitle>
                        <div class="w-full min-h-80 flex flex-col items-center justify-between">  
                            <div class="mt-20">
                                <img :src="PaytacaLogo" class="h-24 w-auto" alt="" loading="lazy">
                                <CheckCircleIcon class="absolute right-44 top-48  h-10 text-green-600 mt-10 " aria-hidden="true" />
                            </div>
                            <div class="text-center mb-3">
                                <slot />
                            </div>              
                        </div>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 flex items-center justify-center sm:px-6"> 
                  <!-- <button type="button" class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto" @click="open = false">Deactivate</button>  -->
                  <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-5 py-3 text-sm font-dela font-normal text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="closeSuccess" ref="cancelButtonRef">Close</button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
</template>
  
