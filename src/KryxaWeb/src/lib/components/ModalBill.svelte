<script>
  import { AppLogo } from "$lib/Assets.js";
  import { Bill, fetch_all, update_bill } from "$lib/Bill.js";
  import { onMount } from "svelte";

  export let status = "close";
  export let bill_id;
  export let updatable = false;

  let bill_info = [];
  let formattedDateString = "newTime";

  async function fetchbills(bill_id) {
    try {
      bill_info = await fetch_all(bill_id);
      console.log("before update", bill_info[0]);
    } catch (error) {
      console.error("Error fetching bills:", error);
    }
    bill_info = await fetch_all(bill_id).then((res) => res);
    const originalDate = new Date(bill_info[0].Datetime);
    const year = originalDate.getFullYear();
    const month = ("0" + (originalDate.getMonth() + 1)).slice(-2); // Adding 1 because months are zero-based
    const day = ("0" + originalDate.getDate()).slice(-2);
    const hours = ("0" + originalDate.getHours()).slice(-2);
    const minutes = ("0" + originalDate.getMinutes()).slice(-2);
    const seconds = ("0" + originalDate.getSeconds()).slice(-2);
    formattedDateString = `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;
    console.log("formattedDateString", formattedDateString);
  }

  async function update_current_bill(bill_data) {
    if (updatable) {
      bill_data.Datetime = new Date().toISOString()
    }
    if (bill_data.Datetime !== undefined && bill_data.Datetime !== ""   && bill_data.Datetime !== null) {
      let statcode = await update_bill(bill_data).then((res) => res);
      if (statcode != 200) {
        console.log("failed to update bill");
      }
      console.log("after update", bill_data);
      location.reload();
    }
  }

  async function remove_item(item_id) {
    console.log("Removing item with ID:", item_id);
    bill_info[0].Cart = bill_info[0].Cart.filter((item) => item.id !== item_id);
    //Update bill's order
    bill_info[0].Cart.forEach((item, index) => {
      item.id = index + 1;
    });

    console.log("Updated Cart:", bill_info[0].Cart);
  }

  let dialog;

  $: if (status === "open" && dialog) {
    dialog.show();
  } else if (status === "close" && dialog) {
    dialog.close();
  }
</script>

{#await fetchbills(bill_id)}
  <p>Loading</p>
{:then}
  <div
    class="flex flex-col w-[520px] content-center justify-center items-center"
  >
    <dialog bind:this={dialog} id="mydialog">
      <div
        class="flex flex-col w-[500px] bg-white border-black border justify-center items-center"
      >
        <div
          id="title"
          class="w-[470px] font-extrabold text-5xl mt-9 text-center"
        >
          KRYXA
        </div>
        <div
          class="w-[470px] h-[160px] border-black border mt-2 mb-2 font-NotoSans inline-flex"
        >
          <div class="w-[250px] ml-1 mt-2">
            <div class="text-black font-semibold mt-2">
              BillID : {bill_info[0].BillID}
            </div>
            <div class="text-black font-semibold mt-2">
              PcID : {bill_info[0].PcID}
            </div>
            <div class="text-black font-semibold mt-2">
              Datetime : {formattedDateString}
            </div>
            <div class="inline-flex">
              <img src={AppLogo} alt="" width="20%" />
              <div class="mt-5 ml-2 text-gray-600">since 2023</div>
            </div>
          </div>
          <div class="w-[220px] mt-2">
            <div class="mr-5 mt-2 font-semibold text-right">Note :</div>
            <textarea
              class="w-[200px] h-[100px] border-black border resize-none"
              bind:value={bill_info[0].Note}
            ></textarea>
          </div>
        </div>
        <div class="w-[470px] mb-2">
          <table class="mx-auto">
            <thead class="font-bold">
              <tr class="h-[40px]">
                <td class="w-[250px] pl-2">Item description</td><td
                  class="w-[50px]">Qt</td
                ><td class="w-[60px]">Price</td><td
                  class="w-[90px] text-right pr-2">Amount</td
                >
              </tr>
            </thead>
            <tbody>
              {#each bill_info[0].Cart as item}
                <tr
                  class=" h-[40px] {item['id'] % 2 == 0
                    ? 'bg-white'
                    : 'bg-slate-200'} cursor-pointer transition-colors duration-300 hover:bg-red-500"
                  on:click={() => remove_item(item["id"])}
                  title="Click to remove"
                >
                  <td class="w-[250px] pl-2">{item["name"]}</td><td
                    class="w-[50px]">{item["qt"]}</td
                  ><td class="w-[60px]">{item["price"]}</td><td
                    class="w-[90px] text-right pr-2"
                    >{item["qt"] * item["price"]}</td
                  >
                </tr>
              {/each}
            </tbody>
          </table>
        </div>
        <div class="w-[470px] border-black border mt-4"></div>
        <div class="flex my-4">
          <div class="w-[235px] h-[40px">
            <button
              class="w-[200px] h-[40px] bg-[#FFC52F] font-bold mx-[10px] shadow-lg shadow-slate-400"
              on:click={update_current_bill(bill_info[0])}>Save</button
            >
          </div>
          <div class="w-[235px] h-[40px] text-center">
            <div
              class="w-[230px] h-[30px] text-white text-xl bg-green-600 font-bold mr-[20px] mt-[4px]"
            >
              Total : {bill_info[0].Total}
            </div>
          </div>
        </div>
      </div>
    </dialog>
  </div>
{/await}

<style>
  dialog {
    position: absolute;
    top: 33.3333%;
    padding: 0.5rem;
    background-color: #ffffff;
    align-items: center;
    border-color: black;
    border-width: 1pt;
  }

  #title {
    border-bottom: 2px solid black;
  }
</style>
