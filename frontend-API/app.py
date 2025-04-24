from flask import Flask, render_template, request, jsonify
from query import montar_query
import pymysql

app = Flask(__name__)

# Dados para conectar ao banco de dados
def get_db_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='api',
        cursorclass=pymysql.cursors.DictCursor 
    )
    print("COnexao feita!")
    return conn

@app.route("/")
def website():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM pais")  
        resultadosPaises = cursor.fetchall()
        
        cursor.execute("Select * from municipios")
        resultadosMunicipios = cursor.fetchall()

    conn.close()
    return render_template('index.html', paises=resultadosPaises, municipios=resultadosMunicipios)

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

    if filtros.get("ano") != "todos" and filtros.get("mes") == "todos":
        resposta = []
        for mes in range(1, 13):
            dados_mes = next((row for row in resultados if row.get("mes") == mes), None)
            total_valor_fob = dados_mes.get("total_valor_fob", 0) if dados_mes else 0
            total_kg_liquido = dados_mes.get("total_kg_liquido", 0) if dados_mes else 0
            valor_agregado = round(float(total_valor_fob) / float(total_kg_liquido), 2) if total_kg_liquido else 0
            resposta.append({
                "tipo": filtros.get("tipo"),
                "ano": filtros.get("ano"),
                "mes": mes,
                "municipio": filtros.get("municipio"),
                "pais": filtros.get("pais"),
                "ncm": filtros.get("ncm"),
                "total_valor_agregado": valor_agregado,
                "total_valor_fob": total_valor_fob,
                "total_kg_liquido": total_kg_liquido,
                "total_registros": dados_mes.get("total_registros", 0) if dados_mes else 0
            })

    elif filtros.get("ano") == "todos" and filtros.get("mes") == "todos":
        resposta = []
        for row in resultados:
            total_valor_fob = row.get("total_valor_fob", 0)
            total_kg_liquido = row.get("total_kg_liquido", 0)
            valor_agregado = round(float(total_valor_fob) / float(total_kg_liquido), 2) if total_kg_liquido else 0
            resposta.append({
                "tipo": filtros.get("tipo"),
                "ano": row.get("ano"),
                "municipio": filtros.get("municipio"),
                "pais": filtros.get("pais"),
                "ncm": filtros.get("ncm"),
                "total_valor_agregado": valor_agregado,
                "total_valor_fob": total_valor_fob,
                "total_kg_liquido": total_kg_liquido,
                "total_registros": row.get("total_registros", 0)
            })

    else:
        row = resultados[0] if resultados else {}
        total_valor_fob = row.get("total_valor_fob", 0)
        total_kg_liquido = row.get("total_kg_liquido", 0)
        valor_agregado = round(float(total_valor_fob) / float(total_kg_liquido), 2) if total_kg_liquido else 0
        resposta = {
            "tipo": filtros.get("tipo"),
            "ano": filtros.get("ano"),
            "mes": filtros.get("mes"),
            "municipio": filtros.get("municipio"),
            "pais": filtros.get("pais"),
            "ncm": filtros.get("ncm"),
            "total_valor_agregado": valor_agregado,
            "total_valor_fob": total_valor_fob,
            "total_kg_liquido": total_kg_liquido,
            "total_registros": row.get("total_registros", 0)
        }

    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)