<template>
	<div class="bg-gray-800/50 fixed overflow-x-hidden overflow-y-auto inset-0 flex justify-center items-center z-10" @click.self="$emit('close')">
		<div class="relative h-1/3 w-1/3 mx-auto w-auto max-w-2xl">
			<div class="bg-white w-full h-full rounded-xl shadow-2xl flex flex-col p-4">
				<div class="text-center">
					<h2 class="text-xl block text-gray-800 mb-4">Confirm delete?</h2>
					<slot/>
				</div>
				<div class="mt-auto text-right">
					<Button class="px-2 py-1 mr-2" @click.self="$emit('close')">Cancel</Button>
					<ButtonDanger class="px-2 py-1" @click.self="$emit('confirm')">Confirm</ButtonDanger>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import ButtonDanger from '../components/ButtonDanger.vue'
import Button from '../components/Button.vue'

</script>


<style lang="css" scoped>
</style>