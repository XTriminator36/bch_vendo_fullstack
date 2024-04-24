<script setup>
  import {RouterView} from 'vue-router'
  import {ref, onMounted} from 'vue'
  import PayOffline from './components/PayError.vue';
  import { DialogTitle } from '@headlessui/vue';
  import { ExclamationTriangleIcon } from '@heroicons/vue/24/outline';

  const offlineModal = ref(null);
  // Check if the browser is offline on component mount
  onMounted(() => {
    if (!navigator.onLine) {
      openOfflineModal();
    }
  });
  // Function to open the offline modal
  const openOfflineModal = () => {
    if (offlineModal.value) {
      offlineModal.value.openFail();
    }
  };
</script>

<template>
  <main class="m-0 p-0 background_1">
    
    <RouterView />
    <PayOffline ref="offline">
      <div class="mt-3 text-center sm:mt-0 sm:text-left">
          <DialogTitle as="h3" class="text-xl font-dela font-normal leading-6 bg-[#ff5151] text-white w-52 p-3 text-center mx-auto tracking-normal">
            Offline
          </DialogTitle>
          <div class="w-full min-h-80 flex flex-col items-center justify-between">  
              <div class="mt-20">
                  <ExclamationTriangleIcon class="  h-24 text-[#ff5151] mt-10 " aria-hidden="true" />
              </div>
              <div class="text-center mb-3">
                <p class="text-normal font-dela text-black">Sorry, we're offline</p>          
                <small class="font-space text-gray-500">Waiting for internet connection to resume</small> 
              </div>              
          </div>
      </div>
    </PayOffline>
  </main>
  
</template>

<style >
  html{
    max-height: 1280px;
    max-width: 800px;
    /* overflow: hidden; */
  }

  .background_1{
    background-color: #ffffff;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='199' viewBox='0 0 100 199'%3E%3Cg fill='%23ccfbf1' fill-opacity='0.73'%3E%3Cpath d='M0 199V0h1v1.99L100 199h-1.12L1 4.22V199H0zM100 2h-.12l-1-2H100v2z'%3E%3C/path%3E%3C/g%3E%3C/svg%3E");
  }
</style>
