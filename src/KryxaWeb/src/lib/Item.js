export class Item {
    constructor(ID, Name,Price,Category,ItemStatus,Stock) {
      this.ID = ID
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

