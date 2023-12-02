<script>
    import CustomerNav from "$lib/components/CustomerNav.svelte";
 
    import { user_fetch_category} from '$lib/Item.js';
    import {UserAssets} from '$lib/Assets.js';
    import ModalItem from "$lib/components/ModalItem.svelte";
  

    let list_items = []
    let text_input = ""
    let status = "close";
    let filter = "All";

    // pop up
    function close(event) {
      if (event.key === "Escape") {
        status = "close";
      }
    }

    function openModal(event) {
      status = "open";
    }

    async function search_all(filter, text_input){
      list_items = await user_fetch_category(filter, text_input)
      console.log(list_items)
    };

    $: {
      search_all(filter, text_input)
    }
</script>
  
<div id="bg"
  class="flex flex-row h-screen bg-cover {status === 'open' ? 'blur-3xl' : ''} "
  style="background-image: url({UserAssets['ItemsBackground']});">
  <div class="flex flex-col">
    <CustomerNav bind:filter_value={filter}/>
  </div>
  <div class="flex flex-col h-full w-full p-10">
    <div class="flex flex-row justify-between">
      <div class="flex flex-row">
        <input type="text" placeholder="Search items..." 
        class="p-5 placeholder-black rounded-3xl font-BlackOpsOne text-2xl bg-[#FF9900] text-black" bind:value={text_input}/>
      </div>
      <div class="flex flex-row bg-red-600 p-3 rounded-2xl hover:cursor-pointer hover:drop-shadow-xl hover:bg-gradient-to-r hover:from-[#FF0202] hover:to-[#FF9900]">
        <img src={UserAssets.CartIcon} alt="cart icon"/>
        <p class="text-5xl text-white font-BlackOpsOne self-center">Cart</p>
      </div>
    </div>
    <div class="p-5 h-full overflow-y-hidden">
      <ul class="grid grid-cols-5 gap-5">
        {#each list_items as list_item}
            {#if list_item.Stock > 0}
              <li class="w-56 h-56 bg-gray-600 flex-rowtext-white justify-center text-center border-2 items-center rounded-lg hover:scale-105">
                <div class="min-w-56 min-h-48 rounded-lg">
                  <!-- svelte-ignore a11y-missing-attribute -->
                  <img style="screen" src="http://localhost:8000/api/getfile/{list_item.ItemID}" sizes="(max-width:224px)"
                    class="bg-contain w-56 h-48"
                  />
                </div>
                <p id ="image"class="justify-center font-BlackOpsOne text-xl">{list_item.Name} | {list_item.Price.toLocaleString()}</p>
              </li>
          {/if}
        {/each}
      </ul>
    </div>
     
  </div>
  <div id ="cartPage"class="flex flex-row w-1/3 bg-white">
    
  </div>  
</div>
  
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div on:keydown={close}>
  <ModalItem {status} on:keydown={close} />
</div>