export class Item {
    constructor(ItemID, Name,Price,Category,ItemStatus,Stock) {
      this.ItemID = ItemID
      this.Name = Name
      this.Price = Price
      this.Category = Category
      this.ItemStatus = ItemStatus
      this.Stock = Stock
    }

    async getItemByID(input_id) {
        let url = `http://localhost:8000/api/admin/items/${input_id}`
        let item = await fetch(url, {
            method: "GET",
            headers: {
                "Authorization": "Bearer " + localStorage.getItem("jwt")
            },
        })
        .then(res=>res.json())
        .catch(err => {
            console.log(err)
            return 500
          })
          console.log(item)
          return item
    }

    async createItem() {
        let url = "http://localhost:8000/api/admin/items"
        let statcode = await fetch(url, {
            method: "POST",
            body: JSON.stringify({
            "ItemID": this.ItemID,
            "Name": this.Name,
            "Price": this.Price,
            "Category": this.Category,
            "ItemStatus": "On sale",
            "Stock": this.Stock,
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
}

export async function fetch_all(){
    let url = 'http://localhost:8000/api/admin/items'
    let items = await fetch(url, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + localStorage.getItem("jwt")
    }
    })
    .then(res => res.json())
    .then(res => res)
    .catch(err => {console.log(err); return [];})
    console.log(items[0])
    return items
}

export async function fetch_category(category,name){
    let url = 'http://localhost:8000/api/admin/items'

    if(name!==""){
        url+='?item_name='+name
        if(category!="All"){
            url+= '&item_category='+category
        }
    }
    else{
        if(category!="All"){
            url+= '?item_category='+category
        }
    }
    console.log(url)
    let items = await fetch(url, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + localStorage.getItem("jwt")
    }
    })
    .then(res => res.json())
    .then(res => res)
    .catch(err => {console.log(err); return [];})
    console.log(items[0])
    return items
}

export async function createImage(filename) {
    let url = "http://localhost:8000/api/admin/uploadfile/"
    let statcode = await fetch(url, {
        method: "POST",
        body: JSON.stringify({
        "filename": filename
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

export async function loadImage(imgname) {
    let url = "http://localhost:8000/api/admin/getfile/"
    if(imgname !==undefined){
        url+=imgname
    }
    let str = await fetch(url, {
        method: "GET",
        body: JSON.stringify({
        "filename": filename
        }),
        headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + localStorage.getItem("jwt")
        },
    })
    .then(res => res.json())
    .then(res => res)
    .catch(err => {console.log(err); return [];})
    console.log(str)
    return str
}

