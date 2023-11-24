export class Bill {
    constructor(BillID, PcID,Datetime,Note,Total,Cart) {
      this.BillID = BillID,
      this.PcID = PcID,
      this.Datetime = Datetime,
      this.Note = Note,
      this.Total = Total,
      this.Cart = Cart
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
    return items
}

export async function fetch_by_id(bill_id){
    let url = `http://localhost:8000/api/admin/bills/${bill_id}`
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




