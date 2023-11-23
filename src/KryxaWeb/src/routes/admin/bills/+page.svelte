<script>
  import AdminNav from "$lib/components/AdminNav.svelte";
  import { MainScreen } from "$lib/Assets.js";
  import { Bill, fetch_all } from "$lib/Bill.js";
  import { Pc, get_Pcs } from "$lib/Pc.js";
  import { onMount } from "svelte";
  let bill_list = [];
  onMount(async () => {
    bill_list = await fetch_all().then((res) => res);
  });

  async function validate(str,pc_id){
    if(refort(str)!=""){
      return 0;
    }
    else{
      if(refort(pc_id.EndTime)<=cur()){
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

    // Displaying the current time
    const datee = `${currentDay}/${currentMonth}/${currentYear} ${currentHour}:${currentMinute}:${currentSecond} `;
    console.log(datee);
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

    console.log(formattedDateString);

    return formattedDateString
  }
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
    <div id="Nav" class="flex-col">p</div>
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

