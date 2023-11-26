<script>
  import {UserAssets} from "$lib/Assets.js";
  import { writable } from "svelte/store";
  import { get } from "svelte/store";
  import {onMount } from "svelte";
  import { tweened } from 'svelte/motion';

const items = [
    "All",
    "Food",
    "Drink",
    "Time"
  ];

  let original = 120 * 60; // 5 min
	let timer = tweened(original)

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
          <span class="hours">{formattedHours} :</span>
          <span class="mins">{formattedMinutes} :</span>
          <span class="secs">{formattedSeconds}</span>
        </div>
      </li>
      {#each items as it}
        <div class="flex my-2">
          <li class="flex p-2 hover:bg-purple-300 hover:text-black">
            <button class="text-2xl">{it}</button>
          </li>
        </div>
      {/each}
    </ul>
  </div>
</aside>
