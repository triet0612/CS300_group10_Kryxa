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
        if (files != undefined)
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
        // window.location.replace("/admin/items")
    } 

</script>

<div 
    class="flex h-full w-full bg-cover bg-fixed"
    style="background-image: url({MainScreen['Background2']});">
    <div class="w-fit">
        <AdminNav></AdminNav>
    </div>
    <div class="w-fit h-3/4 place-self-center p-16 ml-12 border-4 bg-gradient-to-b from-[#342267] black">
        <div class="w-fit h-fit grid grid-cols-3">
            <div class="w-full h-fit flex flex-col gap-y-3 col-span-2">
                <label class="grid grid-flow-row h-fit w-full pr-4">
                    <span class="text-slate-200 text-3xl">
                        Name
                    </span>
                    <input 
                        type="text" 
                        bind:value={item.Name}
                        class="h-fit w-full focus:{"border-2 border-[#facc15] outline-amber-500"} rounded-lg text-2xl text-[#BA7000] whitespace-nowrap"/>
                </label>
                <div class="w-fit h-fit grid grid-flow-col">
                    <div class="w-[255px] h-fit grid grid-flow-row gap-y-4">
                        <!-- svelte-ignore a11y-img-redundant-alt -->
                        <img src="http://localhost:8000/api/admin/getfile/{item.ItemID}" alt="Item Image" class="w-[255px] h-[255px]">
                        <input bind:files class="w-full h-fit my-1 mx-1 bg-white rounded-xl text-left" type="file" accept="image/png, image/jpeg">
                    </div>
                    <div class="h-fit grid grid-flow-row gap-y-4 mx-4">
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
                </div>
                
            </div>
            <div class="flex flex-col h-fit w-full mx-14 px-4 gap-y-3 place-self-center">
                <button class=" h-fit w-full bg-white 
                            ring ring-green-500
                            hover:{"bg-gradient-to-r from-green-500 to-cyan-500"}
                            text-2xl text-green-500
                            hover:text-white" 
                            on:click={update_current_item}>
                    Edit
                </button>
                <button class="h-fit w-full bg-white 
                            ring ring-red-500
                            hover:{"bg-gradient-to-r from-red-500 to-pink-500 text-white"}
                            text-2xl text-red-500
                            hover:text-white"
                            on:click={delete_current_item}>
                    Delete
                </button>
            </div>
        </div>
    </div>
</div>
