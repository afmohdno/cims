<template>
	<nav class="bg-slate-300">
		<div class="container flex items-center justify-between py-4 px-3 mx-auto text-[#0c7bc0] font-bold">
			<div>
				<router-link :to="{ name: 'home'}" class="hover:text-[#49a6dc] px-3 py-2">AFFIN HWANG</router-link>
			</div>
			<div>
				<a class="hover:text-[#49a6dc]" href="">Staff Login</a>
			</div>
		</div>
	</nav>
</template>

<script>
export default {

  name: 'Navbar',

  data () {
    return {

    }
  }
}
</script>

<style lang="css" scoped>
</style>