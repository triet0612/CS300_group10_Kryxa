<script>
  import AdminNav from "$lib/components/AdminNav.svelte";
  import {ImageItem} from '$lib/Assets.js';
  import {fetch_all,fetch_category} from '$lib/Item.js';
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
      console.log(list_items);
  })
  // pull data on request
  async function search_al(){
    list_items = await fetch_category(category_filter,text_input)
    console.log(list_items)
  }

</script>

<div id="bg"
class=" fixed h-full w-full bg-cover {status === 'open' ? 'blur-3xl' : ''} "
style="background-image: url({MainScreen['Background2']});">
  <!-- Nav Bar -->
    <div class="fixed">
        <AdminNav/>
    </div>
    <!-- View Page -->
    <div class="flex flex-col ml-72 h-screen">
      <!-- Search bar -->
      <div class="fixed z-10">
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
      <div class="mt-32 pl-5 overflow-y-scroll">
        <ul class="grid grid-cols-5 gap-5">
          <div class=" w-56 h-56">
            <button on:click={openModal} class="w-56 h-48">
              <img src={MainScreen["addItem"]} alt="cover" />
            </button>
            <div class="">Add Item</div>
          </div>
          {#each list_items as list_item}
            <li class="w-56 h-56 flex-row text-white justify-center text-center border-2 items-center backdrop-blur-2xl">
              <a href="/admin/items/detail?item_id={list_item.ItemID}">
                <div class="min-w-52 min-h-48 bg-gray-600 ml-1.5">
                  <img src = {
                    ImageItem[list_item.Name]}
                    alt="screen"
                    class="bg-contain w-56 h-48 justify-center"
                    />
                </div>
              </a>
              <p id ="image"class="justify-center" value={list_item.Name}>{list_item.Name} : {list_item.Price}</p>
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