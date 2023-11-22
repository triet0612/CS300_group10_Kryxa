<script>
  import AdminNav from "$lib/components/AdminNav.svelte";
  import { MainScreen } from "$lib/Assets.js";
  import { Bill, fetch_all } from "$lib/Bill.js";
  import { onMount } from "svelte";
  let pc_list = [];
  onMount(async () => {
    bill_list = await fetch_all().then((res) => res);
    console.log(bill_list);
  });
</script>

<!-- <div class="flex flex-row h-screen bg-gradient-to-b from-black to-[#352900]"> -->
<div
  id="bg"
  class="flex flex-row h-screen bg-cover"
  style="background-image: url({MainScreen['Background4']});"
>
  <div class="flex flex-col ">
    <AdminNav />
  </div>
  <div class="flex-col flex h-screen w-auto text-white">
    <div class="flex-col">p</div>
    <div class="flex-col flex">
      <div class="grid grid-flow-col grid-cols-2 gap-5">
        <div id="boxed" class="box-content border-2">p</div>
        <div id="boxed" class="box-content border-2">p</div>
      </div>
    </div>
  </div>
</div>
  
<style>
  #boxed{
    width: 700px;
    height: 800px;
    border-radius: 20px;
  }
</style>

