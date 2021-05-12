from firebase import firebase

firebase = firebase.FirebaseApplication(
    "https://aktiven-de72d-default-rtdb.firebaseio.com/", None)

cadastro = {
    'Name': 'Jacquelin',
    'Email': 'jacq30022@hotmail.com',
    'Phone': 794492
}

login = [
    {
        "username": "felipe",
        "password": "x"
    }
]

#result = firebase.post('/aktiven-de72d-default-rtdb/Cadastro:', cadastro)

#result = firebase.post('/aktiven-de72d-default-rtdb/Login:', data)

#result = firebase.post('/aktiven-de72d-default-rtdb/Login:', login)
result = firebase.get('/aktiven-de72d-default-rtdb/Login/0',None)
print(result)
