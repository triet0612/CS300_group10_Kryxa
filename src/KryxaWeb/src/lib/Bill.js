

export class Bill{
    constructor(BillID, PcID, Datetime, Note, Total, Cart){
        this.BillID=BillID
        this.PcID=PcID
        this.Datetime=Datetime
        this.Note=Note
        this.Total=Total
        this.Cart=Cart
    }
}

export async function fetch_all(bill_id,day,month,year){
    let url = 'http://localhost:8000/api/admin/bills/'
    if (bill_id !=undefined){
        url+='?bill_id=' + bill_id;
        if (day != undefined && month !=undefined && year !=undefined){
            url+='&day='+day+'&month='+month+'&year='+year
        }
    }
    else{
        if (day != undefined && month !=undefined && year !=undefined){
            url+='?day='+day+'&month='+month+'&year='+year
        }
    }
    
    let items = await fetch(url, {
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
    return items
}

// export async function getBillbyID(bill_id){
//     let url=`http://localhost:8000/api/admin/bills/${bill_id}`
//     let bill_info = await fetch(url,{
//         method: "GET",
//         header: {
//             "Content-Type": "application/json",
//             "Authorization": "Bearer " + localStorage.getItem("jwt")
//           },
//     })
//     .then(res=>{
//         if(res.status==401){
//             location.replace('admin/login')
//             return
//         }
//         return res.json()
//     })
//     .catch(err=>{
//         console.log(err)
//         return 500
//     })
//     console.log(bill_info)
//     return bill_info
// }

export async function update_bill(new_data){
    let url = `http://localhost:8000/api/admin/bills/${new_data.BillID}`
    console.log(new_data.Cart);
    let statcode = await fetch(url, {
        method: "PUT",
        body: JSON.stringify({
        "BillID": new_data.BillID,
        "PcID" : new_data.PcID,
        "Datetime": new_data.Datetime,
        "Note": new_data.Note,
        "Total": new_data.Total,
        "Cart": new_data.Cart,
        }),
        headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + localStorage.getItem("jwt")
        },
    })
    .then(res => res.status)
    .catch(err => {
        console.log(err)
        return 500
    })
    return statcode
}