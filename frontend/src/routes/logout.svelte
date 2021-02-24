<script>
  import { onMount } from "svelte";
  import { logout } from "../utils/auth";

  onMount(async () => {
    await logout();
  });
</script>
