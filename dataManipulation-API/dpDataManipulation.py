import pandas as pd
import mysql.connector
from mysql.connector import Error

#Função para inserção de dados no Banco
def insertValues(table: str, columns: list[str], values: list):
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


importacoesSP = r"D:\GitHub\KernelPanic\dataManipulation-API\data\importacoesSP.csv"
exportacoesSP = r"D:\GitHub\KernelPanic\dataManipulation-API\data\exportacoesSP.csv"
municipios = r"D:\GitHub\KernelPanic\dataManipulation-API\data\municipiosSP.csv"
paises = r"D:\GitHub\KernelPanic\dataManipulation-API\data\paises.csv"
sh4 = r"D:\GitHub\KernelPanic\dataManipulation-API\data\sh4.csv"


df_paises = pd.read_csv(paises, sep=";")
df_sh4 = pd.read_csv(sh4, sep=";")
df_municipios = pd.read_csv(municipios, sep=";")
df_exportacoes = pd.read_csv(exportacoesSP, sep=";")
df_importacoes = pd.read_csv(importacoesSP, sep=";")



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

        for _, row in df_paises.iterrows():
            query = insertValues("pais", ["co_pais", "co_pais_isoa3", "no_pais"], row.tolist())
            cursor.execute(query)
        print("pais")

        for _, row in df_sh4.iterrows():
            query = insertValues("sh", ["co_sh4", "no_sh4_por"], row.tolist())
            cursor.execute(query)
        print("sh")

        for _, row in df_municipios.iterrows():
            query = insertValues("municipios", ["co_mun" ,"no_mun", "sg_uf_mun"], row.tolist())
            cursor.execute(query)
        print("municipio")

        for _, row in df_exportacoes.iterrows():
            query = insertValues("exportacao", ["co_ano", "co_mes", "co_ncm", "co_pais", "sg_uf_ncm", "co_mun", "kg_liquido_expt", "vl_fob_expt", "valor_agregado"], row.tolist())
            cursor.execute(query)
        
        for _, row in df_exportacoes.iterrows():
            query = insertValues("importacao", ["co_ano", "co_mes", "co_ncm", "co_pais", "sg_uf_ncm", "co_mun", "kg_liquido_expt", "vl_fob_expt", "valor_agregado"], row.tolist())
            cursor.execute(query)

        connection.commit()
        print("Dados inseridos com sucesso!")

except Error as e:
    print(f"Erro ao conectar ou inserir no MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com MySQL fechada.")