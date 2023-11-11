<script>
    import { Account } from '$lib/Account.js'
    let acc = new Account()
</script>

<div id="back" class="h-screen font-BlackOpsOne pt-44 pb-auto bg-login-bg">
    <div class="grid text-white bg-gradient-to-t from-[#4C0783] to-[#4132EC73] p-5 w-3/12 h-60 rounded-xl place-items-center justify-center mr-80 ml-auto">
        <input class="w-full h-12 bg-gray-500 rounded text-center" type="number" placeholder="ID" bind:value={acc.ID}>
        <input class="w-full h-12 bg-gray-500 rounded text-center" type="password" placeholder="Password" bind:value={acc.Password}>
        <button on:click={async () => {await acc.login("Admin")}} class="w-3/4 h-10 bg-[#BC1AD7] rounded-xl hover:bg-slate-600 active:bg-black">Login</button>
    </div>
</div>

<style>
    #back {
        background-size: 100% 100%;
    }
</style>
