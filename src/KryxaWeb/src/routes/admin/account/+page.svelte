<script>
    import AdminNav from "$lib/components/AdminNav.svelte";
    import { MainScreen } from "$lib/Assets.js";
    import { Account } from '$lib/Account.js'
    import {changePassword} from '$lib/Account.js'
    import {checkPassword}from '$lib/Account.js'
    import {AppLogo} from '$lib/Assets.js'
    
    let oldPassword=""
    let newPassword=""
    let confirmNewPassword=""
    
    function logout() {
        localStorage.removeItem("jwt");
        location.replace("/admin");
    }
    async function checkSamePassword(){
        console.log(oldPassword+newPassword+confirmNewPassword)
        if(newPassword!=confirmNewPassword){
            alert("Please confirm the same password")
        
        }
        else if(newPassword==confirmNewPassword){
            changePassword(newPassword).then(res=>res)
            logout()
            
        }
        
    }

    async function showAllFields(){
        let statcode = await checkPassword(oldPassword).then(res=>res)
        if(statcode!=="Check password successful"){
            console.log(statcode)
            alert("Wrong password")
            location.reload()
        }
        else{
            var newPass = document.getElementById("newPass")
            var cfNewPass = document.getElementById("cfNewPass")
            var saveButton = document.getElementById("saveButton")
            var loginButton = document.getElementById("loginButton")
        
            oldPass.style.display = "none"
            newPass.style.display = "block"
            cfNewPass.style.display = "block"
            saveButton.style.display = "block"
            loginButton.style.display = "none"
        }
            // var oldPass = document.getElementById("oldPass")
            // var newPass = document.getElementById("newPass")
            // var cfNewPass = document.getElementById("cfNewPass")
            // var saveButton = document.getElementById("saveButton")
            // var loginButton = document.getElementById("loginButton")

            // oldPass.style.display = "none"
            // newPass.style.display = "block"
            // cfNewPass.style.display = "block"
            // saveButton.style.display = "block"
            // loginButton.style.display = "none"
        
    }

    async function showPassword(){
        var oldPass = document.getElementById("oldPass")
        var newPass = document.getElementById("newPass")
        var cfNewPass = document.getElementById("cfNewPass")
        var hideButton = document.getElementById("hideButton")

        oldPass.type = oldPass.type == "text"?"password":"text"
        newPass.type = newPass.type == "text"?"password":"text"
        cfNewPass.type = cfNewPass.type == "text"?"password":"text"
        hideButton.textContent=hideButton.textContent == "SHOW"?"HIDE":"SHOW"
  

    }
</script>

<div class="flex flex-row h-screen bg-cover overflow-y-scroll" 
    style="background-image: url({MainScreen['Background4']});">
    <div class = "flex flex-col">
        <AdminNav/>
    </div>
    
    <div class = "bg-white/5  backdrop-blur-md rounded-3xl ml-72 mt-60 w-1/2 h-1/2 text-4xl ">
        <img src="{AppLogo}" alt="" width="30%" class=" absolute mx-auto right-0 left-0 top-[-200px] border-[#E3A052]">
        <div class="">
            <div class = "gap-7 mt-20 grid text-amber-400 font-BlackOpsOne " >
                
                <input id = "oldPass" class="m-auto w-2/3 h-16 bg-violet-900/50 rounded text-center" type="password" placeholder="Old password" bind:value={oldPassword}>
                <input id ="newPass"class="none bg-violet-900/50 m-auto w-2/3 h-16 bg-gray-500 rounded text-center" type="password" placeholder="New password" bind:value={newPassword}>
                <input id ="cfNewPass"class="none bg-violet-900/50 m-auto w-2/3 h-16 bg-gray-500 rounded text-center" type="password" placeholder="Confirm new password" bind:value={confirmNewPassword}>
                <button id ="hideButton" on:click={async () => {await showPassword()}} class = " bg-violet-900/50 h-12 mx-auto hover:bg-amber-400 hover:text-violet-900 w-1/4 rounded-3xl">
                    SHOW
                </button>
                <button id ="saveButton" on:click={async () => {await checkSamePassword()}} class = " bg-violet-900/50 h-12 m-auto hover:bg-amber-400 hover:text-violet-900 w-1/2 rounded-3xl">
                    SAVE
                </button>
                <button id ="loginButton" on:click={async () => {await showAllFields()}} class = "bg-violet-900/50 h-12 hover:bg-amber-400 hover:text-violet-900 m-auto w-1/2 rounded-3xl">
                    CONTINUE
                </button>
            </div>
        </div>
    </div>
</div>

<style>
    #newPass{
        display:none
    }
    #cfNewPass{
        display:none
    }
    #saveButton{
        display:none
    }
</style>