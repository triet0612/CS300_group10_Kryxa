export class Item {
    constructor(ItemID, Name,Price,Category,Stock) {
      this.ItemID = ItemID
      this.Name = Name
      this.Price = Price
      this.Category = Category
      this.Stock = Stock
    }



    async getItemByID(input_id) {
        let url = `http://localhost:8000/api/admin/items/${input_id}`
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
            return 500
          })
          console.log(item)
          return item
    }

    async createItem() {
        let url = "http://localhost:8000/api/admin/item"
        
        let statcode = await fetch(url, {
            method: "POST",
            body: JSON.stringify({
            "ItemID": this.ItemID,
            "Name": this.Name,
            "Price": this.Price,
            "Category": this.Category,
            "Stock": 0,
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
    let url = 'http://localhost:8000/api/admin/items'
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

export async function createImage(file,id) {
    
    let url = `http://localhost:8000/api/admin/uploadfile/?item_id=${id}`
    let data = new FormData()

    data.append(
        'file',file[0]
    )
    console.log(data)
    
    let statcode = await fetch(url, {
        method: "POST",
        body: data,
        headers: {
        // "Content-Type": "multipart/form-data",
        "Accept": "application/json",
        "Authorization": "Bearer " + localStorage.getItem("jwt"),
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


