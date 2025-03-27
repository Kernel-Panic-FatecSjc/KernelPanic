import pandas as pd
import mysql.connector
from mysql.connector import Error
import os

#-----------------------AVISO!!!----------------------#
#Coloque os arquivos CSV na pasta data e rode o codigo
#

# Função para inserção de dados no Banco
def generateQuerry(table: str, columns: list[str], values: list):
    formatted_values = []
    
    for value in values:
        if isinstance(value, str):
            value = value.replace("'", "''")
            formatted_values.append(f"'{value}'")
        else:
            formatted_values.append(str(value))
    
    columns_str = ", ".join(columns)
    values_str = ", ".join(formatted_values)
    query = f"""INSERT INTO {table} ({columns_str}) VALUES ({values_str})"""
    return query

# Função de inserção 
def insertValues(dataFrame: pd.DataFrame, generateQuerry: callable, table_name: str, columns: list[str]):
    cursor = connection.cursor()
    loading_count = 100 / len(dataFrame)
    loading = 0

    for _, row in dataFrame.iterrows():
        try:
            query = generateQuerry(table_name, columns, row.tolist())
            cursor.execute(query)
            print(query)
        except Exception as e:
            print(f"Erro ao inserir linha: {e}. Ignorando...")
            continue
        loading += loading_count
        print(f"Carregando {table_name}: {round(loading, 2)}%", end='\r')
    
    print(f"{table_name} inseridos!")

base_dir = os.path.dirname(os.path.abspath(__file__))

# Diretório do Projeto
importacoesSP = os.path.join(base_dir, "data", "importacoesSP.csv")
exportacoesSP = os.path.join(base_dir, "data", "exportacoesSP.csv")
municipios = os.path.join(base_dir, "data", "municipiosSP.csv")
paises = os.path.join(base_dir, "data", "paises.csv")
sh4 = os.path.join(base_dir, "data", "sh4.csv")

df_paises = pd.read_csv(paises, sep=";", encoding="latin1")
df_sh4 = pd.read_csv(sh4, sep=";", encoding="latin1")
df_municipios = pd.read_csv(municipios, sep=";", encoding="latin1")
df_exportacoes = pd.read_csv(exportacoesSP, sep=";", encoding="latin1")
df_importacoes = pd.read_csv(importacoesSP, sep=";", encoding="latin1")

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='api',  
        user='root', 
        password='1234'  
    )

    if connection.is_connected():
        print("Conexão com o MySQL foi bem-sucedida!")
        cursor = connection.cursor()

        # Inserir Países
        insertValues(df_paises, generateQuerry, "pais", ["co_pais", "co_pais_isoa3", "no_pais"])

        # Inserir Códigos SH4
        insertValues(df_sh4, generateQuerry, "sh", ["co_sh4", "no_sh4_por"])

        # Inserir Municípios
        insertValues(df_municipios, generateQuerry, "municipios", ["co_mun", "no_mun", "sg_uf_mun"])

        # Inserir Exportações
        insertValues(df_exportacoes, generateQuerry, "exportacao", ["co_ano", "co_mes", "co_sh4", "co_pais", "sg_uf_ncm", "co_mun", "kg_liquido_expt", "vl_fob_expt", "valor_agregado"])

        # Inserir Importações
        insertValues(df_importacoes, generateQuerry, "importacao", ["co_ano", "co_mes", "co_sh4", "co_pais", "sg_uf_ncm", "co_mun", "kg_liquido_expt", "vl_fob_expt", "valor_agregado"])

        connection.commit()
        print("Dados inseridos com sucesso!")

except Error as e:
    print(f"Erro ao conectar ou inserir no MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com MySQL fechada.")
