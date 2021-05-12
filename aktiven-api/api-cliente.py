import requests
import json

cadastro = {
        "usuario":"Juliana76",
        "senha":"45274vV",
        "resenha":"45274vV"
     }

r = requests.post('http://127.0.0.1:5000/cadastro', data=json.dumps(cadastro))
#print(r.json())

b_g = requests.get('http://127.0.0.1:5000/buscador')
print(b_g.json())

dados = {
        "usuario":"Juliana76"
}
b_p = requests.post('http://127.0.0.1:5000/buscador', data=json.dumps(dados))
print(b_p.json())

login = {
        "usuario":"Juliana",
        "senha":"45274vV"
}
l = requests.post('http://127.0.0.1:5000/login', data=json.dumps(login))
print(l.json())
