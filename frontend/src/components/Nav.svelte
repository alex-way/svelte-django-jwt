<script>
  export let segment;

  import { user } from "../stores/auth";
</script>

<nav class="navbar navbar-expand-lg navbar-light alt-font border-bottom">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">Demo</a>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon" />
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a
            class:active={segment === undefined}
            class="nav-link"
            aria-current="page"
            href="/">Home</a
          >
        </li>
        <li class="nav-item">
          <a class:active={segment === "start"} class="nav-link" href="/start/"
            >Get Started</a
          >
        </li>
      </ul>
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          {#if $user.loggedIn}
            <a class="nav-link" href="/logout/">Logout</a>
          {:else}
            <a
              class:active={segment === "login"}
              class="nav-link"
              href="/login/">Login</a
            >
          {/if}
        </li>
      </ul>
    </div>
  </div>
</nav>
