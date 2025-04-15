from flask import Flask,jsonify, request
import mysql.connector




#atualizar os dados com as reais configurações do banco

app = Flask(__name__)
con = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'root123',
    database = 'nomedobanco'
)


#O outro método Get de pegar os dados e nome de cada tabela já está pronto, mas vou commitar junto com o banco verdadeiro >:D
#Esse aqui só pega o nome das tabelas(só pra testar se tá funcionando)

@app.route('/getTable', methods=['GET'])
def getTables():
    cursor = con.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    cursor.close()
    con.close()
    table_names = [table[0] for table in tables]
    return jsonify({"tables": table_names}),200

@app.route('/api/filtros', methods=['GET'])
def filtros_dados():
    municipio = request.args.get('municipio')
    pais = request.args.get ('pais')
    ano = request.args.get ('ano')
    carga = request.args.get ('carga')

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
    
    cursor = con.cursor(dictionary=True)
    cursor.execute(query, filtros)
    resultados = cursor.fetchall()
    cursor.close()


    if __name__ == "__main__":
        print("Conectando ao banco")
        app.run(debug = true)