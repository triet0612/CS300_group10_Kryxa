import { redirect } from "@sveltejs/kit"

export class Pc {
  constructor(PcID, EndTime, Password, IPv4, TimeUsage) {
    this.PcID = PcID
    this.EndTime = EndTime
    this.Password = Password
    this.IPv4 = IPv4
    this.TimeUsage = TimeUsage
  }

  async createPc() {
    let url = "http://localhost:8000/api/admin/pc"
    let statcode = await fetch(url, {
      method: "POST",
      body: JSON.stringify({
        "PcID": this.PcID,
        "EndTime": new Date().toISOString(),
        "Password": "123",
        "IPv4": this.IPv4,
        "TimeUsage": 0,
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

export async function getPcByID(pc_id){
  let url = `http://localhost:8000/api/admin/pc/${pc_id}`
  let pc_info = await fetch(url,{
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + localStorage.getItem("jwt")
    },
  })
  .then(res=>{
    if (res.status==401){
      location.replace('/admin/login')
      return
    }
    return res.json()
  })
  .catch(err => {
    console.log(err)
    return 500
  })
  console.log(pc_info)
  return pc_info
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
  .then(res=>{
    if (res.status==401){
      location.replace('/admin/login')
      return
    }
    return res.json()
  })
  .catch(err => {
    console.log(err); return [];
  })
  return pc_list
}

export async function updateThisPcByID(pc_info,pc_id){
  let url = `http://localhost:8000/api/admin/pc/${pc_id}`
  let statcode = await fetch(url,{
    method: "PUT",
    body: JSON.stringify({
      "PcID": pc_info.PcID,
      "Password": pc_info.Password,
      "IPv4": pc_info.IPv4,
    }),
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + localStorage.getItem("jwt")
    },
  })
  .then(res=>{
    if (res.status === 401) {
      alert("Not logged in")
      location.replace("/admin/login")
    }
    return res.status
  })
  .catch(err => {
    console.log(err)
    return 500
  })
  return statcode
}


