<script>
    import AdminNav from "$lib/components/AdminNav.svelte";
    let list_items=[
      {ItemID: 1, Name: "Com ga 1", ItemStatus: "On sale"},
      {ItemID: 2, Name: "Com ga 2", ItemStatus: "Depricated"},
      {ItemID: 3, Name: "Com ga 3", ItemStatus: "On sale"},
      {ItemID: 4, Name: "Com ga 4", ItemStatus: "On sale"},
      {ItemID: 5, Name: "Com ga 5", ItemStatus: "On sale"},
      {ItemID: 6, Name: "Com ga 6", ItemStatus: "Depricated"},
      {ItemID: 7, Name: "Com ga 7", ItemStatus: "Depricated"},
      {ItemID: 8, Name: "Com ga 8", ItemStatus: "On sale"},
    ]
</script>

<div class="bg-gradient-to-b from-black to-yellow-600">
    <div class="gap-5 flex w-screen">
        <AdminNav></AdminNav>
        <div class="flex-row w-screen">
            <div class="gap-20 flex pl-8 ">
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
            <div class="pt-5 pl-20 w-11/12 h-screen border-2 mx-9">
              <div class="grid grid-flow-row grid-cols-4">
                {#each list_items as list_item}
                <li>
                  <div class="w-56 h-56 flex-row text-white justify-center text-center">
                    <div class="w-56 h-48 bg-gray-600 justify-center "></div>
                    <p class="justify-center">{list_item.Name}</p>
                  </div>
                </li>
                {/each}
              </div>
            </div>
        </div>
    </div>
  </div>
