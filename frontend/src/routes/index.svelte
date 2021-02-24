<script>
  import { user } from "../stores/auth";
</script>

<svelte:head>
  <title>Demo</title>
</svelte:head>

<h1>Hey {$user.loggedIn ? $user.username : "there"} 👋</h1>
