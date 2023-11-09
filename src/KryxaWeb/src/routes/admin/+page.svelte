<script>
    import AdminNav from "$lib/components/AdminNav.svelte";
    import ModalPc from "$lib/components/ModalPc.svelte"
    import { MainScreen } from "$lib/Assets.js";
    let pc_ids = [
      { PcID: 1, Status: "Unavailable" },
      { PcID: 2, Status: "Available" },
      { PcID: 3, Status: "Available" },
      { PcID: 4, Status: "Available" },
      { PcID: 5, Status: "Maintainance" },
      { PcID: 6, Status: "Maintainance" },
      { PcID: 7, Status: "Maintainance" },
      { PcID: 8, Status: "Maintainance" },
      { PcID: 9, Status: "Maintainance" },
      { PcID: 10, Status: "Maintainance" },
      { PcID: 11, Status: "Maintainance" },
      { PcID: 12, Status: "Maintainance" },
      { PcID: 13, Status: "Maintainance" },
      { PcID: 14, Status: "Maintainance" },
    ];
    let status = "close";
    function close(event) {
      if (event.key === "Escape") {
        status = "close"
      }
    }
</script>

<div id="bg"
class="flex flex-row h-screen bg-cover"
style="background-image: url({MainScreen['Background2']});">
  <div class="flex flex-col">
    <AdminNav />
  </div>
  <div class="mr-auto ml-auto p-20 overflow-y-scroll">
    <ul class="grid grid-cols-5 gap-20">
      <div
        class="w-56 h-56 bg-yellow-400 bg-opacity-70 backdrop-blur-2xl backdrop-brightness-200 text-black-400 font-NotoSans font-bold text-center flex flex-col rounded-xl justify-center"
      >
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-interactive-supports-focus -->
        <div class="h-fit pt-5 px-5" role="button" on:click={() => {status = "open"}}>
          <img src={MainScreen["addPc"]} alt="screen"/>
        </div>
        <div class="mb-6">Add Pc</div>
      </div>
      {#each pc_ids as pc_id}
        <li>
          <div
            class="w-56 h-56 {pc_id['Status'] == 'Available'
              ? 'bg-green-600 bg-opacity-75'
              : pc_id['Status'] == 'Unavailable'
              ? 'bg-red-900 bg-opacity-75'
              : 'bg-white  bg-opacity-25'}
              backdrop-blur-2xl backdrop-brightness-200 text-yellow-400 font-NotoSans text-center flex flex-col rounded-xl justify-center"
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
        </li>
      {/each}
    </ul>
  </div>
</div>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<div on:keydown={close}>
  <ModalPc status={status} on:keydown={close}/>
</div>
