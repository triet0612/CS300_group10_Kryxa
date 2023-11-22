<script>
    import Plotly from 'plotly.js-dist-min'

    let plot;
    const layout = {
        title: `Time usage`,
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
            title: {
                text: "PcID",
                standoff: 50,
            },
            color: 'white'
        },
        yaxis: {
            title: {
                text: "Time (minute)",
                standoff: 50,
            },
            color: 'white'
        }
    };

    async function fetchStats() {
        let sales = await fetch(`http://localhost:8000/api/admin/pc/time/`, {
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
            y: sales["time_usage_list"],
            type: "bar",
            mode: "lines+markers",
            marker: {
                color: 'lightgreen',
                size: 10,
            },
            line: {color: '#B24BF3'}
        }];
        Plotly.newPlot(plot, data, layout); 
    }

    $: fetchStats()

</script>

<div class="h-full font-BlackOpsOne text-xl text-purple-300">
    <div class="h-[95%] w-full my-2" bind:this={plot}></div>
</div>
