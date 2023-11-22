<script>
    import AdminNav from "$lib/components/AdminNav.svelte";
    import { MainScreen } from "$lib/Assets.js";
    import { Account } from '$lib/Account.js'
    import {changePassword} from '$lib/Account.js'
    
    let oldPassword=""
    let newPassword=""
    let confirmNewPassword=""

    async function checkSamePassword(){
        console.log(oldPassword+newPassword+confirmNewPassword)
        if(newPassword!=confirmNewPassword){
            alert("Please confirm the same password")
        }
        else if(newPassword==confirmNewPassword){
            changePassword(oldPassword,newPassword).then(res=>res)
            
        }
        // location.reload()
    }
</script>

<div class="flex flex-row h-screen bg-cover overflow-y-scroll" 
    style="background-image: url({MainScreen['Background4']});">
    <div class = "flex flex-col">
        <AdminNav/>
    </div>
    <div class = "bg-gradient-to-t from-[#4C0783] to-[#4132EC73] backdrop-blur-md rounded-lg mt-40 ml-40 m-auto w-1/2 h-2/3 text-4xl ">
        <div class="">
            <div class = "gap-5 mt-10 grid text-amber-700 font-BlackOpsOne " >
                <input class="m-auto w-2/3 h-12 bg-gray-500 rounded text-center" type="text" placeholder="Old password" bind:value={oldPassword}>
                <input class="m-auto w-2/3 h-12 bg-gray-500 rounded text-center" type="text" placeholder="New password" bind:value={newPassword}>
                <input class="m-auto w-2/3 h-12 bg-gray-500 rounded text-center" type="text" placeholder="Confirm new password" bind:value={confirmNewPassword}>
                <button on:click={async () => {await checkSamePassword()}} class = "bg-gray-500 m-auto text-green-800 w-1/5 rounded">
                    save
                </button>
            </div>
        </div>
    </div>
</div>

