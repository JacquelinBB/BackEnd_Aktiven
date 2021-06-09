import requests
import json

#Vai vir do React Native e colocar no banco de dados
cadastro = {
        "nome":"Juliana",
        "nome_robo":"Amora",
        "usuario":"Juliana76",
        "senha":"45274vV",
        "resenha":"45274vV"
     }

r = requests.post('http://127.0.0.1:5000/cadastro', data=json.dumps(cadastro))
print(r.json())

b_g = requests.get('http://127.0.0.1:5000/buscador')
print(b_g.json())

#Vai vir do banco de dados
dados = {
        "usuario":"Juliana76"
}
b_p = requests.post('http://127.0.0.1:5000/buscador', data=json.dumps(dados))
print(b_p.json())

#Vai vir do banco de dados
login = {
        "usuario":"Juliana76",
        "senha":"45274vV"
}
l = requests.post('http://127.0.0.1:5000/login', data=json.dumps(login))
print(l.json())

login_dh = {
        "usuario":"Juliana76"
}
dh_b = requests.post('http://127.0.0.1:5000/dashboard_buscador', data=json.dumps(login_dh))
print(dh_b.json())
#mandar para o react
dh = requests.post('http://127.0.0.1:5000/dashboard', data=json.dumps(dh_b.json()))
print(dh.json())