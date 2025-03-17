import pandas as pd
import matplotlib.pyplot as plt
low_memory = False

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
urls_baixadas = []

for url in urls:
    try:
      df = pd.read_csv(url, sep=';', encoding="latin1")
      dfs.append(df)
      urls_baixadas.append(url)
      print (f'Baixadas! {url}')
    except Exception as Ex:
            print(f"Erro ao baixar {url}: {e}")

print(f"Total de arquivos carregados: {len(urls_baixadas)}")

if dfs:
    df_final = pd.concat(dfs, ignore_index=True)
    print(df_final.head())

df = df.drop(columns=['NO_SH6_ESP' , 'NO_SH6_ING' , 'NO_SH4_ESP' , 'NO_SH4_ING' , 'NO_SH2_ESP', 'NO_SH2_ING' , 'NO_SEC_ESP' , 'NO_SEC_ING'])

df_final['VL_FOB'] = pd.to_numeric(df_final['VL_FOB'], errors='coerce')
df_final['KG_LIQUIDO'] = pd.to_numeric(df_final['KG_LIQUIDO'], errors='coerce')
df_final['CO_ANO'] = pd.to_numeric(df_final['CO_ANO'], errors='coerce')

df_final = df_final[df_final['KG_LIQUIDO'] > 0]
df_final['VALOR AGREGADO'] = df_final['VL_FOB'] / df_final['KG_LIQUIDO']

valor_agregado_por_ano = df_final.groupby('CO_ANO')['VALOR AGREGADO'].mean()

print(df_final.groupby('CO_ANO')['VALOR AGREGADO'].describe())

plt.figure(figsize=(10, 6))
plt.plot(valor_agregado_por_ano.index, valor_agregado_por_ano.values, marker='o', linestyle='-', color='b', label= 'Valor Agregado Médio')
plt.xlabel('Ano')
plt.ylabel('Valor Agregado')
plt.title('Evolução do Valor Agregado ao Longo dos anos')
plt.grid(True, alpha=0.6)
plt.legend()
plt.show()