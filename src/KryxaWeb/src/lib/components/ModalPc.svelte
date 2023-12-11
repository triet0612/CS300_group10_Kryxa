<script>
  import { Pc } from "$lib/Pc.js";
  import { AppLogo } from "$lib/Assets.js";

  export let status = "close";

  let newPC = new Pc();
  let dialog;

  $: if (status === "open" && dialog) {
    dialog.show();
  } else if (status === "close" && dialog) {
    dialog.close();
  }

  async function click() {
    let statcode = await newPC.createPc().then((res) => res);
    status = "close";
    if (statcode !== 200) {
      alert("Failed create new Pc");
    }
    location.reload();
  }
</script>

<div class="flex flex-col w-72">
  <dialog bind:this={dialog} id="mydialog">
    <div
      class="flex flex-col text-black bg-[#9324C7] justify-center items-center"
    >
      <img
        src={AppLogo}
        alt=""
        width="50%"
        class=" absolute top-[-115px] border-[#9324C7]"
      />
      <div class="flex flex-col w-64">
        <input
          bind:value={newPC.PcID}
          class="p-3 my-1 mx-1 bg-white rounded-xl text-left"
          type="number"
          placeholder="PcID"
        />
        <input
          bind:value={newPC.IPv4}
          class="p-3 my-1 mx-1 bg-white rounded-xl text-left"
          type="text"
          placeholder="IPv4"
        />
        <button
          on:click={async () => click()}
          class="p-2 px-10 m-1 mx-10 bg-white rounded-xl hover:bg-gray-300 active:bg-gray-500"
        >
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
    background-color: #9324c7;
    border-radius: 1.25rem;
    align-items: center;
  }
</style>
