<script>
  import Nav from "../components/Nav.svelte";
  import { refreshToken, logout } from "../utils/auth";
  import { onMount } from "svelte";

  export let segment;

  onMount(async () => {
    await refreshToken();
  });
</script>

<main>
  <Nav {segment} />
  <div class="container py-5">
    <slot />
  </div>
</main>

<style lang="scss" global>
  @import "../styles/global.scss";
</style>
