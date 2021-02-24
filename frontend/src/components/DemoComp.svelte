<script>
  import { onMount } from "svelte";
  import { fly } from "svelte/transition";
  import Select from "svelte-select";
  import axios from "axios";
  let items = [];

  onMount(async () => {
    await axios.get("/api/examples/").then((response) => {
      items = response.data.map((item) => ({
        label: item.name,
        value: item.id,
      }));
    });
  });

  const groupBy = (item) => item.group;

  let selectedItems;

  function handleSelect(event) {
    selectedItems = event.detail || [];
  }
</script>

<form in:fly={{ x: 200, duration: 500 }}>
  <Select {items} {groupBy} isMulti={true} on:select={handleSelect} />
</form>
