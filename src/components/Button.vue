<template>
	<button class="bg-blue-600 hover:bg-blue-900 text-white font-bold rounded-xl drop-shadow-md">
		<slot/>
	</button>
</template>

<script>
export default {

  name: 'Button',

  data () {
    return {

    }
  }
}
</script>

<style lang="css" scoped>
</style>