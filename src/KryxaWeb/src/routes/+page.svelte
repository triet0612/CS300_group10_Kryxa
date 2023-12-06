<script>
    import CustomerNav from "$lib/components/CustomerNav.svelte";
 
    import { user_fetch_category} from '$lib/Item.js';
    import {UserAssets} from '$lib/Assets.js';
    import ModalItem from "$lib/components/ModalItem.svelte";
    import { onMount } from "svelte";
  

    let list_items = []
    let list_all_items = []
    let cart_items =[]
    let text_input = ""
    let status = "close";
    let filter = "All";
   

    function addItem(ItemID){
      let positionThisProductInCart = cart_items.findIndex((value) => value.ItemID == ItemID)
      console.log(positionThisProductInCart)
      if (cart_items.length <= 0){
        cart_items = [{
          ItemID: ItemID,
          quantity: 1
        }]
      }
      else if(positionThisProductInCart<0){
        cart_items.push({
          ItemID: ItemID,
          quantity: 1
        })
      }
      else{
        cart_items[positionThisProductInCart].quantity = cart_items[positionThisProductInCart].quantity+1
      }
      addCartToHTML()
      addCartToMemory()
      console.log(cart_items)
    }

    function addCartToMemory (){
      localStorage.setItem('cart_items', JSON.stringify(cart_items));
    } 

    function addCartToHTML(){
      var listCartHTML = document.getElementById("cart_list")
      listCartHTML.innerHTML = '';
      let totalQuantity = 0;
      if(cart_items.length > 0){
        cart_items.forEach(item => {
            totalQuantity = totalQuantity +  item.quantity;
            let newItem = document.createElement('div');
            newItem.classList.add('item');
            newItem.dataset.id = item.ItemID;

            let positionProduct = list_all_items.findIndex((value) => value.ItemID == item.ItemID);
            let info = list_all_items[positionProduct];
            listCartHTML.appendChild(newItem);
            newItem.innerHTML = `
                <div class = "flex flex-row bg-white/80 rounded-3xl h-1/2 mt-5 h-20 w-11/12 mx-auto">
                  <img style="screen" src="http://localhost:8000/api/getfile/${info.ItemID}" sizes="(max-width:20px)"
                      class="bg-contain rounded-full ml-5 h-14 my-auto"
                    />
                  <div class = "flex flex-col ml-3 mt-2">
                    <div class="text-violet-900 text-xl font-BlackOpsOne">
                    ${info.Name}
                    </div>
                    <div class="text-violet-900 text-xl font-BlackOpsOne mt-3">$${info.Price * item.quantity}</div>
                  </div>
                  <div class="">
                      <span class="minus"><</span>
                      <span>${item.quantity}</span>
                      <span class="plus">></span>
                  </div>
                </div>
            `;
        })
    }}
    onMount(async()=>{
      list_all_items = await user_fetch_category("All","")
      if(localStorage.getItem('cart_items')){
            cart_items = JSON.parse(localStorage.getItem('cart_items'));
            addCartToHTML();
        }
    })
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
      <ul class="grid grid-cols-4 gap-5">
        {#each list_items as list_item}
            {#if list_item.Stock > 0}
              <button on:click={addItem(list_item.ItemID)}>
                <li class="w-56 h-56 bg-gray-600 flex-rowtext-white justify-center text-center border-2 items-center rounded-lg hover:scale-105">
                  <div class="min-w-56 min-h-48 rounded-lg">
                    <!-- svelte-ignore a11y-missing-attribute -->
                    <img style="screen" src="http://localhost:8000/api/getfile/{list_item.ItemID}" sizes="(max-width:224px)"
                      class="bg-contain w-56 h-48"
                    />
                  </div>
                  <p id ="image"class="justify-center font-BlackOpsOne text-xl">{list_item.Name} | {list_item.Price.toLocaleString()}</p>
                </li>
              </button>
          {/if}
        {/each}
      </ul>
    </div>
     
  </div>
  <div id ="cartPage"class="flex flex-col w-1/3 bg-white rounded-xl">
    <p class="text-violet-900 text-4xl font-BlackOpsOne mx-auto h-14 mt-5">My cart</p>
    <div id = "cart_list" class = "bg-gray-300 h-4/5">

    </div>
  </div>  
</div>
  
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div on:keydown={close}>
  <ModalItem {status} on:keydown={close} />
</div>