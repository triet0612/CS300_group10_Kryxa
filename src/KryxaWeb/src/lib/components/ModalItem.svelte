<script>
    import {Item,createImage} from "$lib/Item.js"
    import {AppLogo} from '$lib/Assets.js'

    export let status = "close";

    let newItem = new Item();
    let files = undefined;
    
    let dialog;

    $: if (status === "open" && dialog) {
        dialog.show()
    } else if (status === "close" && dialog) {
        dialog.close()
    }

    async function click() {
        
        let statcode = await newItem.createItem().then(res => res)
        status = "close"
        if (statcode !== 200) {
            alert("Failed create new Item")
        }
        let stat = await createImage(files,newItem.ItemID).then(res => res)
        if (stat !== 200) {
            alert("Failed insert image")
        }
        location.reload()
    }
</script>
<div class="flex flex-col w-72">
    <dialog bind:this={dialog} id="mydialog">
        <div class="flex flex-col text-black bg-[#E3A052] justify-center items-center">
            <img src="{AppLogo}" alt="" width="50%" class=" absolute top-[-115px] border-[#E3A052]">
            <div class="flex flex-col w-64">
                <input bind:value={newItem.ItemID} class="p-3 my-1 mx-1 bg-white rounded-xl text-left" type="number" placeholder="ItemID">
                <input bind:value={newItem.Name} class="p-3 my-1 mx-1 bg-white rounded-xl text-left" type="text" placeholder="Name">
                <input bind:value={newItem.Price} class="p-3 my-1 mx-1 bg-white rounded-xl text-left" type="text" placeholder="Price">
                <input bind:value={newItem.Category} class="p-3 my-1 mx-1 bg-white rounded-xl text-left" type="text" placeholder="Category">
                <input bind:files class="p-3 my-1 mx-1 bg-white rounded-xl text-left" type="file" accept="image/png, image/jpeg">
                <button on:click={async () => click()} class="p-2 px-10 m-1 mx-10 bg-white rounded-xl hover:bg-gray-300 active:bg-gray-500">
                    Create
                </button>
            </div>
        </div>
    </dialog>
</div>

<style>
    dialog {
        position: absolute;
        top: 33.3333%;
        padding: 1.25rem;
        background-color: #E3A052;
        border-radius: 1.25rem;
        align-items: center;
    }
</style>