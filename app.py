from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/<int:id>')
def pessoas(id):
    return jsonify(
        {'id': id, 'nome': 'Vinicius', 'profissao': 'Desenvolvedor'
         })


# Utilizando Método POST
@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)  # Trás as informações do body, usamos a biblioteca json para converter em json
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10+10
    return jsonify({'soma': total})


if __name__ == '__main__':
    app.run(debug=True)
