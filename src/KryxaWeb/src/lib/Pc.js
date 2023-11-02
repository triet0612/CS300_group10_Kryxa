export class Pc {
  constructor(PcID, Password, MAC, IPv4, TimeUsage) {
    this.PcID = PcID
    this.Password = Password
    this.MAC = MAC
    this.IPv4 = IPv4
    this.TimeUsage = TimeUsage
  }

  async createPc() {
    let url = "http://localhost:8000/api/admin/pc"
    let statcode = await fetch(url, {
      method: "POST",
      body: JSON.stringify({
        "PcID": this.PcID,
        "Password": "",
        "MAC": this.MAC,
        "IPv4": this.IPv4,
        "TimeUsage": 0
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