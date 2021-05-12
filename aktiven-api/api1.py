from flask import Flask, request, jsonify
import json
app = Flask(__name__)

cadastro_list = list()

@app.route('/')
def hello_world():
    return 'Bem vindo ao Aktiven!'

@app.route('/cadastro',methods=['POST'])
def cadastro():
    req_data = request.data
    dict_data = json.loads(req_data)
    print(dict_data)
    cadastro_dict = {
        "usuario":dict_data["usuario"],
        "senha":dict_data["senha"],
        "resenha":dict_data["resenha"]
    }
    if cadastro_dict["senha"] == cadastro_dict["resenha"]:
        #vai acontecer aqui o cadastro do usuário
        cadastro_list.append(cadastro_dict)
        return jsonify(msg = "Cadastro feito com sucesso!")
    else:
        return jsonify(msg = "Senhas diferentes!")

@app.route('/buscador', methods=['GET','POST'])
def buscador(manual=False, user=None, senha=None):
    usuario_lista = list()
    senha_lista = list()
    for cadastro in cadastro_list:
        usuario_lista.append(cadastro["usuario"])
        senha_lista.append(cadastro["senha"])
    if request.method == 'GET':
        return jsonify(msg = usuario_lista)
    if request.method == 'POST':
        req_data = request.data
        dict_data = json.loads(req_data)
        if dict_data["usuario"] in usuario_lista:
            string = dict_data["usuario"] + " existe."
            return jsonify(msg = string)  
        else:
            string = dict_data["usuario"] + " não existe."
            return jsonify(msg = string)

    else:
        return jsonify(msg = "Mensagem de erro.")

def buscador_man(user, senha):
    usuario_lista = list()
    senha_lista = list()
    for cadastro in cadastro_list:
        usuario_lista.append(cadastro["usuario"])
        senha_lista.append(cadastro["senha"])
    if user in usuario_lista:
        if senha in senha_lista:
            return True
    else:
        return False

@app.route('/login',methods=['POST'])
def login():
    req_data = request.data
    dict_data = json.loads(req_data)
    login_dict = {
        "usuario":dict_data["usuario"],
        "senha":dict_data["senha"]
    }
    if buscador_man(login_dict["usuario"], login_dict["senha"]) == True:
        return jsonify(msg = "Usuário logado com sucesso!")
    else:
        return jsonify(msg = "Usuário e senha não coincidem!")
    return jsonify(login_dict)
