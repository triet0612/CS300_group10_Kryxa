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
}