<script>
  import AdminNav from "$lib/components/AdminNav.svelte";
  import { MainScreen } from "$lib/Assets.js";
  import { fetch_all } from "$lib/Bill.js";
  import { Pc, getPcByID } from "$lib/Pc.js";
  import { onMount } from "svelte";
  import ModalBill from "$lib/components/ModalBill.svelte"
  let bill_list = [];
  let item_pc = new Pc();
  let input_bill_id;
  let input_date = "";
  let status = "close";
  let bill_id;
  let updatable;

  // pop up
  function close(event) {
    if (event.key === "Escape") {
      status = "close";
    }
  }
  function openModal(billID, update_type) {
    console.log("id of selected bill: ", billID);
    status = "open";
    bill_id = billID;
    updatable = update_type
  }

  onMount(async () => {
    bill_list = await fetch_all().then((res) => res);
    console.log(bill_list)
  });

  async function UpdateBill() {
    bill_list = await fetch_all(input_bill_id);
    if (input_date != "") {
      const refort_date = new Date(input_date);
      const year = refort_date.getFullYear();
      const month = ("0" + (refort_date.getMonth() + 1)).slice(-2);
      const day = ("0" + refort_date.getDate()).slice(-2);

      bill_list = await fetch_all(input_bill_id, day, month, year);
    }
  }

  async function validate(str, pc_id, bill_ID) {
    item_pc = await getPcByID(pc_id).then(res => res);
    console.log(str)
    if (str !== undefined && str !== null && str !== "") {
      console.log(str, bill_ID, 0)
      return 0;
    } else {
      const d1 = new Date(item_pc.EndTime)
      const d2 = new Date(  )
      console.log(d1 <= d2)
      if (d1 <= d2) {
        // console.log(str, bill_ID, 1)
        console.log(item_pc)
        return 1;
      }
      console.log(str, bill_ID, 2)
      console.log(2)
      return 2;
    }
  }

  function cur() {
    const now = new Date();
    return now.toLocaleString('vi-VI')
  }

  function refort(str) {
    if (str == undefined){
      return 'None'
    }
    const originalDate = new Date(str);
    return originalDate.toLocaleString('vi-VI');
  }
</script>

<div
  id="bg"
  class="flex flex-row h-screen bg-cover font-BlackOpsOne"
  style="background-image: url({MainScreen['Background4']});"
>
  <div class="flex flex-col">
    <AdminNav />
  </div>
  <div class="flex-col flex h-full w-full mx-10">
    <div
      class="h-[70px] font-BlackOpsOne text-xl text-purple-300 justify-start items-center flex flex-row my-2"
    >
      <input
        type="number"
        min="0"
        placeholder="Bill ID"
        class="px-5 h-[50px] rounded-3xl bg-purple-900"
        bind:value={input_bill_id}
        on:change={UpdateBill}
      />
      <p class="px-5">Pick Date:</p>
      <input
        type="date"
        bind:value={input_date}
        on:change={UpdateBill}
        class="bg-purple-900"
      />
    </div>
    <div class="flex-col h-full mb-10">
      <div class="grid grid-flow-col grid-cols-2 gap-5">
        <div id="bo" class="overflow-y-scroll no-scrollbar">
          <ul class="grid grid-flow-row grid-cols-3 m-7 gap-5 text-white">
            {#each bill_list as valid}
              {#await validate(valid.Datetime, valid.PcID, valid.BillID)}
                asd
              {:then res} 
                {#if res === 1 || res === 2}
                  <li
                    class="text-center justify-center items-center"
                  >
                    <!-- svelte-ignore a11y-interactive-supports-focus -->
                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                    <div
                      id="bi"
                      class="grid grid-flow-row auto-rows-max"
                      role="button"
                      on:click={openModal(valid.BillID, res === 1? true: false)}
                    >
                      <img
                        src={res === 1? MainScreen["RedForm"]: MainScreen["GreenForm"]}
                        alt="screen"
                      />
                      <div class="justify-center">{valid.BillID}</div>
                      <div class="justify-center">{refort(valid.Datetime)}</div>
                    </div>
                  </li>
                {/if}
              {/await}
            {/each}
          </ul>
        </div>
        <div id="bo" class="overflow-y-scroll no-scrollbar">
          <ul class="grid grid-flow-row grid-cols-3 m-7 gap-5 text-white">
            {#each bill_list as valid}
              {#await validate(valid.Datetime, valid.PcID, valid.BillID)}
                asd
              {:then res}
                {#if res === 0}
                  <li
                    class="text-center justify-center items-center font-medium"
                  >
                    <!-- svelte-ignore a11y-interactive-supports-focus -->
                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                    <div
                      id="bi"
                      class="grid grid-flow-row auto-rows-max"
                      role="button"
                      on:click={openModal(valid.BillID, false)}
                    >
                      <img src={MainScreen["RedForm"]} alt="screen" />
                      <div class="justify-center text-sm">{valid.BillID}</div>
                      <div class="justify-center text-sm">{refort(valid.Datetime)}</div>
                    </div>
                  </li>
                {/if}
              {/await}
            {/each}
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<div on:keydown={close}>
  <ModalBill {status} {bill_id} {updatable} on:keydown={close} />
</div>

<style>
  #bi {
    width: 170px;
    height: 200px;
  }
  #bo {
    width: 700px;
    height: 800px;
    border-radius: 20px;
    background-color: rgba(62, 26, 90, 0.8);
  }
</style>
