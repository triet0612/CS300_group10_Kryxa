<script>
    import AdminNav from "$lib/components/AdminNav.svelte";
    import {ImageItem} from "$lib/Assets.js"
    import {Item} from "$lib/Item.js"
    import { onMount } from "svelte";
    // console.log(urlSearchParams.get("item_id"))
    
    let item = new Item(-1, "", 0, "", "", 0)
    onMount(async ()=>{
        const urlSearchParams = new URLSearchParams(window.location.search).get("item_id");
        console.log("Requested item ID: " + urlSearchParams)
        item = await item.getItemByID(urlSearchParams).then(res => res)
    })
    console.log(item.ID)
    console.log(item.Name)
    console.log(item.Price)
    console.log(item.Category)
    console.log(item.ItemStatus)
    console.log(item.Stock)

</script>

<div class="bg-gradient-to-b from-black to-yellow-600 flex flex-row">
    <div class="flex flex-col">
        <AdminNav></AdminNav>
    </div>
    <div class="w-full flex content-center">
        <div id="detail-box" class="flex flex-row border-4 border-[#facc15] rounded-lg bg-none my-auto mx-auto h-3/4 w-3/4">
            <div id="item-detail-box-info" class="rounded-l-lg ml-0 h-full w-2/3 text-black">
                {#if !item.Name}
                    <script>
                        console.log("Svelte#if: There is no item with such ID")
                    </script>
                    <p class="text-white"> There is no item with such ID, please return to previous page. *This message will be updated later*</p>
                {:else}
                    <div class="grid grid-flow-col grid-cols-2 gap-0 items-stretch h-1/2 w-full">
                        <div class = "h-full">
                            <img src={ImageItem[item.Name]} alt="selected item image" class="max-w-full max-h-full"/>
                        </div>
                        <div class = "grid grid-flow-row place-content-center gap-4 h-full bg-none">
                            <label class="grid grid-flow-row place-content-center h-fit mx-auto w-9/10">
                                <span class="text-slate-200 text-3xl">
                                    Item Name
                                </span>
                                <input type="text" value={item.Name} name="Item Name"
                                    class="h-fit w-full border-2 border-[#facc15] rounded-lg text-2xl text-[#BA7000] whitespace-nowrap"/>
                            </label>
                            
                            <label class="grid grid-flow-row place-content-center h-fit mx-auto w-9/10">
                                <span class="text-slate-200 text-3xl">
                                    Price
                                </span>
                                <input type="number" value={item.Price} 
                                class="h-fit mx-auto w-full border-2 border-[#facc15] rounded-lg text-2xl text-[#BA7000] whitespace-nowrap"/>
                            </label>

                        </div>
                    </div>
                    <div class="grid grid-flow-row grid-cols-1 h-1/2 w-full">
                        <label class="h-3/4 w-3/4 mt-16 mx-auto text-slate-200 text-3xl">
                            Description
                            <input type="text" value={item.ItemStatus} 
                                class="h-full w-full border-2 border-[#facc15] rounded-lg text-2xl text-[#BA7000] text-start  whitespace-pre-line"/>
                        </label>
                        <button name="edit_item_button" type="button" value="Edit" 
                                class="self-end mb-10 mx-auto text-orange-400 text-2xl whitespace-nowrap bg-white w-11/12 h-fit">
                            Edit
                        </button> 
                    </div>
                {/if}
            </div>
            <div id="item-detail-box-kryxa-img" class="rounded-r-lg bg-black mr-0 h-full w-1/3 text-white">
                <p> Kryxa image here</p>
            </div>
            
        </div>
    </div>
</div>
