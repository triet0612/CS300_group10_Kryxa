<script>
    import AdminNav from "$lib/components/AdminNav.svelte"
    import {ImageItem} from "$lib/Assets.js"
    import {MainScreen} from '$lib/Assets.js'
    import {Item} from "$lib/Item.js"
    import { onMount } from "svelte"
    
    let item = new Item(-1, "", 0, "", "", 0)
    onMount(async ()=>{
        const urlSearchParams = new URLSearchParams(window.location.search).get("item_id");
        console.log("Requested item ID: " + urlSearchParams)
        item = await item.getItemByID(urlSearchParams).then(res => res)
    })

    async function save_item(){
        await item.updateItem().then(res => res)
    }

</script>


<div 
    class="flex h-full w-full bg-cover bg-fixed"
    style="background-image: url({MainScreen['Background2']});">
    <div class="w-fit">
        <AdminNav></AdminNav>
    </div>
    <div class="w-full">
        <div class="w-fit h-fit flex flex-row">
            <!-- svelte-ignore a11y-img-redundant-alt -->
            <img src="http://localhost:8000/api/admin/getfile/{item.ItemID}" alt="Item Image" class="w-96 h-96">
            <div class="flex flex-col w-96">
                <label class="grid grid-flow-row h-fit w-full">
                    <span class="text-slate-200 text-3xl">
                        Name
                    </span>
                    <input 
                        type="text" 
                        value={item.Name}
                        class="h-fit w-full border-2 border-[#facc15] rounded-lg text-2xl text-[#BA7000] whitespace-nowrap"/>
                </label>

                <label class="grid grid-flow-row h-fit w-full">
                    <span class="text-slate-200 text-3xl">
                        Price
                    </span>
                    <input 
                        type="number" 
                        value={item.Price}
                        class="h-fit w-full border-2 border-[#facc15] rounded-lg text-2xl text-[#BA7000] whitespace-nowrap"/>
                </label>

                <label class="grid grid-flow-row h-fit w-full">
                    <span class="text-slate-200 text-3xl">
                        Category
                    </span>
                    <select class="h-full w-full border-2 border-[#facc15] rounded-lg text-2xl text-[#BA7000]" bind:value={item.Category}>
                        <option item.Category="Time" >Time</option>
                        <option item.Category="Food" >Food</option>
                        <option item.Category="Drink" >Drink</option>
                    </select>
                </label>

                <label class="grid grid-flow-row h-fit w-full">
                    <span class="text-slate-200 text-3xl">
                        Stock
                    </span>
                    <input 
                        type="text"
                        value={item.Stock}
                        class="h-fit w-full border-2 border-[#facc15] rounded-lg text-2xl text-[#BA7000] whitespace-nowrap"/>
                </label>

            </div>
        </div>
    </div>
    
</div>
