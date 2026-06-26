import pytest
from api.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Retorno HTTP 200 para a rota GET 
def test_get_tarefas_status_200(client):
    response = client.get('/tarefas')
    assert response.status_code == 200

# Validação do JSON retornado
def test_get_tarefas_estrutura_json(client):
    response = client.get('/tarefas')
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 10
    campos_obrigatorios = ['id', 'titulo', 'status', 'prioridade']
    for campo in campos_obrigatorios:
        assert campo in data[0]

# Retorno HTTP 404 para um ID inexistente
def test_get_tarefa_inexistente_404(client):
    response = client.get('/tarefas/9999')
    assert response.status_code == 404

# Valida a rota de status
def test_get_status_valido(client):
    response = client.get('/status')
    data = response.get_json()
    assert response.status_code == 200
    assert data['status'] == "operacional"
