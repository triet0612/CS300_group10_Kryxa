<script>
    import AdminNav from "$lib/components/AdminNav.svelte"
    import SaleStats from "$lib/components/SaleStats.svelte";
    import PCSales from "$lib/components/PCSales.svelte";
    import TimeUsageStats from "$lib/components/TimeUsageStats.svelte";

    let chart_type;
</script>

<div class="flex flex-row h-screen bg-main-bg bg-cover font-BlackOpsOne text-xl text-purple-300">
    <div class="flex flex-col">
        <AdminNav/>
    </div>
    <div class="h-full w-full">
        <div class="m-5">
            <select class="bg-purple-950 px-5 py-2  border-solid border-2 border-purple-400" name="cars" id="cars" bind:value={chart_type}>
                <option value="sales">Sales by month</option>
                <option value="sales_pc">Sales per pc</option>
                <option value="timeusage">Time usage per PC</option>
            </select>
        </div>
        <div class="h-5/6 m-5">
            {#if chart_type === "sales"}
                <SaleStats/>
            {:else if chart_type === "sales_pc"}
                <PCSales/>
            {:else if chart_type === "timeusage"}
                <TimeUsageStats/>
            {/if}
        </div>
    </div>
</div>