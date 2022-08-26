<template>
	<button class="bg-red-600 hover:bg-red-900 text-white font-bold rounded-xl drop-shadow-md">
		<slot/>
	</button>
</template>

<script>
export default {

  name: 'ButtonDanger',

  data () {
    return {

    }
  }
}
</script>