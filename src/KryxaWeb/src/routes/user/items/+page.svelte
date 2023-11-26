<script>
    import CustomerNav from "$lib/components/CustomerNav.svelte";
 
    import { Item, fetch_all, user_fetch_all, user_fetch_category} from '$lib/Item.js';
    import { onMount } from "svelte";
    import {UserAssets} from '$lib/Assets.js';
    import ModalItem from "$lib/components/ModalItem.svelte";
    import { get } from "svelte/store";
  

    let list_items = []
    let text_input = ""
    let category_filter = "All"
    let status = "close";
    

    // pop up
    function close(event) {
      if (event.key === "Escape") {
        status = "close";
      }
    }

    function openModal(event) {
      status = "open";
    }
    // Auto pull db
    // Minh: user's fetch functions tested correctly in docs, but will not show anything in this screen for now. Could be missing /login page for user -> no authorization
    onMount(async () => {
        // list_items = await user_fetch_all().then(res => res); // Commented for debug
        list_items = await fetch_all().then(res => res);
        console.log(list_items);
    });

    // pull data on request
    export async function search_al(){
      const category_str = get(category_filter)
      list_items = await user_fetch_category(category_str, text_input)
      console.log(list_items)
    };

</script>
  
<div id="bg"
  class=" fixed h-full w-full bg-cover {status === 'open' ? 'blur-3xl' : ''} "
  style="background-image: url({UserAssets['ItemsBackground']});">
    <!-- Nav Bar -->
      <div class="fixed">
          <CustomerNav/>
      </div>
      <!-- View Page -->
      <div class="flex flex-col ml-72 h-screen">
        <!-- Search bar -->
        <div class="fixed z-10 ml-5">
          <div class="flex flex-row">
            <!-- Input type check -->
            <input 
              type="text" 
              id="search" 
              placeholder="Search items..." 
              class="mt-20 px-5 py-5 rounded-3xl bg-[#FF9900]" 
              bind:value = {text_input} 
              on:change={search_al}
            />
          </div>
        </div>
        <!-- End search bar -->
        <!-- Cart button -->
        <div class="flex flex-row self-end bg-[#FF0202]
                    p-3
                    rounded-2xl
                    m-10 mr-16
                    hover:cursor-pointer hover:drop-shadow-xl hover:bg-gradient-to-r hover:from-[#FF0202] hover:to-[#FF9900]">
          <img src={UserAssets.CartIcon} alt="cart icon"/>
          <p class="text-5xl text-white font-BlackOpsOne pl-3 self-center">Cart</p>
        </div>
        <div class="p-5 overflow-y-scroll">
          <ul class="grid grid-cols-5 gap-5">
            {#each list_items as list_item}
                {#if list_item.Stock > 0}
                    <li class="w-56 h-56 bg-[#DFDFDF]/[0.29] flex-row 
                              text-white justify-center text-center border-2 items-center backdrop-blur-2xl rounded-lg
                              hover:scale-105 hover:cursor-pointer">
                            <div class="min-w-56 min-h-48 rounded-lg">
                                <!-- svelte-ignore a11y-missing-attribute -->
                                <img style = "screen" src="http://localhost:8000/api/admin/getfile/{list_item.ItemID}" sizes="(max-width:224px)"
                                class="bg-contain w-56 h-48 rounded-lg"
                                />
                            </div>
                        <p id ="image"class="justify-center" value={list_item.Name}>{list_item.Name} | {parseInt(list_item.Price/1000)}.000</p>
                    </li>
              {/if}
            {/each}
            </ul> 
        </div>
      </div>
    </div>
  
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div on:keydown={close}>
    <ModalItem {status} on:keydown={close} />
  </div>