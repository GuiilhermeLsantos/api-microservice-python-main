import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

db_config = {
    'user': 'root',
    'host': 'localhost',
    'database': 'alunos'
}
# Página inicial
@app.route('/')
def hello_world():
    return 'Página inicial!'

# Rota para buscar todos os registros dos alunos
@app.route('/api/registros', methods=['GET'])
def get_registros():

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Executa a consulta SQL para buscar todos os registros
    query = 'SELECT * FROM alunos_info;'
    cursor.execute(query)

    # Obtém os resultados da consulta
    resultados = cursor.fetchall()

    # Fecha a conexão com o banco de dados
    cursor.close()
    conn.close()

    # Retorna os resultados da consulta em formato JSON
    return jsonify(resultados)
    

# Rota para cadastrar um novo registro
@app.route('/api/cadastro', methods=['POST'])
def cadastrar_registro():
    # Obtém os dados do registro a partir dos parâmetros da requisição
    nome = request.args.get('Nome')
    sobrenome = request.args.get('Sobrenome')
    turma = request.args.get('Turma')

    # Conecta ao banco de dados
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Executa a consulta SQL para inserir um novo registro na tabela "registros"
    query = 'INSERT INTO alunos_info (Nome, Sobrenome, Turma) VALUES (%s, %s, %s);'
    cursor.execute(query, (nome, sobrenome, turma))

    # Confirma as alterações no banco de dados
    conn.commit()

    # Fecha a conexão com o banco de dados
    cursor.close()
    conn.close()

    # Retorna uma mensagem indicando que o registro foi cadastrado com sucesso
    return 'Registro cadastrado com sucesso!'


# Rota para excluir um registro com um determinado ID
@app.route('/api/delete-registros', methods=['DELETE'])
def excluir_registro():
    # Obtém o ID do registro a partir dos parâmetros da requisição
    id = request.args.get('ID')

    # Conecta ao banco de dados
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Executa a consulta SQL para excluir o registro com o ID especificado
    query = 'DELETE FROM alunos_info WHERE ID = %s;'
    cursor.execute(query, (id,))

    # Confirma as alterações no banco de dados
    conn.commit()

    # Fecha a conexão com o banco de dados
    cursor.close()
    conn.close()

    # Retorna uma mensagem indicando que o registro foi excluído com sucesso
    return 'Registro excluído com sucesso!'


if __name__ == '__main__':
    app.run(debug=True)