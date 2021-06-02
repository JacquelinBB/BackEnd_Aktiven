from flask import Flask, request, jsonify
import json
import sqlite3
app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("database.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

cadastro_list = list()

@app.route('/cadastro',methods=['POST'])
def cadastro():
    conn = db_connection()
    cursor = conn.cursor()
    req_data = request.data
    dict_data = json.loads(req_data)
    print(dict_data)
    cadastro_dict = {
        "nome":dict_data["nome"],
        "nome_robo":dict_data["nome_robo"],
        "usuario":dict_data["usuario"],
        "senha":dict_data["senha"],
        "resenha":dict_data["resenha"]
    }  
    if cadastro_dict["senha"] == cadastro_dict["resenha"]:
        #vai acontecer aqui o cadastro do usuário
        nome = cadastro_dict["nome"]
        nome_robo = cadastro_dict["nome_robo"]
        usuario = cadastro_dict["usuario"]
        senha  = cadastro_dict["senha"]
        resenha = cadastro_dict["resenha"]
        #cadastro_list.append(cadastro_dict)
        cursor.execute("SELECT * FROM pessoas")
        usuario_lista = list()
        for linha in cursor.fetchall():
            usuario_lista.append(linha[3])
        if usuario in usuario_lista:
            return jsonify(msg = "Usuário já existe!")
        else:
            cursor.execute(f"INSERT INTO pessoas (nome, nome_robo, usuario, senha, resenha) VALUES ('{nome}', '{nome_robo}','{usuario}','{senha}','{resenha}');")
            conn.commit()
            conn.close()
            return jsonify(msg = "Cadastro feito com sucesso!")
    else:
        conn.close()
        return jsonify(msg = "Senhas diferentes!")

@app.route('/buscador', methods=['GET','POST'])
def buscador(manual=False, user=None, senha=None):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas")
    usuario_lista = list()
    senha_lista = list()
    for linha in cursor.fetchall():
        usuario_lista.append(linha[3])
        senha_lista.append(linha[4])
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
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas")
    usuario_lista = list()
    senha_lista = list()
    for linha in cursor.fetchall():
        usuario_lista.append(linha[3])
        senha_lista.append(linha[4])
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

@app.route('/dashboard', methods=['POST'])
def dashboard():
    conn = db_connection()
    cursor = conn.cursor()
    req_data = request.data
    dict_data = json.loads(req_data)
    id = dict_data["id"]
    cursor.execute(f"SELECT nome, nome_robo from pessoas where id ='{id}'")
    perfil = dict()
    for linha in cursor.fetchall():
        perfil['nome'] = linha[0]
        perfil['nome_robo'] = linha[1]
    return jsonify(perfil)

@app.route('/dashboard_buscador', methods=['POST'])
def dashboard_buscador():
    conn = db_connection()
    cursor = conn.cursor()
    req_data = request.data
    dict_data = json.loads(req_data)
    id_login = dict_data["usuario"]
    cursor.execute(f"SELECT id from pessoas where usuario ='{id_login}'")
    perfil_dh = dict()
    for linha in cursor.fetchall():
        perfil_dh['id'] = linha[0]
    return jsonify(perfil_dh)
