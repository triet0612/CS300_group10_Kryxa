

export class Bill{
    constructor(BillID, PcID, Datetime, Note, Total, Cart){
        this.BillID=BillID
        this.PcId=PcID
        this.Datetime=Datetime
        this.Note=Note
        this.Total=Total
        this.Cart=Cart
    }

    async getBillbyID(bill_id){
        let url=`http://localhost:8000/api/admin/bills/${bill_id}`
        let bill_info = await fetch(url,{
            method: "GET",
            header: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem("jwt")
              },
        })
        .then(res=>{
            if(res.status==401){
                location.replace('admin/login')
                return
            }
            return res.json()
        })
        .catch(err=>{
            console.log(err)
            return 500
        })
        console.log(bill_info)
        return bill_info
    }
}