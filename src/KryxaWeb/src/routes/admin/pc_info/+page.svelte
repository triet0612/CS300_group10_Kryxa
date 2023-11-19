<script>
    import AdminNav from "$lib/components/AdminNav.svelte";
    import { MainScreen } from "$lib/Assets.js";
    import {Pc} from "$lib/Pc.js";
    import {updateThisPcByID} from "$lib/Pc.js";
    import { onMount } from "svelte";
    let pc_info = new Pc()
    let newTime = "newTime"
    const d = new Date();
    let real_time = d.toISOString();
    onMount(async()=>{
        const urlSearchParams = new URLSearchParams(window.location.search).get("pc_id");
        console.log("Requested PC ID: "+urlSearchParams)
        pc_info = await pc_info.getPcByID(urlSearchParams).then(res=>res)

        const dateTimeArray = pc_info.EndTime.split("T")
        const dateArray = dateTimeArray[0].split("-")
        newTime = dateArray[2]+"/"+dateArray[1]+"/"+dateArray[0]+"  "+dateTimeArray[1]
    })

    async function click() {
        const urlSearchParams = new URLSearchParams(window.location.search).get("pc_id");
        let statcode =await updateThisPcByID(pc_info,urlSearchParams).then(res=>res)
        console.log(statcode)
        if (statcode !== 200) {
            alert("Failed updating Pc")

        }
        location.reload()
    }



</script>

<div 
    class="flex flex-row h-screen bg-cover overflow-y-scroll"
    style="background-image: url({MainScreen['Background4']});">
    <div class="flex flex-col">
        <AdminNav />
    </div>
    <div clas="flex flex-col ">
        <div class = "bg-white/5 backdrop-blur-md rounded-lg mt-40 ml-40 m-auto w-full h-3/5 text-4xl ">
            <div class="flex flex-row">
                <div class = "basis-3/5 grid ml-10 text-amber-700 x" >

                    <div class = " flex flex-row mt-10 ">
                        <div class ="w-1/2 flex items-center  h-12 bg-violet-900/50 rounded font-BlackOpsOne"  >
                            PC ID: {pc_info.PcID}
                        </div>
                        <input class ="ml-10 w-1/2 h-12  bg-violet-900/50 rounded font-BlackOpsOne" 
                            placeholder={pc_info.Password}
                            bind:value = {pc_info.Password}
                        >
                    </div>
                    
                    <input class ="h-12  bg-violet-900/50 rounded font-BlackOpsOne" 
                        placeholder={pc_info.IPv4}
                        bind:value={pc_info.IPv4}
                    >
                    <div class ="flex items-center h-12  bg-violet-900/50 rounded font-BlackOpsOne">
                        {newTime}
                    </div>
                    
                    

                
                    
                    <div class ="flex flex-row">
                        <button class = " h-12 w-2/3 h-10 rounded-lg hover:bg-amber-600 active:bg-black  bg-violet-900/50 text-amber-700 font-BlackOpsOne">
                            Bill
                        </button>
                        <button on:click={async () => click()}
                            class = "ml-10  h-12 w-2/3 h-10 rounded-lg hover:bg-amber-600 active:bg-black  bg-violet-900/50 text-amber-700 font-BlackOpsOne">
                            Save
                        </button>
                        <button class = "ml-10  h-12 w-2/3 h-10 rounded-lg hover:bg-amber-600 active:bg-black  bg-violet-900/50 text-amber-700 font-BlackOpsOne">
                            Terminate
                        </button>
                    </div>
                </div>
                <div class="flex flex-col basis-2/5 text-amber-700 text-3xl">
                    <div class ="">
                        <button class = "ml-16 mt-10 h-12 w-2/3 rounded-lg hover:bg-amber-600 active:bg-black  bg-violet-900/50 font-BlackOpsOne">
                            Open
                        </button>
                    </div>
                    
                    <div class="mt-5 w-2/3 ml-16 {real_time > pc_info.EndTime
                        ? 'bg-green-600 bg-opacity-75'
                        : real_time < pc_info.EndTime
                        ? 'bg-red-600 bg-opacity-75'
                        : 'bg-white  bg-opacity-25'}
                        rounded-xl">
                        <img 
                          src={MainScreen["pc_screen"]}
                          alt="screen"
                          class="bg-contain w-11/12 m-auto"
                        />
                    </div>

                    
                    <div class = "ml-10 flex flex-row">
                        <input class ="text-center mt-5 ml-10 w-24 h-12 bg-violet-900/50 rounded font-BlackOpsOne" type ="number">
                        <div class ="mt-7 ml-3 text-amber-300 font-BlackOpsOne">
                            x30m    
                        </div>
                    </div>
                    
                </div>
                
            </div>
        </div>
    </div>
</div>
