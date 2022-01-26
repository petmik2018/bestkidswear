<template>


</template>

<script>

import { toast } from 'bulma-toast'

export default {
	name: 'Utils',
	props: {
		makeTestToast: Function
	},
	methods: {
		makeTestToast(message) {
			console.log(message)
			toast({
				message: message,
				type: 'is-success',
				dismissible: true,
				pauseOnHover: true,
				duration: 2000,
				position: 'bottom-right',
			})			
		},

	},
}

</script>