<script>
    import {NavIcons} from '$lib/Assets.js'
    const items = ["Management", "Items", "Tournament", "Statistics", "Settings"]
</script>

<aside class="top-0 left-0 w-64 m-5 p-2 h-screen flex flex-col justify-center">
    <div class="px-3 py-5 rounded-xl overflow-y-auto bg-gradient-to-b from-black to-[#352900] border-[1px] border-white">
        <ul class="text-2xl text-[#E3A052] font-BlackOpsOne">
            <li><img src="{NavIcons["Logo"]}" alt="Logo"></li>
            {#each items as it}
                <div class="flex m-3">
                    <li class="flex p-2 hover:bg-[#E3A052] hover:text-black">
                        <a href="/admin/{it}">{it}</a>
                    </li>
                </div>
            {/each}
            <div class="flex mt-5 border-[1px] hover:bg-[#E3A052] hover:text-black justify-center">
                <li class="flex items-center justify-center p-2">
                    <button>Logout</button>
                </li>
            </div>
        </ul>
    </div>
</aside>