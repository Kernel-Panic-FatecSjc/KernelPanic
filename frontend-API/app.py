from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)


#atualizar os dados com as reais configurações do banco

app = Flask(__name__)

#Dados para conectar ao banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root123',
        database='nomedobanco'
    )

connection = get_db_connection()

@app.route("/")
def website():
    return render_template('index.html')


#REcebimento dos dados via POST
@app.route('/filtros', methods=['POST'])
def filtros_dados():
    dados = request.get_json()
    municipio = dados.get('municipio')
    pais = dados.get ('pais')
    ano = dados.get ('ano')
    carga = dados.get ('carga')

    query = """
        SELECT 
            CO_ANO, 
            CO_UF, 
            CO_PAIS, 
            CO_NCM, 
            KG_LIQUIDO, 
            VL_FOB, 
            VALOR_AGREGADO 
        FROM comex_registro 
        WHERE 1=1
    """
    
    filtros = []

    if municipio:
        query += "AND CO_UF = %s"
        filtros.append(municipio)
    if pais:
        query += " AND CO_PAIS = %s"
        filtros.append(pais)
    if ano:
        query += " AND ANO = %s"
        filtros.append(ano)
    if carga:
        query += " AND CO_NCM = %s"
        filtros.append(carga)
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, filtros)
    resultados = cursor.fetchall()
    cursor.close()


if __name__ == '__main__':
    app.run(debug =True)

