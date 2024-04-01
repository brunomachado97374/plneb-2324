from flask import Flask, render_template , request
import json

app = Flask(__name__)

with open("plneb-2324/TPC6/conceitos.json", encoding='utf-8') as file_conceitos:
    conceitos = json.load(file_conceitos)

@app.route("/")

def home():
    return render_template("home.html")



@app.route("/conceitos")
def listar_Conceitos():

    return render_template('conceitos.html', conceitos = conceitos)


@app.route("/conceitos/<designacao>")
def consultar_Conceitos(designacao):
    #return conceitos[designacao]

    if designacao in conceitos:
        conceito_desi = conceitos[designacao]
        desi = designacao
        return render_template('designacoes.html', conceito_desi = conceito_desi , desi = desi )
    
    else:
        return "Conceito não encontrado", 404
    


# Configuração para aceitar solicitações PUT, POST e DELETE como PUT
@app.before_request
def before_request():
    if request.method == 'POST' and request.form.get('_method'):
        request.environ['REQUEST_METHOD'] = request.form['_method'].upper()



@app.route("/conceitos/<designacao>", methods=["PUT", "POST"])
def editar_Conceitos(designacao):
    #return conceitos[designacao]

    if request.method == "PUT" or request.method == "POST":
        if designacao in conceitos:

            dados_atualizados = request.form
            conceitos[designacao].update(dados_atualizados)
            return render_template("designacoes.html", desi=designacao, conceito_desi=conceitos[designacao]), 200
        
        else:
            return "Conceito não encontrado", 404


app.run(host="localhost", port=4002, debug=True)