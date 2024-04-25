interface CreateProps {
  body: any;
  token?: any;
}
interface TokenProps {
  body: any;
  token: any;
}
interface RegisterProps {
  params: string;
  body: any;
}
interface IndexProps {
  params: string;
  skip?: number;
  take?: number;
}
class Api {
  async createUser(props: CreateProps) {
    return await fetch(`http://localhost:8000/api/auth/users/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: `${JSON.stringify(props.body)}`,
    })
      .then((response) => response.json())
      .then((data) => data)
      .catch((error) => error.message);
  }

  async createProfile(props: CreateProps) {
    return await fetch(`http://localhost:8000/api/profiles/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${props.token}`
      },
      body: `${JSON.stringify(props.body)}`,
    })
      .then((response) => response.json())
      .then((data) => data)
      .catch((error) => error);
  }

  async getToken(props: CreateProps) {
    return await fetch(`http://localhost:8000/api/token/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: `${JSON.stringify(props.body)}`,
    })
      .then((response) => response.json())
      .then((data) => data)
      .catch((error) => error.message);
  }

  async register(props: RegisterProps) {
    return await fetch(`http://localhost:8000/` + props.params, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        authorization: `Bearer ${localStorage.getItem("token")}`,
      },
      body: `${JSON.stringify(props.body)}`,
    })
      .then((response) => response.json())
      .then((data) => data)
      .catch((error) => error);
  }

  async update() {}

  async show() {}

  async index(props: IndexProps,  userId?: boolean) {
    return await fetch(`http://localhost:8000/` + `${props.params}${userId ? '/feed/' + localStorage.getItem('userId') : ''}?skip=${props.skip || 0}&take=${props.take ||  4}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then((response) => response.json())
      .then((data) => data)
      .catch((error) => error);
  }

  async delete() {}
  
  async getAnimalsByInstitution() {
    return await fetch(`http://localhost:8000/animal/user/${localStorage.getItem('userId')}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then((response) => response.json())
      .then((data) => data)
      .catch((error) => error);
  }

  async adotarAnimal(animalId: string) {
    return await fetch(`http://localhost:8000/animal/adotar/${animalId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then((response) => response.json())
      .then((data) => data)
      .catch((error) => error);
  }

  async listInteresseByAnimal(animalId: string) {
    return await fetch(`http://localhost:8000/user/interesse/list/${animalId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then((response) => response.json())
      .then((data) => data)
      .catch((error) => error);
  }

  async addInteresse(animalId: string) {
    return await fetch(`http://localhost:8000/api/users/interesse/${localStorage.getItem('userId')}/${animalId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then((response) => response.json())
      .then((data) => data)
      .catch((error) => error);
  }
}

export const api = new Api();
