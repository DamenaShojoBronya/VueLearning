<template>
	<div id="app">

		<!--顶部导航栏菜单-->
		<header-component></header-component>
		<router-view />
		<PageFooter />
	</div>
</template>
  
<script>
import HeaderComponent from "@/components/HeaderComponent";
import PageFooter from './components/PageFooter.vue';

export default {
	name: 'App',
	components: {
		HeaderComponent,
		PageFooter
	}
};

</script>
  
<style>
#app{
	display: flex;
	flex-wrap: wrap;
	align-items: center;
	justify-content: center;
	width: 100%;
	height: 100%;
	/*background-color: red;*/
	
}
</style>
  