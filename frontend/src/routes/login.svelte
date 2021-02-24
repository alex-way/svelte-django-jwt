<script>
  import { login } from "../utils/auth";
  let username;
  let password;
  import { goto } from "@sapper/app";

  const handleForm = async () => {
    await login(username, password).then((success) => {
      if (success) {
        goto("/start/");
      }
    });
  };
</script>

<svelte:head>
  <title>Sapper project template</title>
</svelte:head>

<h1 class="bg-primary text-white p-3 ps-5 alt-font mb-5">Login</h1>

<form on:submit|preventDefault={handleForm}>
  <div class="mb-3">
    <label for="usernameInput" class="form-label">Username</label>
    <input
      bind:value={username}
      type="text"
      class="form-control"
      id="usernameInput"
      aria-describedby="usernameHelp"
    />
    <div id="usernameHelp" class="form-text">
      This is usually in the form of: last name, followed by the first letter of
      your first name.
    </div>
  </div>
  <div class="mb-3">
    <label for="passwordInput" class="form-label">Password</label>
    <input
      bind:value={password}
      type="password"
      class="form-control"
      id="passwordInput"
    />
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
