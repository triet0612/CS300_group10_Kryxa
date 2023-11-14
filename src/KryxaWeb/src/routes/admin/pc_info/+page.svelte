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

<div class="flex flex-row h-screen bg-gradient-to-b from-black to-[#352900] overflow-y-scroll">
    <div class="flex flex-col">
        <AdminNav />
    </div>
    <div clas="flex flex-col">
        <div class = "w-5/6 mx-auto">
            <img 
                src = {Banner}
                alt = "banner"
            />
        </div>
        <div class = "bg-stone-500 rounded-lg w-2/3 h-1/2 m-auto mt-10">
            <div class="flex flex-row">
                <div class = "basis-3/5 gap-5 grid ml-5 text-amber-700 text-3xl " >

                    <div class ="mt-10 h-10 bg-stone-200 rounded" >
                        {pc_info.PcID}
    
                    </div>
                    <input class ="h-10 bg-stone-200 rounded" 
                        placeholder={pc_info.MAC}
                        bind:value = {pc_info.MAC}
                    >
                    <input class ="h-10 bg-stone-200 rounded" 
                        placeholder={pc_info.IPv4}
                        bind:value={pc_info.IPv4}
                    >
                    
                    <div class ="flex flex-row">
                        <input class ="w-10 h-10 bg-stone-200 rounded" type ="number">
                        <div class ="ml-3 text-amber-400">
                            x30m    
                        </div>
                        <button on:click={async () => click()}
                            class = "ml-10  h-10 w-2/3 h-10 rounded-lg hover:bg-amber-600 active:bg-black  bg-stone-200 text-amber-700">
                            Save
                        </button>
                    </div>
                </div>
                <div class="flex flex-col basis-2/5 text-amber-700 text-3xl">
                    <div class ="">
                        <button class = "ml-10 mt-10 h-10 w-2/3 rounded-lg hover:bg-amber-600 active:bg-black  bg-stone-200">
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

                    <button class = "ml-10  h-10 w-2/3 h-10 rounded-lg hover:bg-amber-600 active:bg-black  bg-stone-200 text-amber-700">
                        Open
                    </button>
                </div>
                
            </div>
        </div>
    </div>
</div>
