export class Account {
  constructor(ID, Password) {
    this.ID = ID
    this.Password = Password
  }

  async login(role) {
    let url = 'http://localhost:8000/api/login'
    if (role === "Admin") {
      url = 'http://localhost:8000/api/admin/login'
    }
    let creds = await fetch(url, {
      method: "POST",
      body: JSON.stringify({
        ID: Number(this.ID),
        Password: this.Password
      }),
      headers: {
        "Content-Type": "application/json"
      }
    })
    .then(res => {
      if (res.status === 200) {
        return res.headers.get("Authorization")
      } else {
        return ""
      }
    })
    .catch(err => {console.log(err); return "";})
    if (creds === "") {
      return
    }
    localStorage.setItem("jwt", creds)
    location.replace("./")
  }
}