<script>
  import AdminNav from "$lib/components/AdminNav.svelte";
  import ModalPc from "$lib/components/ModalPc.svelte";
  import { MainScreen } from "$lib/Assets.js";
  import { Pc, get_Pcs } from "$lib/Pc.js";
  import { onMount } from "svelte";
  let pc_list = [];
  onMount(async () => {
    pc_list = await get_Pcs().then((res) => res);
    console.log(pc_list);
  });
  // let pc_list = [
  //   { PcID: 1, Status: "Unavailable" },
  //   { PcID: 2, Status: "Available" },
  //   { PcID: 3, Status: "Available" },
  //   { PcID: 4, Status: "Available" },
  //   { PcID: 5, Status: "Maintainance" },
  //   { PcID: 6, Status: "Maintainance" },
  //   { PcID: 7, Status: "Maintainance" },
  //   { PcID: 8, Status: "Maintainance" },
  //   { PcID: 9, Status: "Maintainance" },
  //   { PcID: 10, Status: "Maintainance" },
  //   { PcID: 11, Status: "Maintainance" },
  //   { PcID: 12, Status: "Maintainance" },
  //   { PcID: 13, Status: "Maintainance" },
  //   { PcID: 14, Status: "Maintainance" },
  // ];
  let status = "close";
  function close(event) {
    if (event.key === "Escape") {
      status = "close";
    }
  }
</script>

<!-- <div class="flex flex-row h-screen bg-gradient-to-b from-black to-[#352900]"> -->
<div
  id="bg"
  class="flex flex-row h-screen bg-cover"
  style="background-image: url({MainScreen['Background2']});"
>
  <div class="flex flex-col">
    <AdminNav />
  </div>
  <div class="mr-auto ml-auto p-20 overflow-y-scroll">
    <ul class="grid grid-cols-5 gap-20">
      <div
        class="w-50 h-50 bg-yellow-400 bg-opacity-70 backdrop-blur-2xl backdrop-brightness-200 text-black-400 font-NotoSans font-bold text-center flex flex-col rounded-xl justify-center"
      >
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-interactive-supports-focus -->
        <div
          class="h-fit pt-5 px-5"
          role="button"
          on:click={() => {
            status = "open";
          }}
        >
          <img src={MainScreen["addPc"]} alt="screen" />
        </div>
        <div class="mb-6">Add Pc</div>
      </div>
      {#each pc_list as pc_id}
        <li>
          <a href="/admin/{pc_id['PcID']}">
            <div
              class="w-50 h-50 {pc_id['Status'] == 'Available'
                ? 'bg-green-600 bg-opacity-75'
                : pc_id['Status'] == 'Unavailable'
                ? 'bg-red-600 bg-opacity-75'
                : 'bg-white  bg-opacity-25'}
              backdrop-blur-2xl backdrop-brightness-200 text-black font-semibold font-NotoSans text-center flex flex-col rounded-xl justify-center"
            >
              <div class="h-fit pt-5 px-5">
                <img
                  src={MainScreen["pc_screen"]}
                  alt="screen"
                  class="bg-contain"
                />
              </div>

              <div class="mb-6">Computer {pc_id.PcID}</div>
            </div>
          </a>
        </li>
      {/each}
    </ul>
  </div>
</div>

<!-- <style>
  #bg{
    display: flex; 
  flex-direction: row; 
  height: 100vh; 
  background-size: cover; 
  }
</style> -->

<!-- svelte-ignore a11y-no-static-element-interactions -->
<div on:keydown={close}>
  <ModalPc {status} on:keydown={close} />
</div>
