export class Pc {
  constructor(PcID, Password, MAC, IPv4, TimeUsage, Status) {
    this.PcID = PcID
    this.Password = Password
    this.MAC = MAC
    this.IPv4 = IPv4
    this.TimeUsage = TimeUsage
    this.Status = Status
  }

  async createPc() {
    let url = "http://localhost:8000/api/admin/pc"
    let statcode = await fetch(url, {
      method: "POST",
      body: JSON.stringify({
        "PcID": this.PcID,
        "Password": "123",
        "MAC": this.MAC,
        "IPv4": this.IPv4,
        "TimeUsage": 0,
        "Status": "Available"
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

  async getPcByID(pc_id){
    let url = `http://localhost:8000/api/admin/pc/${pc_id}`
    let pc_info = await fetch(url,{
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + localStorage.getItem("jwt")
      },
    })
    .then(res=>res.json())
    .catch(err => {
      console.log(err)
      return 500
    })
    console.log(pc_info)
    return pc_info
  }
}

export async function get_Pcs(){ //Fetch all Pcs with their ID and Status
  let url = "http://localhost:8000/api/admin/pc"
  let pc_list= await fetch(url,({
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + localStorage.getItem("jwt")
    },
  }))
  .then(res => res.json())
  .catch(err => {
    console.log(err); return [];
  })
  console.log(pc_list[0])
  return pc_list
}

// export async function updatePcByID(pc_id){
//   let url = `http://localhost:8000/api/admin/pc/${pc_id}`
//   let pc_info = await fetch(url,{
//     method: "POST",
//     body: JSON.stringify({
//       "PcID": this.PcID,
//       "MAC": this.MAC,
//       "IPv4": this.IPv4,
//     }),
//     headers: {
//       "Content-Type": "application/json",
//       "Authorization": "Bearer " + localStorage.getItem("jwt")
//     },
//   })
//   .then(res=>res.json())
//   .catch(err => {
//     console.log(err)
//     return 500
//   })
//   console.log(pc_info)
//   return pc_info
// }
