<script>
    import AdminNav from "$lib/components/AdminNav.svelte";
    import { MainScreen } from "$lib/Assets.js";
    import {Pc} from "$lib/Pc.js";
    import {updateThisPcByID} from "$lib/Pc.js";
    import { onMount } from "svelte";
    let pc_info = new Pc()
    let newTime = "newTime"
    const d = new Date();
    let real_time = d.toLocaleString();
    let openButton;
    let terminateButton;
    onMount(async()=>{
        const urlSearchParams = new URLSearchParams(window.location.search).get("pc_id");
        pc_info = await pc_info.getPcByID(urlSearchParams).then(res=>res)

        newTime = new Date(pc_info.EndTime).toLocaleString()
        if (pc_info.EndTime === undefined || pc_info.EndTime === "") {
            openButton.disabled = true
            terminateButton.disabled = false
        }
        else if (new Date(real_time) < new Date(pc_info.EndTime)) {
            openButton.disabled = true
            terminateButton.disabled = false
        } else {
            openButton.disabled = false
            terminateButton.disabled = true
        }
    })

    async function click() {
        const urlSearchParams = new URLSearchParams(window.location.search).get("pc_id");
        let statcode = await updateThisPcByID(pc_info,urlSearchParams).then(res=>res)
        console.log(statcode)
        if (statcode !== 200) {
            alert("Failed updating Pc")
        }
        location.reload()
    }
    let session_time = 0;
    async function openSession() {
        let res = await fetch(`http://localhost:8000/api/admin/session?PcID=${pc_info.PcID}&time=${session_time}`,{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem("jwt")
            },
        }).then(r => r.status !== 200? "": r.statusText)
        .catch(err => {console.log(err); return ""})
        if (res === "") {
            alert("A bill in progress or error open")
        } else {
            location.reload()
        }
    }

    async function terminateSession() {
        let res = await fetch(`http://localhost:8000/api/admin/session?PcID=${pc_info.PcID}`,{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem("jwt")
            },
        }).then(r => r.status !== 200? "": r.statusText)
        .catch(err => {console.log(err); return ""})
        if (res === "") {
            alert("Error closing")
        } else {
            location.reload()
        }
    }
</script>

<div 
    class="flex flex-row h-screen bg-cover overflow-y-scroll"
    style="background-image: url({MainScreen['Background4']});">
    <div class="flex flex-col">
        <AdminNav />
    </div>
    <div class = "flex flex-col bg-white/5 backdrop-blur-md rounded-lg mt-40 ml-40 m-auto w-2/3 h-3/5 text-4xl ">
        <div class="flex flex-row">
            <div class = "basis-3/5 grid ml-10 text-amber-400" >
                <div class = " flex flex-row mt-10 ">
                    <div class ="w-1/3 pl-5  flex items-center  h-16 rounded font-BlackOpsOne">
                        PC ID: 
                    </div>
                    <div class ="w-1/5 pl-5  flex items-center h-16 bg-violet-900/50 rounded font-BlackOpsOne"  >
                        {pc_info.PcID}
                    </div>
                    <div class ="ml-10 w-1/2 pl-5  flex items-center  h-16 rounded font-BlackOpsOne">
                        Password:
                    </div>
                    <input class =" w-1/4 pl-5 h-16  bg-violet-900/50 rounded font-BlackOpsOne" 
                        placeholder={pc_info.Password}
                        bind:value = {pc_info.Password}
                    >
                </div>
                <input class ="h-16 pl-5 bg-violet-900/50 rounded font-BlackOpsOne" 
                    placeholder={pc_info.IPv4}
                    bind:value={pc_info.IPv4}
                >
                <div class ="flex pl-5 items-center h-16 bg-violet-900/50 rounded font-BlackOpsOne">
                    {newTime}
                </div>
                <div class ="flex flex-row text-amber-400">
                    <button class = "w-2/3 h-16 rounded-full hover:bg-yellow-300 hover:text-violet-900 active:bg-black  bg-violet-900  font-BlackOpsOne">
                        Bill
                    </button>
                    <button on:click={async () => click()}
                        class = "ml-10 w-2/3 h-16 rounded-full hover:bg-amber-400 hover:text-violet-900 active:bg-black  bg-violet-900  font-BlackOpsOne">
                        Save
                    </button>
                    <button on:click={terminateSession} bind:this={terminateButton} class = "ml-10 w-2/3 h-16 rounded-full hover:bg-amber-400 hover:text-violet-900 active:bg-black  bg-violet-900 font-BlackOpsOne">
                        Terminate
                    </button>
                </div>
            </div>
            <div class="flex flex-col basis-2/5 text-amber-400 text-3xl">
                <div class ="">
                    <button class="ml-16 mt-10 h-16 w-2/3 rounded-full hover:bg-amber-400 hover:text-violet-900 active:bg-black  bg-violet-900 text-yellow-300 font-BlackOpsOne"
                        on:click={openSession} bind:this={openButton}>
                        Open
                    </button>
                </div>
                <div class="mt-5 w-2/3 ml-16 { new Date(real_time) > new Date(pc_info.EndTime)
                    ? 'bg-green-600 bg-opacity-75'
                    : new Date(real_time) < new Date(pc_info.EndTime)
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
                    <input class ="text-center mt-5 ml-10 w-24 h-16 bg-violet-900/50 rounded font-BlackOpsOne" type ="number" bind:value={session_time}>
                    <div class ="mt-7 ml-3 text-amber-300 font-BlackOpsOne">
                        x30m    
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
