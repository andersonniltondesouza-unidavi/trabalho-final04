from flask import Flask, jsonify, abort
import json
import os

app = Flask(__name__)

# Função auxiliar para carregar os dados
def carregar_tarefas():
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'data', 'tarefas.json')
    try:
        with open(caminho_arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        abort(500, description="Erro interno: Arquivo de dados não encontrado.")

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "nome": "API de Gestão de Tarefas",
        "versao": "1.0.0",
        "status": "operacional"
    }), 200

@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = carregar_tarefas()
    return jsonify(tarefas), 200

@app.route('/tarefas/<int:tarefa_id>', methods=['GET'])
def get_tarefa_por_id(tarefa_id):
    tarefas = carregar_tarefas()
    tarefa = next((t for t in tarefas if t['id'] == tarefa_id), None)
    
    if tarefa is None:
        abort(404, description="Tarefa não encontrada")
        
    return jsonify(tarefa), 200

# Tratamento de erro 404 personalizado para retornar JSON estruturado
@app.errorhandler(404)
def not_found(error):
    return jsonify({"erro": str(error.description)}), 404

# Tratamento de erro 500 personalizado
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"erro": str(error.description)}), 500

if __name__ == '__main__':
    app.run(debug=True)
