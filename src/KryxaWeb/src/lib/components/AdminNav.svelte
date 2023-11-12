<script>
  import { AppLogo } from "$lib/Assets.js";
  const items = [
    ["Home", ""],
    ["Items", "items"],
    ["Tournament", "tournament"],
    ["Statistics", "stats"],
    ["Account", "account"]
  ];

  function logout() {
    localStorage.removeItem("jwt");
    location.replace("/admin");
  }
</script>

<aside class="flex flex-col m-4 w-60 h-screen justify-center">
  <div
    class="p-3 rounded-lg bg-white/5 border-2 border-gray-500 backdrop-blur-md backdrop-brightness-125"
  >
    <ul class="text-2xl text-purple-300 font-BlackOpsOne">
      <li><img src={AppLogo} alt="Logo" /></li>
      {#each items as it}
        <div class="flex my-2">
          <li class="flex p-2 hover:bg-purple-300 hover:text-black">
            <a href="/admin/{it[1]}">{it[0]}</a>
          </li>
        </div>
      {/each}
      <div
        class="flex my-3 border-2 border-gray-500 text-purple-600 hover:bg-black hover:text-purple-300 justify-center"
      >
        <button class="p-3" on:click={() => logout()}>Logout</button>
      </div>
    </ul>
  </div>
</aside>
