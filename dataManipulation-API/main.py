import pandas as pd
import mysql.connector
from mysql.connector import Error

# Carregar o arquivo CSV
file = "excelFile/Dados.csv"
df = pd.read_csv(file)

# Conectar ao banco de dados MySQL
try:
    connection = mysql.connector.connect(
        host='localhost',  # Substitua pelo seu host MySQL
        database='seu_banco_de_dados',  # Substitua pelo nome do seu banco de dados
        user='seu_usuario',  # Substitua pelo seu nome de usuário
        password='sua_senha'  # Substitua pela sua senha
    )

    if connection.is_connected():
        print("Conexão com MySQL bem-sucedida!")

        # Criar um cursor para executar comandos SQL
        cursor = connection.cursor()

        # Inserir dados na tabela MySQL
        for i, row in df.iterrows():
            # Preparar o comando SQL de inserção (substitua 'tabela_destino' pelo nome da sua tabela)
            insert_query = """
            INSERT INTO tabela (CO_ANO, CO_MES, SH4, CO_PAIS, SG_UF_MUN, CO_MUN, KG_LIQUIDO, VL_FOB)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Os valores da linha são passados como uma tupla
            cursor.execute(insert_query, tuple(row))

        # Commit das alterações
        connection.commit()
        print(f"{cursor.rowcount} registros inseridos com sucesso!")

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com MySQL fechada.")