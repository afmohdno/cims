<template>
	<Modal v-if="showModal" @close="toggleModal" @confirm="confirmDelete(toDelete)" >
		<template v-slot>
			<div class="text-gray-700">
				<p>Name: {{modalHelper['name']}}</p>
				<p>Email: {{modalHelper['email']}}</p>
			</div>
		</template>
	</Modal>
  <ContentLayout>
  	<div class="flex justify-between items-center">
  		<div>
  			<h1>Customers</h1>
  		</div>
  		<div class="text-right">
  			<router-link to="/c/new" custom v-slot="{ navigate }">
  				<Button @click="navigate" class="px-3 py-2">Add customer</Button>
  			</router-link>
  		</div>
  	</div>
  	<div v-if="customers.length" class="overflow-x-scroll">
	  	<table class="w-full mt-4 table-auto border rounded-full border-collapse rounded">
	  		<thead>
	  			<tr>
	  				<th class="text-center p-4" v-for="(value,key) in customers[0]">{{key}}</th>
	  				<th class="text-center p-4">Action</th>
	  			</tr>
	  		</thead>

	  		<tbody>
					<template v-for="customer, index in customers" :key="customer[index]">
	  				<tr :id="customer['_id']">
	  					<td class="text-center p-4">
	  						<router-link :to="{ name: 'customer', params: { id: customer['_id'] } }" class="text-white font-bold">{{customer['_id']}}</router-link>
	  					</td>
	  					<td class="text-center p-4">
	  						<router-link :to="{ name: 'customer', params: { id: customer['_id'] } }" class="text-white font-bold">{{customer.name}}</router-link>
	  					</td>
	  					<td class="text-center p-4">{{customer.email}}</td>
	  					<td class="text-center p-4">{{customer.city}}</td>
	  					<td class="text-center p-4">{{customer.age}}</td>
	  					<td class="text-center p-4">
	  						<div>
	  							<ButtonDanger class="px-3 py-1" @click="toggleModal(customer)">Delete</ButtonDanger>
	  						</div>
	  					</td>
	  				</tr>
	  			</template>
	  		</tbody>
	  	</table>
  	</div>
  	<div v-else>
  		<p class="text-center">Fetching data...</p>
  	</div>
  </ContentLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ContentLayout from '../components/ContentLayout.vue'
import Modal from '../components/Modal.vue'
import Button from '../components/Button.vue'
import ButtonDanger from '../components/ButtonDanger.vue'

const customers = ref([])
const showModal = ref(false)
const toDelete = ref('')
const modalHelper = ref({})

onMounted(async () => {
	await axios.get("http://localhost:5000/customers")
	.then(response => {
		customers.value = response.data
	})
	.catch(err => {
		console.log(err)
	})
})

const toggleModal = (customer) => {
	console.log(customer)
	showModal.value = !showModal.value
	modalHelper.value = customer
	toDelete.value = customer['_id']
}

const confirmDelete = async(customer_id) => {
	const path = `http://localhost:5000/customer/${customer_id}`
	await axios.delete(path)
	.then(response => {
		if (response.data.status == 'success') {
			const row = document.getElementById(customer_id)
			row.style.display = "none"
			showModal.value = false
		}
	})
	.catch(err => {
		console.log(err)
	})
}
</script>
