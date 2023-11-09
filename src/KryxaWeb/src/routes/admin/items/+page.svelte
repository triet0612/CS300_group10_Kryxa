<script>
    import AdminNav from "$lib/components/AdminNav.svelte";
    import {ImageItem} from '$lib/Assets.js';
    import {Item, fetch_all} from '$lib/Item.js';
    import { onMount } from "svelte";
    import {MainScreen} from '$lib/Assets.js';
    let list_items = []
    onMount(async () => {
        list_items = await fetch_all().then(res => res)
        console.log(list_items)
    })
    
</script>

<div id="bg"class=" fixed h-full w-full bg-cover"style="background-image: url({MainScreen['Background2']});">
    <div class="fixed">
        <AdminNav/>
    </div>
    <div class="flex flex-col ml-72">
      <div class="fixed">
        <div class="flex flex-row">
          <div class=" text-center ml-5 flex-col">
            <button class=" text-orange-400 text-3xl  border bg-black mt-5 px-20 py-5 rounded-3xl border-solid border-white ">
                All
            </button>
          </div>  
            <div class=" text-center ml-5 flex-col">
              <button class=" text-orange-400 text-3xl  border bg-black mt-5 px-20 py-5 rounded-3xl border-solid border-white">
                  Time
              </button>
            </div>
            <div class=" text-center ml-5 flex-col">
              <button class="text-orange-400 text-3xl  border bg-black mt-5 px-20 py-5 rounded-3xl border-solid border-white">
                Food
              </button>
            </div>
            <div class=" text-center ml-5 flex-col">
              <button class=" text-orange-400 text-3xl  border bg-black mt-5 px-20 py-5 rounded-3xl border-solid border-white">
                Drink
              </button>
            </div>
        </div>
      </div>
        <div class="pt-32 pl-5  overflow-y-scroll h-screen">
          <ul class="grid grid-cols-5 gap-5">
            {#each list_items as list_item}
              <li class="w-56 h-56 flex-row text-white justify-center text-center active:bg-violet-700 border-2 items-center">
                <div class="w-52 h-48 bg-gray-600 justify-center"  >
                  <img src = {
                    ImageItem[list_item.Name]}
                    alt="screen"
                    class="bg-contain w-56 h-48"
                    />
                </div>
                <p class="justify-center">{list_item.Name} : {list_item.Price}</p>
              </li>
            {/each}
            </ul>
        </div>
    </div>
  </div>
