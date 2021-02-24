<script>
  import DemoComp from "../components/DemoComp.svelte";
  import { user } from "../stores/auth";
</script>

<h1>Hey {$user.loggedIn ? $user.username : "there"} 👋</h1>

<DemoComp />
