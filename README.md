# 📈 Automação de Dados de Câmbio (Python & SQL)

Este projeto realiza a extração automática de cotações de moedas, trata os dados e os armazena em um banco de dados relacional para análises futuras.

## 🚀 Funcionalidades
- **Coleta Automatizada:** Busca dados da AwesomeAPI em intervalos programados.
- **Tratamento de Dados:** Utiliza Pandas para limpeza e tipagem correta dos dados.
- **Persistência SQL:** Armazena o histórico em SQLite para evitar perda de dados.
- **Resiliência:** Tratamento de erros de conexão (Timeout) e de permissão de arquivo.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Bibliotecas:** Pandas, Requests, SQLite3
- **Banco de Dados:** SQLite
- **Ferramentas:** VS Code, DBeaver

## 📂 Como executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute o script: `python main.py`