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

  let n = true;
  // let audio;

  function get_notif() {
    n = !n
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

  async function get_food_queue() {
    let url = 'http://localhost:8000/api/admin/food_queue'
    let foods = await fetch(url, {
      method: "GET",
      headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + localStorage.getItem("jwt")
      }
    })
    .then(res => {
        if (res.status === 401){
            location.replace('/admin/login')
            return []
        }
        return res.json()
    })
    .catch(err => {console.log(err); return [];})
    return foods
  }

  async function delete_food(food) {
    let url = 'http://localhost:8000/api/admin/delete_food_queue'
    await fetch(url, {
      method: "POST",
      body: JSON.stringify(food),
      headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + localStorage.getItem("jwt")
      }
    })
    .then(res => {
      if (res.status === 401){
        location.replace('/admin/login')
        return []
      }
      return res
    })
    .catch(err => {console.log(err); return [];})
    location.reload()
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


<aside class="flex flex-col w-72 h-screen justify-center">
  <div class="p-3 w-full h-full">
    <div
      class="p-3 h-full flex flex-col rounded-lg bg-white/5 border-2 border-gray-500 backdrop-blur-md backdrop-brightness-125 font-BlackOpsOne"
    >
      <div class="text-2xl text-purple-300">
        <ul>
          <li><img src={AppLogo} alt="Logo" /></li>
          {#each items as it}
            <div class="flex my-2">
              <li class="grid grid-cols-2 gap-4 p-2 hover:bg-purple-300 hover:text-black">
                <div>
                  <a rel="external" href="/admin/{it[1]}">{it[0]}</a>
                </div>
                {#if it[1] === "bills" && $notifs === "True"}
                <div class=" text-center rounded-lg bg-green-900">
                    &#128276;
                  </div>
                {/if}
              </li>
            </div>
          {/each}
          <br>
        </ul>
      </div>
      <div class="text-xl h-1/4 text-yellow-400 font-BlackOpsOne no-scrollbar overflow-auto">
        {#key n}
          {#await get_food_queue(n)}
            <p>None</p>
          {:then res}
            {#each res as v}
              <div class="flex flex-row h-[90px] p-1 justify-between">
                <div class="flex flex-col">
                  <p>PcID: {v["PcID"]}</p>
                  <p>Item: {v["ItemID"]}</p>
                  <p>Qt: {v["Qt"]}</p>
                </div>
                <div class="flex border-2 border-gray-500 text-2xl p-4 text-blue-400 hover:bg-sky-600 hover:text-white justify-center">
                  <button on:click={() => delete_food(v)}>Done</button>
                </div>
              </div>
              <br>
            {/each}
          {/await}
        {/key}
      </div>
      <div class="py-3">
        <div class="text-2xl border-2 border-gray-500 text-purple-600 hover:bg-black hover:text-purple-300 justify-center text-center">
          <button class="p-3" on:click={() => logout()}>Logout</button>
        </div>
      </div>
    </div>
  </div>
</aside>
