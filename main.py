

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def bem_vindo():
    mensagem = {"Mensagem": "Bem-vindo à API NARUTO"}
    return jsonify(mensagem)

if __name__ == '__main__':
    app.run(debug=True)
