<script>
  import AdminNav from "$lib/components/AdminNav.svelte";
  import { MainScreen } from "$lib/Assets.js";
  import { fetch_all,fetch_by_id } from "$lib/Bill.js";
  import { Pc} from "$lib/Pc.js";
  import { onMount } from "svelte";
  let bill_list = [];
  let item_pc = new Pc();
  let input_bill_id;
  onMount(async () => {
    bill_list = await fetch_all().then((res) => res);
    console.log(bill_list)
  });

  async function UpdateBill(){
    bill_list = await fetch_by_id(input_bill_id);
    console.log(bill_list)
  }

  async function validate(str,pc_id){
    item_pc = await item_pc.getPcByID(pc_id).then((res)=>res)
    if(refort(str)!=""){
      return 0;
    }
    else{
      if(refort(item_pc.EndTime)<=cur()){
        return 1;
      }
      else{
        return 2;
      }
    }
  }

  function cur(){
    const now = new Date();
    const currentHour = ('0' + now.getHours()).slice(-2);
    const currentMinute = ('0' + now.getMinutes()).slice(-2);
    const currentSecond = ('0' + now.getSeconds()).slice(-2);
    const currentDay = ('0' + now.getDate()).slice(-2);
    const currentMonth = ('0' + (now.getMonth() + 1)).slice(-2);
    const currentYear = now.getFullYear();

    const datee = `${currentDay}/${currentMonth}/${currentYear} ${currentHour}:${currentMinute}:${currentSecond}`;
    return datee;
  }

  function refort(str){
    const originalDate = new Date(str);

    const year = originalDate.getFullYear();
    const month = ('0' + (originalDate.getMonth() + 1)).slice(-2); // Adding 1 because months are zero-based
    const day = ('0' + originalDate.getDate()).slice(-2);
    const hours = ('0' + originalDate.getHours()).slice(-2);
    const minutes = ('0' + originalDate.getMinutes()).slice(-2);
    const seconds = ('0' + originalDate.getSeconds()).slice(-2);
    
    const formattedDateString = `${day}/${month}/${year} ${hours}:${minutes}:${seconds}`;
    return formattedDateString
  }
</script>


<div id="bg" class="flex flex-row h-screen bg-cover" style="background-image: url({MainScreen['Background4']});">
  <div class="flex flex-col">
    <AdminNav />
  </div>
  <div class="flex-col flex h-full w-auto">
    <div class="h-[70px] font-BlackOpsOne text-xl text-purple-300 justify-start items-center flex flex-row my-2 ">
        <input type="number" min=0 placeholder="PC ID"  class="px-5 h-[50px] rounded-3xl bg-purple-900" bind:value = {input_bill_id} on:change={UpdateBill} />
        <p class="px-5">Pick Date:</p>
        <input type="date" value="" class="bg-purple-900" />
    </div>
    <div class="flex-col flex">
      <div class="grid grid-flow-col grid-cols-2 gap-5">
        <div id="bo">
          <ul class="grid grid-flow-row grid-cols-3 m-7 gap-5">
            {#each bill_list as valid}
              <li class="text-center justify-center items-center" style ="{validate(valid.Datetime,valid.PcID)!=0? 'display:none':''}">
                <div id="bi" class="grid grid-flow-row auto-rows-max">
                  <img src={validate(valid.Datetime,valid.PcID)==1? MainScreen["RedForm"]:MainScreen["GreenForm"]} alt="screen"/>
                  <div class="justify-center">{valid.BillID}</div>
                  <div class="justify-center">{refort(valid.Datetime)}</div>
                </div>
              </li>
            {/each}
          </ul>
        </div>
        <div id="bo">
          <ul class="grid grid-flow-row grid-cols-3 m-7 gap-5">
            {#each bill_list as valid}
              <li class="text-center justify-center items-center font-medium" style ="{validate(valid.Datetime,valid.PcID)==0? 'display:none':''}">
                <div id="bi" class="grid grid-flow-row auto-rows-max">
                  <img src={MainScreen["RedForm"]} alt="screen"/>
                  <div class="justify-center">{valid.BillID}</div>
                  <div class="justify-center">{refort(valid.Datetime)}</div>
                </div>
              </li>
            {/each}
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
<style>
  #bi{
    width: 170px;
    height: 200px;
  }
  #bo{
    width: 700px;
    height: 800px;
    border-radius: 20px;
    background-color: rgba(62, 26, 90, 0.8);
  }
</style>

