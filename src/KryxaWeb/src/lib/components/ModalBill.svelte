<script>
  import { AppLogo } from "$lib/Assets.js";
  import { Bill } from "$lib/Bill.js";

  let bill_info = new Bill();
  let newTime = "newTime";
  onMount(async () => {
    const urlSearchParams = new URLSearchParams(window.location.search).get(
      "bill_id"
    );
    console.log("Requested Bill ID: " + urlSearchParams);
    bill_info = await bill_info.getBillbyID(urlSearchParams).then((res) => res);

    const dateTimeArray = bill_info.Datetime.split("T");
    const dateArray = dateTimeArray[0].split("-");
    newTime =
      dateArray[2] +
      "/" +
      dateArray[1] +
      "/" +
      dateArray[0] +
      "  " +
      dateTimeArray[1];
  });

  export let status = "close";
  let dialog;

  $: if (status === "open" && dialog) {
    dialog.show();
  } else if (status === "close" && dialog) {
    dialog.close();
  }
</script>

<div class="flex flex-col w-[520px] content-center justify-center items-center">
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
          <div class="text-black font-semibold mt-2">BillID : 123</div>
          <div class="text-black font-semibold mt-2">PcID : 0</div>
          <div class="text-black font-semibold mt-2">
            Datetime : 12/11/2023 15:10:39
          </div>
          <div class="inline-flex">
            <img src={AppLogo} alt="" width="20%" />
            <div class="mt-5 ml-2 text-gray-600">since 2023</div>
          </div>
        </div>
        <div class="w-[220px] mt-2">
          <div class="mr-5 mt-2 font-semibold text-right">Note :</div>
          <textarea class="w-[200px] h-[100px] border-black border resize-none"
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
            {#each bill_info.Cart as item}
              <tr
                class=" h-[40px] {item.id % 2 == 0
                  ? 'bg-white'
                  : 'bg-slate-200'}"
              >
                <td class="w-[250px] pl-2">{item.Name}</td><td class="w-[50px]"
                  >{item.Amount}</td
                ><td class="w-[60px]">{item.Price}</td><td
                  class="w-[90px] text-right pr-2"
                  >{item.Amount * item.Price}</td
                >
              </tr>{/each}
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
            class="w-[230px] h-[30px] text-white bg-green-600 font-bold mr-[20px] mt-[5px]"
          >
            {bill_info.Total}
          </div>
        </div>
      </div>
    </div>
  </dialog>
</div>

<!-- <button class="w-[200px] h-[40px] bg-[#FFC52F] font-bold"
>Complete</button
> -->

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
