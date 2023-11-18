<script>
    import AdminNav from "$lib/components/AdminNav.svelte"
    import {MainScreen} from '$lib/Assets.js'
    import {Item, update_item, delete_item, createImage} from "$lib/Item.js"
    import { onMount } from "svelte"
    import ModalItem from "$lib/components/ModalItem.svelte"
    
    let item = new Item(-1, "", 0, "", "", 0)
    let files = undefined
    onMount(async ()=>{
        const urlSearchParams = new URLSearchParams(window.location.search).get("item_id");
        console.log("Requested item ID: " + urlSearchParams)
        item = await item.getItemByID(urlSearchParams).then(res => res)
    })

    async function update_current_item(){
        await update_item(item).then(res => res)
        await createImage(files, item.ItemID).then(res => res)
        console.log(item)
        window.location.reload()
    }

    async function delete_current_item(){
        let del_statcode = await delete_item(item.ItemID).then(res => res)
        if (del_statcode != 200){
            console.log("Item deletion failed")
        }
        console.log("Delete item called")
        window.location.replace("/admin/items")
    } 

</script>

<div 
    class="flex h-full w-full bg-cover bg-fixed"
    style="background-image: url({MainScreen['Background2']});">
    <div class="w-fit">
        <AdminNav></AdminNav>
    </div>
    <div class="w-3/4 h-3/4 place-self-center p-3 ml-12 border-4">
        <div class="w-fit h-fit flex flex-row">
            <!-- svelte-ignore a11y-img-redundant-alt -->
            <div class="w-fit h-fit flex flex-col gap-y-3">
                <img src="http://localhost:8000/api/admin/getfile/{item.ItemID}" alt="Item Image" class="w-[480px] h-[480px]">
                <input bind:files class="my-1 mx-1 bg-white rounded-xl text-left" type="file" accept="image/png, image/jpeg">
            </div>
            <div class="flex flex-col gap-y-16">
                <div class="flex flex-col w-96 mx-14 gap-y-3">
                    <label class="grid grid-flow-row h-fit w-full">
                        <span class="text-slate-200 text-3xl">
                            Name
                        </span>
                        <input 
                            type="text" 
                            bind:value={item.Name}
                            class="h-fit w-full focus:{"border-2 border-[#facc15] outline-amber-500"} rounded-lg text-2xl text-[#BA7000] whitespace-nowrap"/>
                    </label>
    
                    <label class="grid grid-flow-row h-fit w-full">
                        <span class="text-slate-200 text-3xl">
                            Price
                        </span>
                        <input 
                            type="number" 
                            bind:value={item.Price}
                            class="h-fit w-full focus:{"border-2 border-[#facc15] outline-amber-500"} rounded-lg text-2xl text-[#BA7000] whitespace-nowrap"/>
                    </label>
    
                    <label class="grid grid-flow-row h-fit w-full">
                        <span class="text-slate-200 text-3xl">
                            Category
                        </span>
                        <select class="h-full w-full focus:{"border-2 border-[#facc15] outline-amber-500"} rounded-lg text-2xl text-[#BA7000]" bind:value={item.Category}>
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
                            type="number"
                            bind:value={item.Stock}
                            class="h-fit w-full focus:{"border-2 border-[#facc15] outline-amber-500"} rounded-lg text-2xl text-[#BA7000] whitespace-nowrap"/>
                    </label>
                </div>
                <div class="flex flex-col mx-14 gap-y-3">
                    <button class=" h-fit w-full bg-white 
                                ring ring-green-500
                                hover:{"bg-gradient-to-r from-green-500 to-cyan-500"}" 
                                on:click={update_current_item}>
                        Edit
                    </button>
                    <button class="h-fit w-full bg-white 
                                ring ring-red-500
                                hover:{"bg-gradient-to-r from-red-500 to-pink-500"}"
                                on:click={delete_current_item}>
                        Delete
                    </button>
                </div>
            </div>
            
        </div>
    </div>
</div>
