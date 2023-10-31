<script>
    import {NavIcons} from '$lib/Assets.js'
    import AdminNav from '$lib/components/AdminNav.svelte'
    const items = ["Management", "Items", "Tournament", "Statistics", "Settings"]
</script>
<div>
    <aside class="fixed top-12 left-5 w-64 h-auto margin-x">
        <div id="sidebar" class="h-full px-3 overflow-y-auto bg-[#2B2A2A]">
            <ul id="tx" class="text-xl text-[rgb(227,160,82)] font-tx">
                <li><img src="{NavIcons["Logo"]}" alt="Logo"></li>
                {#each items as it}
                    <div class="flex m-3">
                        <li class="flex items-center p-2">
                            
                            <div>
                                <a href="/admin/{it}">
                                    <p class="ml-6">{it}</p>
                                </a>
                            </div>
                        </li>
                    </div>
                    
                {/each}
            </ul>
        </div>
    </aside>
    <!-- <AdminNav/> -->
    
    <div id="background">
        <div class="fixed top-5 left-72 h-auto w-auto">
            <button id="food" class="px-6 h-auto uppercase font-primary tracking-wider border-2 border-white bg-gradient-to-r from-yellow-500 to-black text-black rounded-2xl" type="submit">
                Food
              </button>
              <button id="food" class="px-6 h-auto uppercase font-primary tracking-wider border-2 border-white bg-gradient-to-r from-yellow-500 to-black text-black rounded-2xl" type="submit">
                Drinks
              </button>
              <button id="food" class="px-6 h-auto uppercase font-primary tracking-wider border-2 border-white bg-gradient-to-r from-yellow-500 to-black text-black rounded-2xl" type="submit">
                Time
              </button>
        </div>
    </div>
</div>
<style>
    #food{
        font-size: 40px;
        color: white;
    }
    #sidebar{
        border-top-right-radius: 30px;
        border-bottom-right-radius: 30px;
        border-top-left-radius: 30px;
        border-bottom-left-radius: 30px;
        
    }
    #background{
        position: static;
        width: 100%;
        min-height: 100vh;
        background-color:rgba(27, 27, 27, 1);
    }
    
</style>