from flask import Flask, render_template, request, jsonify
from query import montar_query
import pymysql

app = Flask(__name__)

# Dados para conectar ao banco de dados
def get_db_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='api',
        cursorclass=pymysql.cursors.DictCursor 
    )
    print("COnexao feita!")
    return conn

@app.route("/")
def website():
    return render_template('index.html')

# Recebimento dos dados via POST
@app.route('/filtros', methods=['POST'])
def filtros_dados():
    filtros = request.get_json()

    try:
        query, params = montar_query(filtros)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        resultados = cursor.fetchall()
    conn.close()

    # Se estiver agrupando por mês, retorna lista com dados por mês
    if "mes" not in filtros:
        resposta = []
        for row in resultados:
            resposta.append({
                "tipo": filtros.get("tipo"),
                "ano": filtros.get("ano"),
                "mes": row["mes"],
                "municipio": filtros.get("municipio"),
                "pais": filtros.get("pais"),
                "ncm": filtros.get("ncm"),
                "total_valor_agregado": row["total_valor_agregado"],
                "total_kg_liquido": row["total_kg_liquido"],
                "total_valor_fob": row["total_valor_fob"],
                "total_registros": row["total_registros"]
            })
    else:
        row = resultados[0]
        resposta = {
            "tipo": filtros.get("tipo"),
            "ano": filtros.get("ano"),
            "mes": filtros.get("mes"),
            "municipio": filtros.get("municipio"),
            "pais": filtros.get("pais"),
            "ncm": filtros.get("ncm"),
            "total_valor_agregado": row["total_valor_agregado"],
            "total_kg_liquido": row["total_kg_liquido"],
            "total_valor_fob": row["total_valor_fob"],
            "total_registros": row["total_registros"]
        }

    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)