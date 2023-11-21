<script>
    import Plotly from 'plotly.js-dist-min'

    let d = (new Date().getFullYear()).toString() + "-" + (new Date().getMonth() + 1).toString();
    const max_month = d;

    $: year = d.split("-")[0]
    $: month = d.split("-")[1]

    let plot;
    const layout = {
        title: `Daily Sales`,
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
                text: "Day",
                standoff: 50,
            },
            color: 'white'
        },
        yaxis: {
            title: {
                text: "Sales",
                standoff: 50,
            },
            color: 'white'
        }
    };

    async function fetchStats() {
        let sales = await fetch(`http://localhost:8000/api/admin/sales?month=${month}&year=${year}`, {
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
            x: sales["month"],
            y: sales["sales"],
            type: "scatter",
            mode: "lines+markers",
            marker: {
                color: 'yellow',
                size: 10,
            },
            line: {color: 'blue'}
        }];
        Plotly.newPlot(plot, data, layout); 
    }

    $: if (d !== "") {
        fetchStats()
    }
</script>

<div class="h-full font-BlackOpsOne text-xl text-purple-300">
    <div class="h-[5%] flex flex-row my-2">
        <p class="px-5">Pick Month:</p>
        <input bind:value={d} class="bg-purple-900 px-5 border-2 border-black" type="month" max="{max_month}">
    </div>
    <div class="h-[95%] w-full my-2" bind:this={plot}></div>
</div>
