
<script setup>
import { ref, onMounted, watch } from 'vue';
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue';
import BaseModal from './BaseModal.vue';
import axios from 'axios' //imports the axios api 
import { VQrcode, RenderOptions, ErrorCorrectLevel } from 'qrcode-vuejs';
// import { CheckCircleIcon } from '@heroicons/vue/24/solid';
// import PaytacaLogo from './icons/paytaca_logo.png';

const open = ref(false)
const scan = ref(null)
const props = defineProps({
  arrayPurchase : {
    type: null,
    required: true,
  }
})
const myArray = ref(null)
var qrGenerated = ref([])
const qrText = ref(null)
const newVal = ref(null)
const qrTextValue = ref(null)


// fetches the wallet address and displays it in a form of qr code with the bch amount included
const fetchQR = async() => {
    return new Promise((resolve, reject) => {
        axios.get('http://127.0.0.1:8080/api/wallet-address') //wallet address api
            .then( async response => {
                console.log(response.data);
                const cashAddress = response.data;
                qrTextValue.value = qrText.value = JSON.stringify(cashAddress[0].cash_address).replace(/"/g, '');

                // qrText.value = qrTextValue + "?amount=" + "0.00001"; //product price value should be passed here depending on the product chosen in the store.vue
                // resolve(response.data);
                watch(() => props.arrayPurchase, (newValue) => {
                    myArray.value = {...newValue} // Copy the props array to myArray
                });
                
                watch(() => myArray.value, (newValue) => {
                  // if (newValue.length > 0) {
                    
                    // newVal.value = newValue.product_code
                    // qrGenerated.value.push(newValue[0]) 
                    // qrGenerated.value.push(newValue[0]) // Accessing the id property of the first item in myArray
                    // qrText.value = JSON.stringify(newValue)
                    qrText.value = qrTextValue.value + '?amount=' + newValue.bch_current;
                    console.log(qrText)
                  // }
                });

                
            })
            .catch(error => {
                // Display an error message if failed to fetch
                console.error('Error fetching items:', error);
                reject(error);
            });
    });
};


onMounted( () => {
  // const myArray = ref([])
  // myArray = props.arrayPurchase;
  fetchQR()
});
// const qrGenerated = (myArray.id+myArray.product_code+myArray.product_quantity)

const closeProd =  function() {
    open.value = false
    // emit('closeEmit')
}
const openProd = function() {
    open.value = true
    // console.log(arrayPurchase.value)
}


const openModal = () => {
    scan.value.openModal()
    open.value = false
    // emit('closeEmit')
    // closeProd()
}
const isLoading = ref(false)

// defineEmits(['close']);
const emit = defineEmits(['closeEmit', 0], ['purchaseEmit', ])

defineExpose({
  openProd,
  closeProd
})
</script>

<template>
    <TransitionRoot appear :show="open" as="template" >
      <Dialog as="div" class="relative z-10" @close="closeProd">
        <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity">
          </div>
        </TransitionChild>
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel class="relative transform overflow-hidden rounded-2xl bg-white/75 text-left shadow-xl transition-all min-h-96  sm:my-8 sm:w-full sm:max-w-md">
                <!-- <div class="bg-white min-h-96 px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                  <div class="">
                    
                    <div class="mt-3 text-center sm:mt-0 sm:text-left">
                        <slot />
                    </div>
                  </div>
                </div>         -->
                <!-- <div class="bg-gray-50 px-4 pb-3 content-center justify-items-center sm:px-6"> 
                  <div class=" grid gird-rows-2 grid-flow-col"> 
                    <button type="button" class="mt-3 w-full justify-center rounded-md bg-white px-5 py-3 text-md font-dela font-normal text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="closeProd" ref="cancelButtonRef">Cancel</button>
                    <button type="button" class="ml-3 mt-3 w-full justify-center rounded-md bg-[#53A0FB] px-5 py-3 text-md font-dela font-normal text-white shadow-sm  hover:bg-lime-300 hover:text-black sm:mt-0 sm:w-auto transition-colors"  @click="openModal" >Purchase</button>
                  </div>
                </div> -->
                <slot />
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
    

</template>
  
