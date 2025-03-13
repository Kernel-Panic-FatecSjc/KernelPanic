
import pandas as pd
import requests
from io import StringIO
low_memory = False
# %matplotlib inline
pd.options.display.max_columns = 100
pd.options.display.max_rows = 100

urls = [
    'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2023_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2022_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2021_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2020_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2019_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2018_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2017_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2016_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2015_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2014_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2013_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/tabelas/UF_MUN.csv',
    'https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_SH.csv'
]

dfs = []

for url in urls:
    response = requests.get(url)
    df = pd.read_csv(StringIO(response.text), sep=';', encoding="latin1")
    if "EXP" in url:
      ano = url.split('_')[1]
      df['Ano'] = ano
    dfs.append(df)

df_final = pd.concat(dfs, ignore_index=True)

print(df_final.head())

df.rename(columns={'CO_ANO' : 'CODIGOANO', 'CO_MES' : 'MES', 'CO_NCM' : 'CODIGONCM', 'CO_UNID' : 'CODIGOUNIDADE','CO_PAIS' : 'CODIGOPAIS','SG_UF_MUN'
                   : 'ESTADO', 'CO_MUN' : 'CODIGOMUNICIPIO', 'CO_VIA' : 'CODIGOVIA', 'CO_URF' : 'CODIGOURF', 'QT_ESTAT' : 'QUANTIDADE','KG_LIQUIDO' : 'PESOKG', 'VL_FOB' : 'VALORFOB'}, inplace=True)

df = df.drop(columns=['NO_SH6_ESP' , 'NO_SH6_ING' , 'NO_SH4_ESP' , 'NO_SH4_ING' , 'NO_SH2_ESP', 'NO_SH2_ING' , 'NO_SEC_ESP' , 'NO_SEC_ING'])

df.sample(5)

df['VALORAGREGADO'] = df['VALORFOB'] / df['PESOKG']

df = df[df['PESOKG']>0]

municipio_agregado = df.groupby(['CODIGOMUNICIPIO', 'ESTADO', 'SH4'])['VALORAGREGADO'].mean().reset_index()

df_mun = df_mun.rename(columns={"CO_MUN_GEO": "CODIGOMUNICIPIO"})

municipio_agregado = municipio_agregado.merge(df_mun, on=["CODIGOMUNICIPIO"], how="left")

df_sh4 = df_sh4.rename(columns={"CO_SH4": "SH4", "NO_SH4_POR": "PRODUTO"})

municipio_agregado = municipio_agregado.merge(df_sh4, on=["SH4"], how="left")

municipio_agregado = municipio_agregado[municipio_agregado["ESTADO"] == "SP"]

municipio_top20 = municipio_agregado.sort_values(by="VALORAGREGADO", ascending=False).head(20)

print(municipio_top20[["NO_MUN_MIN", "SG_UF", "PRODUTO", "VALORAGREGADO"]])