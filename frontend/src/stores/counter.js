// import { ref, computed } from 'vue'
// import { defineStore } from 'pinia'

// export const useCounterStore = defineStore('counter', () => {
//   const count = ref(0)
//   const doubleCount = computed(() => count.value * 2)
//   function increment() {
//     count.value++
//   }

//   return { count, doubleCount, increment }
// })
import axios from 'axios' //imports the axios api 
import { defineStore } from 'pinia'

export const useCounterStore = defineStore( 'counter', {
    id: 'data',
    state: () => ({
      responseData: null,
      loading: false,
      error: null,
      submittedData: null,
      qrcodeObj: null,
    }),
    actions: {
      async fetchData() {
        this.loading = true;
        try {
          const response = await axios.get('http://127.0.0.1:8080/api/ProductItems');
          this.responseData = response.data;
          console.log(this.responseData)
        } catch (error) {
          this.error = error.message;
        } finally {
          this.loading = false;
        }
      },
    },
    mutations: {
      setSubmittedData(data) {
        this.submittedData = data;
      },
    },
  });