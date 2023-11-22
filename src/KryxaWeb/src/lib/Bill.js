export class Bill {
    constructor(BillID, PcID,Datetime,Note,Total,Cart) {
      this.BillID = BillID,
      this.PcID = PcID,
      this.Datetime = Datetime,
      this.Note = Note,
      this.Total = Total,
      this.Cart = Cart
    }
    async getBills(input_id) {
        let url = `http://localhost:8000/api/admin/bills`
        let item = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem("jwt")
            },
        })
        .then(res => {
            if (res.status === 401){
                location.replace('/admin/login')
                return []
            }
            return res.json()
        })
        .catch(err => {
            console.log(err)
            return []
          })
          console.log(item)
          return item
    }

    async createBill() {
        let url = "http://localhost:8000/api/admin/item"
        
        let statcode = await fetch(url, {
            method: "POST",
            body: JSON.stringify({
            "BillID": this.BillID,
            "PcID": this.PcID,
            "Datetime": this.Datetime,
            "Note": this.Note,
            "Total": this.Total,
            "Cart" : this.Cart,
            }),
            headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem("jwt")
            },
        })
        .then(res => {
            if (res.status === 401){
                location.replace('/admin/login')
                return res.status
            }
            return res.status
        })
        .catch(err => {
            console.log(err)
            return 500
        })
        return statcode
    }
}

export async function fetch_all(){
    let url = 'http://localhost:8000/api/admin/bills'
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
    console.log(items[0])
    return items
}

// export async function fetch_category(category,name){
//     let url = 'http://localhost:8000/api/admin/items'

//     if(name!==""){
//         url+='?item_name='+name
//         if(category!="All"){
//             url+= '&item_category='+category
//         }
//     }
//     else{
//         if(category!="All"){
//             url+= '?item_category='+category
//         }
//     }
//     console.log(url)
//     let items = await fetch(url, {
//     method: "GET",
//     headers: {
//         "Content-Type": "application/json",
//         "Authorization": "Bearer " + localStorage.getItem("jwt")
//     }
//     })
//     .then(res => {
//         if (res.status === 401){
//             location.replace('/admin/login')
//             return []
//         }
//         return res.json()
//     })
//     .catch(err => {console.log(err); return [];})
//     console.log(items[0])
//     return items
// }

// export async function createImage(file,id) {
    
//     let url = `http://localhost:8000/api/admin/uploadfile/?item_id=${id}`
//     let data = new FormData()

//     data.append(
//         'file',file[0]
//     )
//     console.log(data)
    
//     let statcode = await fetch(url, {
//         method: "POST",
//         body: data,
//         headers: {
//         // "Content-Type": "multipart/form-data",
//         "Accept": "application/json",
//         "Authorization": "Bearer " + localStorage.getItem("jwt"),
//         },
//     })
//     .then(res => {
//         if (res.status === 401){
//             location.replace('/admin/login')
//             return res.status
//         }
//         return res.status
//     })
//     .catch(err => {
//         console.log(err)
//         return 500
//     })
//     return statcode
// }


