<script>
    import Plotly from 'plotly.js-dist-min'
    import { onMount } from 'svelte';

    let plot;
    const layout = {
        title: `Sales per PC`,
        font: {
            size: 18,
            color: 'white',
            family: 'Consolas',
        },
        margin: {
            l: 130,
            r: 100,
            t: 100,
            b: 100,
            pad: 20
        },
        paper_bgcolor: '#212121',
        plot_bgcolor: '#424242',
        xaxis: {
            type: 'category',
            title: {text: "PcID",standoff: 50},
            color: 'white'
        },
        yaxis: {
            title: {text: "Sales",standoff: 50},
            color: 'white'
        }
    };
    async function fetchStats() {
        let sales = await fetch(`http://localhost:8000/api/admin/sales`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem("jwt")
            }
        }).then(res => {
            if (res.status === 401) {
                alert("Not logged in")
                location.replace("/admin/login")
            }
            return res.json()
        }).catch(err => {console.log(err); return {}})
        let data = [{
            x: sales["pc_list"],
            y: sales["sales"],
            type: "bar",
        }];
        Plotly.newPlot(plot, data, layout); 
    }
    onMount(() => {
        fetchStats()
    })
</script>

<div class="h-full w-full my-2" bind:this={plot}></div>
