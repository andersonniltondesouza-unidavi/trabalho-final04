from flask import Flask, jsonify, abort
import json
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

app = Flask(__name__)

# Função auxiliar para carregar a base de dados JSON
def carregar_tarefas():
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'data', 'tarefas.json')
    try:
        with open(caminho_arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("Arquivo tarefas.json nao encontrado no disco!")
        abort(500, description="Erro interno: Arquivo de dados não encontrado.")

# Rota para verificação de status e integridade do sistema (Health Check)
@app.route('/status', methods=['GET'])
def get_status():
    logging.info("Verificacao de status (Health Check) acionada.")
    return jsonify({
        "nome": "API de Gestão de Tarefas",
        "versao": "1.0.0",
        "status": "operacional"
    }), 200

# Rota para listagem completa de todas as tarefas cadastradas
@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    logging.info("Requisicao recebida para listar todas as tarefas.")
    tarefas = carregar_tarefas()
    return jsonify(tarefas), 200

# Rota para buscar e retornar uma tarefa específica através do seu ID
@app.route('/tarefas/<int:tarefa_id>', methods=['GET'])
def get_tarefa_por_id(tarefa_id):
    logging.info(f"Buscando tarefa com ID: {tarefa_id}")
    tarefas = carregar_tarefas()
    tarefa = next((t for t in tarefas if t['id'] == tarefa_id), None)
    
    if tarefa is None:
        logging.warning(f"Tarefa com ID {tarefa_id} nao encontrada. Retornando 404.")
        abort(404, description="Tarefa não encontrada")
        
    logging.info(f"Tarefa {tarefa_id} encontrada e retornada com sucesso.")
    return jsonify(tarefa), 200

# Manipulador global para erros de rota não encontrada (HTTP 404)
@app.errorhandler(404)
def not_found(error):
    return jsonify({"erro": str(error.description)}), 404

# Manipulador global para erros internos de servidor (HTTP 500)
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"erro": str(error.description)}), 500

if __name__ == '__main__':
    logging.info("Iniciando a API de Gestao de Tarefas...")
    app.run(debug=True)
