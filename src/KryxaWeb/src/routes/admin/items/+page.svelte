<script>
  import AdminNav from "$lib/components/AdminNav.svelte";
  import {Item,fetch_all,fetch_category} from '$lib/Item.js';
  import { onMount } from "svelte";
  import {MainScreen} from '$lib/Assets.js';
  import ModalItem from "$lib/components/ModalItem.svelte";

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
  //Auto pull db
  onMount(async () => {
      list_items = await fetch_all().then(res => res);
  })
  // pull data on request
  async function search_al(){
    list_items = await fetch_category(category_filter,text_input)
  }

</script>


<div class="flex flex-row h-100% bg-cover font-BlackOpsOne" style="background-image: url({MainScreen['Background4']});">
  <div class = "flex flex-col">
    <AdminNav/>
  </div>
  <!-- View Page -->
  <div class="h-full w-full">
    <!-- Search bar -->
    <div class="m-5">
      <div class="flex flex-row">
        <!-- Input type check -->
        <input 
          type="text" 
          id="search" 
          placeholder="Search items..." 
          class="mt-5 px-5 py-5 rounded-3xl" 
          bind:value = {text_input} 
          on:change={search_al}
        />
        <!-- Drop down -->
        <select name="category" id="category" class="mt-5 ml-5 px-5 py-5 rounded-3xl" bind:value={category_filter} on:change={search_al}>
          <option category_filter="All" selected>All</option>
          <option category_filter="Time" >Time</option>
          <option category_filter="Food" >Food</option>
          <option category_filter="Drink" >Drink</option>
        </select> 
      </div>
    </div>
    <!-- End search bar -->
    <div class="pl-5 h-5/6 overflow-y-scroll no-scrollbar">
      <ul class="grid grid-cols-5 gap-5">
        <div class="w-56 h-56">
          <button on:click={openModal} class="w-56 h-48">
            <img src={MainScreen["addItem"]} alt="cover" />
          </button>
          <div class="">Add Item</div>
        </div>
        {#each list_items as list_item}
          <li class="w-56 h-auto flex-row text-white justify-center text-center border-2 items-center backdrop-blur-2xl rounded-lg {list_item.Stock >0
          ? 'bg-green-600 bg-opacity-75'
          :'bg-red-600 bg-opacity-75'}">
            <a href="/admin/items/detail?item_id={list_item.ItemID}">
              <div class="min-w-56 min-h-48 rounded-lg">
                <!-- svelte-ignore a11y-missing-attribute -->
                <img style = "screen" src="http://localhost:8000/api/admin/getfile/{list_item.ItemID}" sizes="(max-width:224px)"
                  class="bg-contain w-56 h-48 rounded-lg p-5"
                  />
              </div>
            </a>
            <div class="bg-gray-800">
              <p id ="image"class="justify-center" value={list_item.Name}>{list_item.Name}</p>
              <p id ="image"class="justify-center" value={list_item.Name}>{parseInt(list_item.Price/1000)}.000</p>
            </div>
          </li>
        {/each}
        </ul> 
    </div>
  </div>
</div>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<div on:keydown={close}>
  <ModalItem {status} on:keydown={close} />
</div>