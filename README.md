# Plataforma de Gestão de Tarefas e Projetos

Este projeto consiste numa API RESTful desenvolvida em Python com o framework Flask para a gestão de tarefas e projetos. A aplicação foi estruturada seguindo as melhores práticas de desenvolvimento, incluindo testes unitários automatizados e um pipeline de Integração Contínua (CI) via GitHub Actions.

---

## Estrutura do Projeto

O repositório está organizado da seguinte forma:

```text
trabalho-final04/
├── .github/
│   └── workflows/
│       └── ci.yml          # Configuração do Pipeline de CI (GitHub Actions)
├── api/
│   ├── app.py              # Código-fonte principal da API Flask
│   ├── data/
│   │   └── tarefas.json    # Base de dados simulada (Massa de dados)
│   └── testes/
│       └── teste_api.py    # Suite de testes unitários (Pytest)
├── .gitignore              # Definição de ficheiros ignorados pelo Git
├── README.md               # Documentação do projeto
└── requerimentos.txt       # Dependências do ecossistema Python
```

---

##  Tecnologias Utilizadas

* **Python 3.10+**: Linguagem de programação base.
* **Flask**: Micro-framework para construção da API REST.
* **Pytest & Pytest-Flask**: Framework para escrita e execução de testes unitários.
* **Flake8**: Ferramenta de análise estática (Linting) para garantir a qualidade do código.
* **GitHub Actions**: Plataforma de automação para o pipeline de CI.

---

##  Como Executar o Projeto Localmente

### Pré-requisitos
Certifique-se de que tem o Python instalado na sua máquina.

### 1. Clonar o Repositório e Acessar a Pasta
```bash
git clone <https://github.com/andersonniltondesouza-unidavi/trabalho-final04>
cd trabalho-final04
```

### 2. Criar e Ativar o Ambiente Virtual (Virtualenv)
```bash
# Criar o ambiente isolado
python -m venv venv

# Ativar no Windows (Prompt de Comando):
venv\Scripts\activate

# Ativar no Linux:
source venv/bin/activate
```

### 3. Instalar as Dependências
```bash
pip install -r requerimentos.txt
```

### 4. Executar a API
```bash
python api/app.py
```
A API ficará disponível em: `http://127.0.0.1:5000/`

---

## Rotas da API (End-points)

| Método | Rota | Descrição | Status Sucesso |
| :--- | :--- | :--- | :--- |
| **GET** | `/status` | Verifica a integridade e versão da API | `200 OK` |
| **GET** | `/tarefas` | Retorna a lista completa com todas as tarefas | `200 OK` |
| **GET** | `/tarefas/<id>` | Busca uma tarefa específica pelo ID | `200 OK` / `404 Not Found` |

---

## Execução dos Testes Unitários

Para garantir o correto funcionamento da aplicação e validar os contratos das rotas, execute o comando abaixo no terminal (com o ambiente virtual ativo):

```bash
# Define o PYTHONPATH e executa o Pytest
PYTHONPATH=. pytest api/testes/ -v
```

A suite valida 4 cenários essenciais:
1. Retorno de Status `200 OK` na listagem.
2. Presença dos campos obrigatórios na estrutura do JSON.
3. Tratamento de erro `404` para registros inexistentes.
4. Validação autoral da rota de status da API.

---

## ntegração Contínua (CI) - GitHub Actions

O projeto conta com um fluxo de **Integração Contínua** configurado no arquivo `.github/workflows/ci.yml`. 

Sempre que é efetuado um `push` ou um `pull request` para a branch `main`, o GitHub Actions inicia automaticamente uma máquina virtual (Ubuntu) e executa os seguintes passos:

1. **Checkout do Código**: Baixa o código para o ambiente virtual de testes.
2. **Setup do Python**: Configura a versão correta do interpretador.
3. **Instalação**: Instala as dependências listadas no `requerimentos.txt`.
4. **Linting (Flake8)**: Analisa a sintaxe do código à procura de más práticas ou erros.
5. **Testes Automatizados (Pytest)**: Executa a suite de testes unitários. Se algum teste falhar, o pipeline falha, impedindo a integração de código instável.

---
Desenvolvido por **Anderson Nilton de Souza** - Junho de 2026.
