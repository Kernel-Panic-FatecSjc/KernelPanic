from flask import Flask,jsonify
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

@app.route('/getTable', methods)
def getTables():
    cursor = con.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    cursor.close()
    con.close()
    table_names = [table[0] for table in tables]
    return jsonify({"tables": table_names}),200


    if __name__ == "__main__":
        print("Conectando ao banco")
        app.run(debug = true)