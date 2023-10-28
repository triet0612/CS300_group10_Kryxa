<script>
    import { Account } from '$lib/Account.js'
    import { AdminLogin } from '$lib/Assets.js'
    let acc = new Account()
</script>

<div id="back" class="h-screen relative" style="background-image: url({AdminLogin['Background']});">
    <div class="grid bg-amber-500 p-5 w-3/12 h-60 rounded-xl place-items-center justify-center relative top-1/3 left-2/4">
        <input class="w-full h-12 bg-white rounded text-center" type="number" placeholder="ID" bind:value={acc.ID}>
        <input class="w-full h-12 bg-white rounded text-center" type="password" placeholder="Password" bind:value={acc.Password}>
        <button on:click={async () => {await acc.login("Admin")}} class="w-3/4 h-10 bg-white rounded-xl hover:bg-slate-600 active:bg-black">Login</button>
    </div>
</div>

<style>
    #back {
        background-size: 100% 100%;
    }
</style>
