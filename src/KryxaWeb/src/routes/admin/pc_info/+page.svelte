<script>
    import AdminNav from "$lib/components/AdminNav.svelte";
    import { Banner } from "$lib/Assets.js";
    import { MainScreen } from "$lib/Assets.js";
    import {Pc} from "$lib/Pc.js";
    import {updateThisPcByID} from "$lib/Pc.js";
    import { onMount } from "svelte";
    
    let pc_info = new Pc()
    onMount(async()=>{
        const urlSearchParams = new URLSearchParams(window.location.search).get("pc_id");
        console.log("Requested PC ID: "+urlSearchParams)
        pc_info = await pc_info.getPcByID(urlSearchParams).then(res=>res)
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
    <div clas="flex flex-col">
        <div class = "bg-white/5 backdrop-blur-md rounded-lg mt-40 ml-40 m-auto w-full h-3/5">
            <div class="flex flex-row">
                <div class = "basis-3/5 gap-8 grid ml-10 text-amber-700 text-3xl " >

                    <div class ="mt-10 h-15 bg-violet-900/50 rounded font-BlackOpsOne"  >
                        {pc_info.PcID}
    
                    </div>
                    <input class ="h-15  bg-violet-900/50 rounded font-BlackOpsOne" 
                        placeholder={pc_info.MAC}
                        bind:value = {pc_info.MAC}
                    >
                    <input class ="h-15  bg-violet-900/50 rounded font-BlackOpsOne" 
                        placeholder={pc_info.IPv4}
                        bind:value={pc_info.IPv4}
                    >
                    
                    <div class ="flex flex-row">
                        <input class ="w-10 h-15 bg-violet-900/50 rounded font-BlackOpsOne" type ="number">
                        <div class ="ml-3 text-amber-300 font-BlackOpsOne">
                            x30m    
                        </div>
                        <button on:click={async () => click()}
                            class = "ml-10  h-15 w-2/3 h-10 rounded-lg hover:bg-amber-600 active:bg-black  bg-violet-900/50 text-amber-700 font-BlackOpsOne">
                            Save
                        </button>
                    </div>
                </div>
                <div class="flex flex-col basis-2/5 text-amber-700 text-3xl">
                    <div class ="">
                        <button class = "ml-10 mt-10 h-15 w-2/3 rounded-lg hover:bg-amber-600 active:bg-black  bg-violet-900/50 font-BlackOpsOne">
                            Bill
                        </button>
                    </div>
                    
                    <div class="w-1/2 ml-16">
                        <img
                          src={MainScreen["pc_screen"]}
                          alt="screen"
                          class="bg-contain"
                        />
                    </div>

                    <button class = "ml-10  h-10 w-2/3 h-10 rounded-lg hover:bg-amber-600 active:bg-black  bg-violet-900/50 text-amber-700 font-BlackOpsOne">
                        Open
                    </button>
                </div>
                
            </div>
        </div>
    </div>
</div>
