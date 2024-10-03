from app import app
from flask import render_template
from flask import request
import requests
import json
link = "https://flaskti20n-default-rtdb.firebaseio.com/" #conectar ao banco

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo="Página Principal")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="cadastro")

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf      = request.form.get("cpf")
        nome     = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados    = {"cpf":cpf,"nome":nome,"telefone":telefone, "endereco":endereco}
        requisicao = requests.post(f'{link}/cadastrar/.json', data = json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n\n {e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #solicitação dos dados
        dicionario = requisicao.json()
        return dicionario
    except Exception as e:
        return f'Algo deu errado \n\n{e}'

@app.route('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #solicitar os dados
        dicionario = requisicao.json()
        idCadastro = "" #Armazenar o ID individual de cada um
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == '1234':
                idCadastro = codigo
                return idCadastro
    except Exception as e:
        return f'Algo deu errado \n\n{e}'

@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome":"João"}
        requisicao = requests.patch(f'{link}/cadastrar/-O8JEUw1XyLSKUCa02Jz/.json', data=json.dumps(dados))
        return "Atualizado com sucesso!"
    except Exception as e:
        return f'Algo deu errado\n\n {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastrar/-O8JEUw1XyLSKUCa02Jz/.json')
        return "Excluído com sucesso!"
    except Exception as e:
        return f"Algo deu errado \n\n {e}"


