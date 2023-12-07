<script>
  import CustomerNav from "$lib/components/CustomerNav.svelte";

  import { user_fetch_category } from "$lib/Item.js";
  import { UserAssets,Trash } from "$lib/Assets.js";
  import ModalItem from "$lib/components/ModalItem.svelte";
  import { onMount } from "svelte";


  let list_items = [];
  let list_all_items = [];
  let cart_items = [];
  let text_input = "";
  let status = "close";
  let filter = "All";
  let listCartHTML = document.getElementById("cart_list");
  

  function addItem(ItemID) {
    let positionThisProductInCart = cart_items.findIndex(
      (value) => value.ItemID == ItemID,
    );
    console.log(positionThisProductInCart);
    if (cart_items.length <= 0) {
      cart_items = [
        {
          ItemID: ItemID,
          quantity: 1,
        },
      ];
    } else if (positionThisProductInCart < 0) {
      cart_items.push({
        ItemID: ItemID,
        quantity: 1,
      });
    } else {
      cart_items[positionThisProductInCart].quantity =
        cart_items[positionThisProductInCart].quantity + 1;
    }
    addCartToHTML();
    addCartToMemory();
    console.log(cart_items);
  }

  function addCartToMemory() {
    localStorage.setItem("cart_items", JSON.stringify(cart_items));
  }

  function addCartToHTML() {
    let total_price = document.getElementById("total_price")
    let total_quantity = document.getElementById("total_quantity")
    listCartHTML.innerHTML = "";
    let totalQuantity = 0;
    let totalPrice = 0;
    if (cart_items.length > 0) {
      cart_items.forEach((item) => {
        totalQuantity = totalQuantity + item.quantity;
        
        let newItem = document.createElement("div");
        newItem.classList.add("item");
        newItem.dataset.id = item.ItemID;

        let positionProduct = list_all_items.findIndex(
          (value) => value.ItemID == item.ItemID,
        );
        let info = list_all_items[positionProduct];
        totalPrice = totalPrice + info.Price * item.quantity
        listCartHTML.appendChild(newItem);
        newItem.innerHTML = `
                <div class = "flex flex-row bg-white/80 border-b-2 h-1/2 h-20 w-11/12 mx-auto">
                  <img style="screen" src="http://localhost:8000/api/getfile/${
                    info.ItemID
                  }" sizes="(max-width:20px)"
                      class="bg-contain rounded-full ml-5 h-14 my-auto w-14"
                    />
                  <div class = "flex flex-col ml-3 mt-2 w-32">
                    <div class="text-[#FF9900] text-xl font-BlackOpsOne">
                    ${info.Name}
                    </div>
                    <div class="text-[#FF9900] text-xl font-BlackOpsOne mt-3">$${
                      info.Price * item.quantity
                    }</div>
                  </div>
                  <div class="flex flex-row my-auto ml-12">
                    <button class="minus rounded-full w-7 h-7 bg-gray-300">-</button>
                    <span class = "ml-3 mr-3 ">${item.quantity}</span>
                    <button class="plus rounded-full w-7 h-7 bg-gray-300">+</button>
                  </div>
                </div>
            `;
      });
    }
    total_price.textContent = totalPrice+'đ'
    total_quantity.textContent = totalQuantity + ' items'
  }

  

  function add_click(){
    listCartHTML.addEventListener("click", (event) => {
    let positionClick = event.target;
    if (
      positionClick.classList.contains("minus") ||
      positionClick.classList.contains("plus")
    ) {
      let ItemID = positionClick.parentElement.parentElement.parentElement.dataset.id;
      let type = "minus";
      if (positionClick.classList.contains("plus")) {
        type = "plus";
      }
      changeQuantityCart(ItemID, type);
    }
  });
  }

  function changeQuantityCart(ItemID, type) {
    console.log(ItemID);
    let positionItemInCart = cart_items.findIndex(
      (value) => value.ItemID == ItemID,
    );
    if (positionItemInCart >= 0) {
      let info = cart_items[positionItemInCart];
      switch (type) {
        case "plus":
          cart_items[positionItemInCart].quantity =
            cart_items[positionItemInCart].quantity + 1;
          break;

        default:
          let changeQuantity = cart_items[positionItemInCart].quantity - 1;
          if (changeQuantity > 0) {
            cart_items[positionItemInCart].quantity = changeQuantity;
          } else {
            cart_items.splice(positionItemInCart, 1);
          }
          break;
      }
    }
    addCartToHTML();
    addCartToMemory();
  }
  function clearCart(){
    cart_items = []
    addCartToHTML();
    addCartToMemory();
  }
  onMount(async () => {
    listCartHTML = document.getElementById("cart_list");
    add_click()
    list_all_items = await user_fetch_category("All", "");
    if (localStorage.getItem("cart_items")) {
      cart_items = JSON.parse(localStorage.getItem("cart_items"));
      addCartToHTML();
    }
  });
  // pop up
  function close(event) {
    if (event.key === "Escape") {
      status = "close";
    }
  }

  function openModal(event) {
    status = "open";
  }

  async function search_all(filter, text_input) {
    list_items = await user_fetch_category(filter, text_input);
    console.log(list_items);
  }

  $: {
    search_all(filter, text_input);
  }
</script>

<div
  id="bg"
  class="flex flex-row h-screen bg-cover {status === 'open' ? 'blur-3xl' : ''} "
  style="background-image: url({UserAssets['ItemsBackground']});"
>
  <div class="flex flex-col">
    <CustomerNav bind:filter_value={filter} />
  </div>
  <div class="flex flex-col h-full w-full p-10">
    <div class="flex flex-row justify-between">
      <div class="flex flex-row">
        <input
          type="text"
          placeholder="Search items..."
          class="p-5 placeholder-black rounded-3xl font-BlackOpsOne text-2xl bg-[#FF9900] text-black"
          bind:value={text_input}
        />
      </div>
      <div
        class="flex flex-row bg-red-600 p-3 rounded-2xl hover:cursor-pointer hover:drop-shadow-xl hover:bg-gradient-to-r hover:from-[#FF0202] hover:to-[#FF9900]"
      >
        <img src={UserAssets.CartIcon} alt="cart icon" />
        <p class="text-5xl text-white font-BlackOpsOne self-center">Cart</p>
      </div>
    </div>
    <div class="p-5 h-full overflow-y-hidden">
      <ul class="grid grid-cols-4 gap-5">
        {#each list_items as list_item}
          {#if list_item.Stock > 0}
            <button on:click={addItem(list_item.ItemID)}>
              <li
                class="w-56 h-56 bg-green-600 bg-opacity-75 flex-rowtext-white justify-center text-center border-2 items-center rounded-lg hover:scale-105"
              >
                <div class="min-w-56 min-h-48 rounded-lg">
                  <!-- svelte-ignore a11y-missing-attribute -->
                  <img
                    style="screen"
                    src="http://localhost:8000/api/getfile/{list_item.ItemID}"
                    sizes="(max-width:224px)"
                    class="bg-contain w-56 h-48"
                  />
                </div>
                <p id="image" class="justify-center font-NotoSans text-xl text-white">
                  {list_item.Name} | {list_item.Price.toLocaleString()}
                </p>
              </li>
            </button>
          {/if}
        {/each}
      </ul>
    </div>
  </div>
  <div id="cartPage" class="flex flex-col w-1/3 bg-white rounded-xl">
    <div class = "flex flex-row">
      <p class="text-[#FF9900] text-4xl border-b-2 font-BlackOpsOne mx-auto h-14 mt-5">
        My cart
      </p>
      <button on:click={clearCart} class = "w-10">
        <img src={Trash} alt="">
      </button>
    </div>
    
    <div id="cart_list" class="overflow-auto h-2/3"></div>
    <div class = "bg-gray-400 w-11/12 mx-auto rounded-3xl">
      <div class = "border-b-4 border-black">
        <div class ="flex flex-row">
          <div id = "" class = " text-2xl font-NotoSans mt-8 ml-3 ">
            Total items: 
          </div>
          <div id = "total_quantity" class = "text-2xl font-NotoSans mt-8 ">
            0 items
          </div>
        </div>
        <div class ="flex flex-row">
          <p id="" class = "text-2xl font-NotoSans mt-4 ml-3 ">
            Total price: 
          </p>
          <p id="total_price" class = "text-green-900 text-2xl font-NotoSans mt-4 ml-5 ">
            $0
          </p>
        </div>
        
      </div>
      
      <button class="bg-amber-400 h-20 mb-5 rounded-xl flex flex-col items-center justify-center mx-auto w-11/12 text-3xl mt-3 font-NotoSans font-bold">
        Check Out
      </button>
    </div>
    
    
    
    
  </div>
</div>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<div on:keydown={close}>
  <ModalItem {status} on:keydown={close} />
</div>
