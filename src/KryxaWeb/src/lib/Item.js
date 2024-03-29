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

export async function update_item(new_data){
            let url = `http://localhost:8000/api/admin/items/${new_data.ItemID}`
            console.log(url)
            let statcode = await fetch(url, {
                method: "PUT",
                body: JSON.stringify({
                "ItemID": new_data.ItemID,
                "Name": new_data.Name,
                "Price": new_data.Price,
                "Category": new_data.Category,
                "Stock": new_data.Stock,
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


export async function delete_item(input_id) {
    let url = `http://localhost:8000/api/admin/items/${input_id}`

    let statcode = await fetch(url, {
        method: "DELETE",
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

export async function createImage(file,id) {
    
    let url = `http://localhost:8000/api/admin/uploadfile/?item_id=${id}`
    let data = new FormData()
    if (file != undefined){
        data.append(
            'file',file[0]
        )
    }
    
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

export async function user_fetch_category(category,name){
    let url = 'http://localhost:8000/api/items'

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
            location.replace('/login')
            return []
        }
        return res.json()
    })
    .catch(err => {console.log(err); return [];})
    return items
}
