# Importando as bibliotecas e arquivos
from flask import Flask, request, jsonify
from flask_restx import Api, Resource

# Importando controle responsável pela avaliação dos nomes
from src.controlers.evaluation_name import *

# Instannciando nossa API
app = Flask(__name__)
api = Api(app,
        version = '1.0',
        title = 'bNaming API',
        description = 'Api de um sistema para auxiliara a avaliar a qualidade de um nome de uma marca.',
        doc = '/docs'
        )

# Definindo nossas rotas

# Rotas de avaliação
@api.route('/evaluation')
class Evaluation(Resource):

    def get(self,):
        print("Entrou no GET")
        return jsonify({"Messagem":"Utilize o metodo POST e envie o nome e o segmento em um JSON para que possamos realizar a avaliacao do nome."})

    def post(self,):
        dados = request.json
        nome = dados['nome']
        segmento = dados['segmento']

        return jsonify(predicao_classificacao(nome, segmento))

# Executando nossa API
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    


