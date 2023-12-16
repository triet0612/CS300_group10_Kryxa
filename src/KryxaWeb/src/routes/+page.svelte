<script>
  import CustomerNav from "$lib/components/CustomerNav.svelte";

  import { user_fetch_category } from "$lib/Item.js";
  import { UserAssets, Trash, AppLogo } from "$lib/Assets.js";
  import { getBillbyID, Bill, update_user_bill } from "$lib/Bill.js";
  import ModalItem from "$lib/components/ModalItem.svelte";
  import { onMount } from "svelte";

  let list_items = [];
  let list_all_items = [];
  let cart_items = [];
  let bill = new Bill();
  let text_input = "";
  let status = "close";
  let filter = "All";
  let listCartHTML = document.getElementById("cart_list");
  let billHTML;
  let bill_items = [];

  function addItem(ItemID) {
    let positionThisProductInCart = cart_items.findIndex(
      (value) => value.ItemID == ItemID,
    );
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
  }

  function addCartToMemory() {
    localStorage.setItem("cart_items", JSON.stringify(cart_items));
  }

  function addCartToHTML() {
    let total_price = document.getElementById("total_price");
    let total_quantity = document.getElementById("total_quantity");
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
        totalPrice = totalPrice + info.Price * item.quantity;
        listCartHTML.appendChild(newItem);
        newItem.innerHTML = `
                <div class = "font-NotoSans font-semibold flex flex-row bg-white/80 border-b-2 h-32 w-11/12 mx-auto">
                  <img style="screen" src="http://localhost:8000/api/getfile/${
                    info.ItemID
                  }" sizes="(max-width:20px)"
                      class="bg-contain rounded-full ml-5 h-14 my-auto w-14"
                    />
                  <div class = "flex flex-col ml-3 mt-5 w-full">
                    <div class="text-[#FF9900] text-xl">
                    ${info.Name}
                    </div>
                    <div class = "flex flex-row mt-5">
                      <div class="text-[#FF9900] text-xl">$${
                        info.Price * item.quantity
                      }</div>
                      <div class="flex flex-row my-auto ml-40 w-1/2">
                        <button class="minus rounded-full w-7 h-7 bg-gray-300">-</button>
                        <span class = "ml-3 mr-3 ">${item.quantity}</span>
                        <button class="plus rounded-full w-7 h-7 bg-gray-300">+</button>
                    </div>
                    </div>
                  </div>
                </div>
            `;
      });
    }
    total_price.textContent = totalPrice + "đ";
    total_quantity.textContent = totalQuantity + " items";
  }

  function add_click() {
    listCartHTML.addEventListener("click", (event) => {
      let positionClick = event.target;
      if (
        positionClick.classList.contains("minus") ||
        positionClick.classList.contains("plus")
      ) {
        let ItemID =
          positionClick.parentElement.parentElement.parentElement.dataset.id;
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

  function clearCart() {
    cart_items = [];
    addCartToHTML();
    addCartToMemory();
  }

  async function switch_tab(id) {
    let cartPage = document.getElementById("cart_page");
    let billHTML = document.getElementById("billHTML");
    let cart_btn = document.getElementById("cart_btn");
    let bill_btn = document.getElementById("bill_btn");
    if (id === 0) {
      cartPage.style.display = "block";
      billHTML.style.display = "none";
      cart_btn.style.color = "#FF9900";
      bill_btn.style.color = "#e2e8f0";
    } else {
      cartPage.style.display = "none";
      billHTML.style.display = "block";
      cart_btn.style.color = "#e2e8f0";
      bill_btn.style.color = "#FF9900";
    }
  }
  async function getBill() {
    bill = await getBillbyID();
    console.log(bill);
  }
  async function check_out() {
    if (cart_items.length > 0) {
      cart_items.forEach((item) => {
        let positionProduct = list_all_items.findIndex(
          (value) => value.ItemID == item.ItemID,
        );
        let info = list_all_items[positionProduct];
        let positionThisProductInBill = bill.Cart.findIndex(
          (value) => value.id == item.ItemID,
        );
        if (positionThisProductInBill < 0) {
          bill.Cart.push({
            id: item.ItemID,
            name: info.Name,
            qt: item.quantity,
            price: info.Price,
          });
        } else {
          bill.Cart[positionThisProductInBill].qt =
            bill.Cart[positionThisProductInBill].qt + item.quantity;
        }
      });
      let temp_food = []
      cart_items.filter((val) => val.ItemID > 1);
      for (let i = 0; i < cart_items.length; i++) {
        temp_food.push({"PcID": 0, "ItemID": cart_items[i].ItemID, "Qt": cart_items[i].quantity})
      }
      console.log(temp_food)
      let add_queue_stat = await fetch("http://localhost:8000/api/food_queue", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + localStorage.getItem("jwt")
        },
        body: JSON.stringify(temp_food)
      }).then(res => res.status).catch(err => {console.log(err); return 500})
      if (add_queue_stat !== 200) {
        alert("Error create food queue")
        return
      }
      clearCart();

      let statcode = await update_user_bill(bill).then((res) => res);
      if (statcode != 200) {
        console.log("failed to update bill");
      } else {
      }
      location.reload();
    }
  }

  function odd_even(id) {
    let positionProduct = bill.Cart.findIndex((value) => value.id == id);
    return positionProduct;
  }
  onMount(async () => {
    listCartHTML = document.getElementById("cart_list");
    add_click();
    list_all_items = await user_fetch_category("All", "");
    if (localStorage.getItem("cart_items")) {
      cart_items = JSON.parse(localStorage.getItem("cart_items"));
      addCartToHTML();
    }
    // getBill()
    bill = await getBillbyID().then((res) => res);
    console.log("cart:", bill.Cart);
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
                class="w-56 h-auto bg-green-600 bg-opacity-75 flex-rowtext-white justify-center text-center border-2 items-center rounded-lg hover:scale-105"
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
                <div class="bg-gray-900">
                  <p
                    id="image"
                    class="justify-center font-NotoSans text-xl text-white"
                  >
                    {list_item.Name}
                  </p>
                  <p
                    id="image"
                    class="justify-center font-NotoSans text-xl text-white"
                  >
                    {list_item.Price.toLocaleString()}
                  </p>
                </div>
              </li>
            </button>
          {/if}
        {/each}
      </ul>
    </div>
  </div>
  <div class="flex flex-col w-1/3 bg-white rounded-xl">
    <div class="flex flex-row">
      <button
        id="cart_btn"
        on:click={async () => {
          switch_tab(0);
        }}
        class=" text-[#FF9900] text-4xl border-2 font-BlackOpsOne mx-auto h-14 w-1/2 flex flex-col items-center justify-center rounded-t-xl"
      >
        My cart
      </button>
      <!-- <button on:click={clearCart} class = "w-10">
        <img src={Trash} alt="">
      </button> -->
      <button
        id="bill_btn"
        on:click={async () => {
          switch_tab(1);
        }}
        class="text-[#e2e8f0] text-4xl border-2 font-BlackOpsOne mx-auto h-14 w-1/2 flex flex-col items-center justify-center rounded-t-xl"
      >
        My Bill
      </button>
    </div>

    <div id="cart_page" class="w-[500px] h-full">
      <div
        id="cart_list"
        class="overflow-auto h-2/3"
        bind:this={listCartHTML}
      ></div>
      <div class="bg-gray-400 w-11/12 mx-auto rounded-3xl">
        <div class="border-b-4 border-black">
          <div class="flex flex-row mt-20">
            <div id="" class=" text-2xl font-NotoSans mt-8 ml-3">
              Total items:
            </div>
            <div id="total_quantity" class="text-2xl font-NotoSans mt-8 ml-40">
              0 items
            </div>
          </div>
          <div class="flex flex-row">
            <p id="" class="text-2xl font-NotoSans mt-4 ml-3">Total price:</p>
            <p
              id="total_price"
              class="text-green-900 text-2xl font-NotoSans mt-4 ml-40"
            >
              $0
            </p>
          </div>
        </div>
        <button
          class="bg-amber-400 h-20 rounded-xl flex flex-col items-center justify-center mx-auto w-11/12 text-3xl mt-3 mb-3 font-NotoSans font-bold"
          on:click={async () => check_out()}
        >
          Check Out
        </button>
      </div>
    </div>

    <div id="billHTML" bind:this={billHTML}>
      <div
        class="flex flex-col w-[500px] bg-white border-black border justify-center items-center"
      >
        <div
          id="title"
          class=" w-[470px] font-extrabold text-5xl mt-9 text-center"
        >
          KRYXA
        </div>
        <div
          class="w-[470px] h-[160px] border-black border mt-2 mb-2 font-NotoSans inline-flex"
        >
          <div class="w-[250px] ml-1 mt-2">
            <div class="text-black font-semibold mt-2">
              BillID : {bill.BillID}
            </div>
            <div class="text-black font-semibold mt-2">
              PcID : {bill.PcID}
            </div>
            <div class="text-black font-semibold mt-2">Datetime :</div>
            <div class="inline-flex">
              <img src={AppLogo} alt="" width="20%" />
              <div class="mt-5 ml-2 text-gray-600">since 2023</div>
            </div>
          </div>
          <div class="w-[220px] mt-2">
            <div class="mr-5 mt-2 font-semibold text-right">Note :</div>
            <textarea
              class="w-[200px] h-[100px] border-black border resize-none"
              bind:value={bill.Note}
            ></textarea>
          </div>
        </div>
        <div class="w-[470px] mb-2">
          <table class="mx-auto">
            <thead class="font-bold">
              <tr class="h-[40px]">
                <td class="w-[250px] pl-2">Item description</td><td
                  class="w-[50px]">Qt</td
                ><td class="w-[60px]">Price</td><td
                  class="w-[90px] text-right pr-2">Amount</td
                >
              </tr>
            </thead>
            <tbody>
              {#if bill.Cart !== undefined}
                {#each bill["Cart"] as item}
                  <tr
                    class=" h-[40px] {odd_even(item['id']) % 2 == 0
                      ? 'bg-white'
                      : 'bg-slate-200'} cursor-pointer transition-colors duration-300 hover:bg-green-500"
                    title="Click to remove"
                  >
                    <td class="w-[250px] pl-2">{item["name"]}</td><td
                      class="w-[50px]">{item["qt"]}</td
                    ><td class="w-[60px]">{item["price"]}</td><td
                      class="w-[90px] text-right pr-2"
                      >{item["qt"] * item["price"]}</td
                    >
                  </tr>
                {/each}
              {/if}
            </tbody>
          </table>
        </div>
        <div class="w-[470px] border-black border mt-4"></div>
        <div class="flex my-4">
          <div class="w-[235px] h-[40px] text-center">
            <div
              class="w-[230px] h-[30px] text-white text-xl bg-green-600 font-bold mr-[20px] mt-[4px]"
            >
              Total : {bill.Total}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<div on:keydown={close}>
  <ModalItem {status} on:keydown={close} />
</div>

<style>
  #billHTML {
    display: none;
  }
</style>
