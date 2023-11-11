<script>
    import AdminNav from "$lib/components/AdminNav.svelte";
    import {ImageItem} from '$lib/Assets.js';
    import {Item, fetch_all,fetch_category} from '$lib/Item.js';
    import { onMount } from "svelte";
    import {MainScreen} from '$lib/Assets.js';
    let list_items = []
    onMount(async () => {
        list_items = await fetch_all().then(res => res);
        console.log(list_items);
    })
    
    async function search_al(){
      var x = document.getElementById("image");
      var na = x.value.toUpperCase();
      var y = document.getElementById("search")
      var us = y.value.toUpperCase();

      console.log(na)

    }

    async function filter(){
      var x = document.getElementById("category");
      var cate = x.value;
      switch(cate){
        case 'All':
          list_items = await fetch_all().then(res=>res);
          console.log(list_items);
          break;
        case 'Drink':
          list_items = await fetch_category('Drink').then(res=>res);
          console.log(list_items);
          break;
        case 'Food':
          list_items = await fetch_category('Food').then(res=>res);
          console.log(list_items);
          break;
        case 'Time':
          list_items = await fetch_category('Time').then(res=>res);
          console.log(list_items);
          break;
      }
    }

    
</script>

<div id="bg"class=" fixed h-full w-full bg-cover"style="background-image: url({MainScreen['Background2']});">
    <div class="fixed">
        <AdminNav/>
    </div>
    <div class="flex flex-col ml-72 h-screen">
      <div class="fixed z-10">
        <div class="flex flex-row">
          <input type="text" id="search" placeholder="Seach items..." class="mt-5 px-5 py-5 rounded-3xl" value = ""/>
          <select name="category" id="category" class="mt-5 ml-5 px-5 py-5 rounded-3xl" on:change={filter}>
            <option value="All" selected>All</option>
            <option value="Time" >Time</option>
            <option value="Food" >Food</option>
            <option value="Drink" >Drink</option>
          </select> 
        </div>
      </div>
      <div class="mt-32 pl-5 overflow-y-scroll">
        <ul class="grid grid-cols-5 gap-5">
          {#each list_items as list_item}
            <li class="w-56 h-56 flex-row text-white justify-center text-center border-2 items-center backdrop-blur-2xl">
              <div class="w-52 h-48 bg-gray-600 ml-1.5"  >
                <img src = {
                  ImageItem[list_item.Name]}
                  alt="screen"
                  class="bg-contain w-56 h-48 justify-center"s
                  />
              </div>
              <p id ="image"class="justify-center" value={list_item.Name}>{list_item.Name} : {list_item.Price}</p>
            </li>
          {/each}
          </ul>
      </div>
    </div>
  </div>
