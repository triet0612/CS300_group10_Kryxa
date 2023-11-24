<script>
  import AdminNav from "$lib/components/AdminNav.svelte";
  import { MainScreen } from "$lib/Assets.js";
  import ModalBill from "$lib/components/ModalBill.svelte";
  import { Bill } from "$lib/Bill.js";
  import { onMount } from "svelte";

  let status = "close";
  // pop up
  function close(event) {
    if (event.key === "Escape")
      status = "close";
    }
  }
  function openModal(event) {
    status = "open";
  }
</script>

<div
  id="bg"
  class=" fixed h-full w-full bg-cover {status === 'open' ? 'blur-3xl' : ''} "
  style="background-image: url({MainScreen['Background2']});"
>
  <!-- Nav Bar -->
  <div class="fixed">
    <AdminNav />
  </div>
  <!-- View Page -->
  <div class="mr-auto ml-auto flex flex-col" />

  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-interactive-supports-focus -->
  <div class="h-40 w-40 pt-5 ml-64 bg-white" role="button" on:click={openModal}>
    <img src={MainScreen["addPc"]} alt="screen" />
  </div>
</div>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<div on:keydown={close}>
  <ModalBill {status} on:keydown={close} />
</div>
