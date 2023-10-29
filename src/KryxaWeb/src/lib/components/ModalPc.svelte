<script>
    import {Pc} from "$lib/Pc.js"

    export let status = "close";    

    let newPC = new Pc();
    let dialog;

    $: if (status === "open" && dialog) {
        dialog.show()
    } else if (status === "close" && dialog) {
        dialog.close()
    }

    async function click() {
        let statcode = await newPC.createPc().then(res => res)
        if (statcode !== 200) {
            alert("Failed create new Pc")
        }
        status = "close"
    }
</script>

<dialog bind:this={dialog} id="mydialog">
    <div class="grid text-white">
        <div class="grid grid-cols-2">
            <input bind:value={newPC.PcID} class="p-2 my-1 mx-1 bg-teal-950 rounded text-center" type="number" placeholder="PcID">
            <input bind:value={newPC.Password} class="p-2 my-1 mx-1 bg-teal-950 rounded text-center" type="text" placeholder="Password">
            <input bind:value={newPC.MAC} class="p-2 my-1 mx-1 bg-teal-950 rounded text-center" type="text" placeholder="MAC">
            <input bind:value={newPC.IPv4} class="p-2 my-1 mx-1 bg-teal-950 rounded text-center" type="text" placeholder="IPv4">
        </div>
        <button on:click={async () => click()} class="p-2 px-10 m-1 bg-rose-600 rounded hover:bg-rose-700 active:bg-rose-900">
            Create
        </button>
    </div>
</dialog>

<style>
    dialog {
        position: absolute;
        top: 33.3333%;
        padding: 1.25rem;
        background-color: rgb(56, 6, 6);
        border-radius: 0.25rem;
    }
</style>