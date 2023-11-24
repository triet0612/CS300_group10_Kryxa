<script>
  import { AppLogo } from "$lib/Assets.js";
  import { onMount } from "svelte";
  import {notif} from "$lib/Assets.js"
  import {notifs} from "$lib/stores.js"
  const items = [
    ["Home", ""],
    ["Items", "items"],
    ["Bills", "bills"],
    ["Statistics", "stats"],
    ["Account", "account"]
  ];

  // let notifs = "false";
  // let audio;

  function get_notif() {
    console.log($notifs)
    let xhttp = new XMLHttpRequest();
    let res;

    xhttp.open("GET", "http://localhost:8000/api/admin/bill_notif")
    xhttp.setRequestHeader("Content-Type", "application/json")
    xhttp.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("jwt"))

    xhttp.onreadystatechange = function () {
      if (xhttp.readyState == 4 && xhttp.status == 200) {
        res = JSON.parse(xhttp.responseText)
        console.log(res["Message"])
        if (res["Message"] === "True" && $notifs === "False") {
          console.log($notifs)
          notifs.set("True")
          let audio = new Audio(notif);
          audio.play()
        }
        if (res["Message"] === "False"){
          notifs.set("False")
        }
        console.log("asd")
      }
    }
    xhttp.send()
  }

  onMount(() => {
    const interval = setInterval(get_notif, 5000)
    get_notif()
    return () => clearInterval(interval)
  })

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
          <li class="grid grid-cols-2 gap-4 p-2 hover:bg-purple-300 hover:text-black">
            <div>
              <a href="/admin/{it[1]}">{it[0]}</a>
            </div>
            {#if it[1] === "bills" && $notifs === "True"}
            <div class=" text-center rounded-lg bg-green-900">
                &#128276;
              </div>
            {/if}
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
