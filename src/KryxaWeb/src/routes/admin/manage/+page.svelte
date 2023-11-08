<script>
    import AdminNav from "$lib/components/AdminNav.svelte";
    import {ImageItem} from '$lib/Assets.js';
    import {Item, fetch_all} from '$lib/Item.js';
    import { onMount } from "svelte";
    let list_items = []
    onMount(async () => {
        list_items = await fetch_all().then(res => res)
        console.log(list_items)
    })
</script>

<div class="bg-gradient-to-b from-black to-yellow-600 flex flex-row">
    <div class="flex flex-col">
        <AdminNav></AdminNav>
    </div>
    <div class="mr-auto ml-auto ">
        <div class="flex-row w-screen">
            <div class="gap-36 flex w-9/12 mx-14">
                <div class="flex flex-col marker:text-center w-[27%] ml-5 max-md:w-full max-md:ml-0">
                    <button class=" text-orange-400 text-4xl whitespace-nowrap border bg-black w-full max-w-[301px] mt-36 mx-auto px-20 py-6 rounded-3xl border-solid border-white self-start max-md:mt-10 max-md:pl-8 max-md:pr-5">
                        Food
                    </button>
                  </div>
                  <div class="flex flex-col text-center items-center w-[27%] ml-5 max-md:w-full max-md:ml-0">
                    <button class="text-orange-400 text-4xl whitespace-nowrap border bg-black w-full max-w-[301px] mt-36 mx-auto px-20 py-6 rounded-3xl border-solid border-white self-start max-md:mt-10 max-md:pl-8 max-md:pr-5">
                      Drink
                    </button>
                  </div>
                  <div class="flex flex-col text-centeritems-center w-1/5 ml-5 max-md:w-full max-md:ml-0">
                    <div class="border bg-black flex w-full max-w-[301px] flex-col mt-36 mx-auto px-20 py-6 rounded-3xl border-solid border-white max-md:mt-10 max-md:px-5">
                      <button class="text-orange-400 text-4xl self-center whitespace-nowrap">
                        Time
                      </button>
                    </div>
                  </div>
            </div>
            <div class="class = h-5"></div>
            <div class="pt-5 pl-20 w-9/12 h-screen mx-20 ">
              <ul class="grid grid-flow-row grid-cols-5">
                {#each list_items as list_item}
                  <div class="w-48 h-48 flex-row text-white justify-center text-center active:bg-violet-700">
                    <div class="w-48 h-36 bg-gray-600 justify-center" >
                      <img src = {
                        ImageItem[list_item.Name]}
                        alt="screen"
                        class="bg-contain w-48 h-36"
                        />
                    </div>
                    <p class="justify-center">{list_item.Name} : {list_item.Price}</p>
                  </div>
                {/each}
                </ul>
            </div>
        </div>
    </div>
  </div>
