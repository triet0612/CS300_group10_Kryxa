<script>
  import {UserAssets} from "$lib/Assets.js";
  import { onMount } from "svelte";
  import { tweened } from 'svelte/motion';

  const items = [
    "All",
    "Food",
    "Drink",
    "Time"
  ];

  let endtime;

  let original = 120 * 60; // 5 min
	let timer;

  onMount(async () => {
    let response = await fetch("http://localhost:8000/api/time", {
      method: "GET",
      headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + localStorage.getItem("jwt")
      }
    }).then(res => res.json()).catch(err => err)
    endtime = new Date(response["EndTime"])
    let time_diff = endtime - new Date()
    if (time_diff > 0) {
      timer = tweened((time_diff / 1000))
    }
  })

  setInterval(() => {
    if ($timer > 0) $timer--;
  }, 1000);

  $: hours = Math.floor($timer / 3600)
  $: minutes = Math.floor(($timer - hours * 3600) / 60);
  $: seconds = Math.floor($timer - hours * 3600 - minutes * 60)

  $: formattedHours = hours.toLocaleString('en-US', {
    minimumIntegerDigits: 2,
    useGrouping: false
  });
  $: formattedMinutes = minutes.toLocaleString('en-US', {
    minimumIntegerDigits: 2,
    useGrouping: false
  });
  $: formattedSeconds = seconds.toLocaleString('en-US', {
    minimumIntegerDigits: 2,
    useGrouping: false
  });

  export let filter_value;

  $: {
    console.log(filter_value)
  }
</script>



<aside class="flex flex-col m-4 w-60 h-screen justify-center">
  <div
    class="p-3 rounded-lg bg-white/5 border-2 border-gray-500 backdrop-blur-md backdrop-brightness-125"
  >
    <ul class="flex flex-col text-2xl text-[#FF9900] font-BlackOpsOne">
      <li><img src={UserAssets["UserLogo"]} alt="Logo" /></li>
      <li>
        <div h-fit w-fit class="justify-self-center my-2
                                text-center text-3xl leading-relaxed
                                ring-4 ring-[#BD7BFF] rounded-lg">
          {#if timer === undefined}
            Ended
          {:else}
            <span class="hours">{formattedHours} :</span>
            <span class="mins">{formattedMinutes} :</span>
            <span class="secs">{formattedSeconds}</span>
          {/if}
        </div>
      </li>
      {#each items as it}
        <div class="flex my-2">
          <li class="flex p-2 hover:bg-purple-300 hover:text-black">
            <button class="text-2xl" on:click={() => {filter_value=it}}>{it}</button>
          </li>
        </div>
      {/each}
    </ul>
  </div>
</aside>
