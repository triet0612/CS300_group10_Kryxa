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
        let upd_statcode = await update_item(item).then(res => res)
        let upd_img_statcode = await createImage(files, item.ItemID).then(res => res)

        if (upd_statcode != 200){
            console.log("Item update failed")
        }

        if (upd_img_statcode != 200){
            console.log("Item image update failed")
        }

        console.log(item)
        location.reload()
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


<div class="flex flex-row h-screen bg-cover font-BlackOpsOne" style="background-image: url({MainScreen['Background4']});">
    <div class = "flex flex-col">
      <AdminNav/>
    </div>
    <!-- View Page -->
    <div class="flex h-screen w-full">
        <div class="w-fit h-fit m-auto place-self-center p-16 border-2 rounded-lg {"bg-gradient-to-b from-[#342267] to-black"}/30">
            <div class="grid grid-cols-3">
                <div class="flex flex-col gap-y-3 col-span-2">
                    <label class="grid grid-flow-row h-fit w-full pr-4">
                        <input 
                            type="text" 
                            placeholder="Name"
                            bind:value={item.Name}
                            class="h-fit w-full bg-[#160425]/75 rounded-lg whitespace-nowrap
                            indent-2.5 text-4xl text-[#BA7000] leading-relaxed font-BlackOpsOne
                            placeholder:italic placeholder:text-[#BA7000]
                            focus:outline-none focus:ring-2 focus:ring-[#BA7000]"/>
                    </label>
                    <div class="w-fit h-fit grid grid-flow-col">
                        <div class="w-[255px] h-fit grid grid-flow-row gap-y-4">
                            <!-- svelte-ignore a11y-img-redundant-alt -->
                            <img src="http://localhost:8000/api/admin/getfile/{item.ItemID}" alt="Item Image" class="w-[255px] h-[255px]">
                            <input bind:files class="w-full h-fit my-1 mx-1 bg-white rounded-xl text-left" type="file" accept="image/png, image/jpeg">
                        </div>
                        <div class="h-fit grid grid-flow-row gap-y-10 mx-4">
                            <label class="grid grid-flow-row h-fit w-full">
                                <input 
                                    type="number"
                                    placeholder="Price"
                                    bind:value={item.Price}
                                    class="h-fit w-full bg-[#160425]/75 rounded-lg whitespace-nowrap
                                    indent-2.5 text-3xl text-[#BA7000] leading-relaxed font-BlackOpsOne
                                    placeholder:italic placeholder:text-[#BA7000]
                                    focus:outline-none focus:ring-2 focus:ring-[#BA7000]"/>
                            </label>
            
                            <label class="grid grid-flow-row h-fit w-full">
                                <select class="h-fit w-full bg-[#160425]/75 rounded-lg whitespace-nowrap
                                indent-2.5 text-3xl text-[#BA7000] leading-relaxed font-BlackOpsOne
                                placeholder:italic placeholder:text-[#BA7000]
                                focus:outline-none focus:ring-2 focus:ring-[#BA7000]"
                                 bind:value={item.Category}>
                                    <option item.Category="Time" class="text-3xl focus:outline-none focus:ring-2 focus:ring-[#BA7000]" >Time</option>
                                    <option item.Category="Food" class="text-3xl focus:outline-none focus:ring-2 focus:ring-[#BA7000]">Food</option>
                                    <option item.Category="Drink" class="text-3xl focus:outline-none focus:ring-2 focus:ring-[#BA7000]">Drink</option>
                                </select>
                            </label>
            
                            <label class="grid grid-flow-row h-fit w-full">
                                <input 
                                    type="number"
                                    placeholder="Stock"
                                    bind:value={item.Stock}
                                    class="h-fit w-full bg-[#160425]/75 rounded-lg whitespace-nowrap
                                    indent-2.5 text-3xl text-[#BA7000] leading-relaxed font-BlackOpsOne
                                    placeholder:italic placeholder:text-[#BA7000]
                                    focus:outline-none focus:ring-2 focus:ring-[#BA7000]"/>
                            </label>
                        </div>
                    </div>
                    
                </div>
                <div class="flex flex-col h-fit w-full mx-14 px-4 gap-y-3 place-self-center">
                    <button class=" h-fit w-full {"bg-gradient-to-b from-[#160425] to-black"}/75
                                rounded-lg
                                text-3xl text-[#BA7000] leading-relaxed font-BlackOpsOne
                                hover:bg-gradient-to-b hover:from-[#160425] hover:to-cyan-500/75" 
                                on:click={update_current_item}>
                        Edit
                    </button>
                    <button class=" h-fit w-full {"bg-gradient-to-b from-[#160425] to-black"}/75
                                rounded-lg
                                text-3xl text-[#BA7000] leading-relaxed font-BlackOpsOne
                                hover:bg-gradient-to-b hover:from-[#160425] hover:to-pink-500/75" 
                                on:click={delete_current_item}>
                        Delete
                    </button>
                </div>
            </div>
        </div>
    </div>
    
</div>
