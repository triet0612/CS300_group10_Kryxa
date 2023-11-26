<script>
  import { AppLogo } from "$lib/Assets.js";
  import { Bill, fetch_all } from "$lib/Bill.js";
  import { onMount } from "svelte";

  export let status = "close";
  export let bill_id;

  //     let bills = [
  //     { id: 1, name: "com chien duong chau", qt: 2, price: 20000, amount: 40000 },
  //     { id: 2, name: "com chien ga", qt: 1, price: 20000, amount: 20000 },
  //     { id: 3, name: "Mi 2 trung", qt: 3, price: 10000, amount: 30000 },
  //   ];

  let bill_info = [];
  let formattedDateString = "newTime";
  let mybill;
  // onMount(async () => {
  //   bill_id = 1;
  //   bill_info = await fetch_all(bill_id).then((res)=>res);
  //   console.log(bill_info[0])
  //   const dateTimeArray = bill_info[0].Datetime.split("T");
  //   const dateArray = dateTimeArray[0].split("-");
  //   newTime =
  //     dateArray[2] +
  //     "/" +
  //     dateArray[1] +
  //     "/" +
  //     dateArray[0] +
  //     "  " +
  //     dateTimeArray[1];
  // });
  async function fetchbills(bill_id) {
    try {
      console.log("billID", bill_id);
      bill_info = await fetch_all(bill_id);
      console.log("bill_info", bill_info); // Log the bill_info array
      console.log("bill_info[0]", bill_info[0]); // Log the first element of the array
    } catch (error) {
      console.error("Error fetching bills:", error);
    }
    // mybill = await getBillbyID(1).then((res) => res);
    // console.log(mybill);
    // console.log(bill_id);
    bill_info = await fetch_all(bill_id).then((res) => res);
    // console.log(bill_info[0]);
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
                    : 'bg-slate-200'}"
                >
                  <td class="w-[250px] pl-2">{item["name"]}</td><td
                    class="w-[50px]">{item["qt"]}</td
                  ><td class="w-[60px]">{item["price"]}</td><td
                    class="w-[90px] text-right pr-2"
                    >{item["amount"] * item["price"]}</td
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
              >Complete</button
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
