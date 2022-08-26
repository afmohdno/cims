<template>
	<ContentLayout>
		<div class="flex justify-between items-center">
			<div>
				<router-link :to="{ name: 'home' }">Back</router-link>
			</div>
			<div class="text-right" v-show="pageMode == 'edit'">
				<Button class="px-3 py-2" @click="inputMode = true">Edit</Button>
			</div>
		</div>
		<div v-if="responseMessage" class="w-full mt-2 rounded p-2 text-white" :class="{ 'bg-green-500': responseFlag == 'success', 'bg-red-500': responseFlag == 'failed' }">
			<p>{{responseMessage}}</p>
		</div>
		<form @submit.prevent="sendForm">
			<table class="w-full mt-4 table-auto border rounded-full border-collapse rounded">
				<tbody>
					<template v-if="customer">
						<tr v-for="(value, key) in customer">
							<th class="px-3 py-2 text-left">{{key}}</th>
							<td class="px-3 py-2">

								<template v-if="key != '_id'">
									<span v-show="!inputMode">{{value}}</span>
									
									<template v-if="key == 'age'">
										<input type="number" v-model="customer[key]" v-show="inputMode" class="px-1 rounded text-gray-700 bg-slate-200 w-full" autocomplete="off" required>
									</template>
									<template v-else-if="key == 'email'">
										<input type="email" v-model="customer[key]" v-show="inputMode" class="px-1 rounded text-gray-700 bg-slate-200 w-full" autocomplete="off" required>
									</template>
									<template v-else>
										<input type="text" v-model="customer[key]" v-show="inputMode" class="px-1 rounded text-gray-700 bg-slate-200 w-full" autocomplete="off" required>
									</template>

								</template>

								<template v-else>
									<span>{{value}}</span>
								</template>
							</td>
						</tr>
					</template>
				</tbody>
			</table>

			<div class="mt-4 text-right" v-if="inputMode">
				<ButtonDanger v-show="pageMode == 'edit'" class="px-3 py-2">Update</ButtonDanger>
				<Button v-show="pageMode == 'add'" class="px-3 py-2">Add</Button>
			</div>
		</form>
	</ContentLayout>
	<!-- <div class="w-2/3 mx-auto">
		<p>see magic happening:</p>
		<p>{{customer}}</p>
	</div> -->
</template>

<script setup>
import { ref, onMounted, defineProps } from 'vue'
import axios from 'axios'
import ContentLayout from '../components/ContentLayout.vue'
import Button from '../components/Button.vue'
import ButtonDanger from '../components/ButtonDanger.vue'

const props = defineProps(['id'])
const customer = ref({})
const inputMode = ref(false)
const responseMessage = ref('')
const responseFlag = ref('')
const pageMode = ref('')

console.log(props.id)

if (props.id == 'new') {
		customer.value.name = ''
		customer.value.email = ''
		customer.value.city = ''
		customer.value.age = ''
		pageMode.value = 'add'
	inputMode.value = true
} else {
	pageMode.value = 'edit'
	onMounted(async () => {
		const path = `http://localhost:5000/customer/${props.id}`
		await axios.get(path)
		.then(response => {
			customer.value = response.data
		})
	})
}
const sendForm = async() => {
	const payload = {
		"name": customer.value.name,
		"email": customer.value.email,
		"city": customer.value.city,
		"age": customer.value.age
	}
	console.log(pageMode.value)
	if (pageMode.value == 'edit') {
		console.log(payload)
		const path = `http://localhost:5000/customer/${props.id}`
		await axios.put(path,payload)
		.then(response => {
			console.log(response.data.status)
			responseFlag.value = response.data.status
			responseMessage.value = response.data.message
			if (response.data.status == 'success') {
				inputMode.value = false
			}
		})
	} else if (pageMode.value == 'add') {
		console.log(payload)
		const path = 'http://localhost:5000/customer'
		await axios.post(path,payload)
		.then(response => {
			console.log(response.data.status)
			responseFlag.value = response.data.status
			responseMessage.value = response.data.message
			if (response.data.status == 'success') {
				inputMode.value = false
			}
		})
	}
}

</script>

<style lang="css" scoped>
</style>