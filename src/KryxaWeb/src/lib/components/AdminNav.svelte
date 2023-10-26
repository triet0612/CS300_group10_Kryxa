<script>
    import {NavIcons} from '$lib/ImageAssets.js'
    const items = ["Management", "Items", "Tournament", "Statistics", "Settings"]
</script>

<aside class="fixed top-0 left-0 w-64 h-screen">
    <div class="h-full px-3 overflow-y-auto bg-[#2B2A2A]">
        <ul class="text-xl text-[#E3A052]">
            <li><img src="{NavIcons["Logo"]}" alt="Logo"></li>
            {#each items as it}
                <div class="flex m-3">
                    <li class="flex items-center p-2">
                        <div class="w-10">
                            <img src="{NavIcons[it]}" alt="Icon">
                        </div>
                        <div>
                            <a href="/admin/{it}">
                                <p class="ml-6">{it}</p>
                            </a>
                        </div>
                    </li>
                </div>
                <hr>
            {/each}
        </ul>
    </div>
</aside>