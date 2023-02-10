import pandas as pd

combustiveis_df = pd.read_excel("ca-2021-02.xlsx")

print(combustiveis_df)

# Adicionar nova coluna
combustiveis_df['Ativo'] = True
print(combustiveis_df.head())

# Nova coluna com condição
combustiveis_df["Obs"] = ["MELHOR CIDADE" if municipio == "SALVADOR" else "" for municipio in combustiveis_df['Municipio']]
print(combustiveis_df.loc[combustiveis_df['Municipio'].isin(["SALVADOR", "JEQUIE"])])


import numpy as np

# Nova coluna com condição com numpy
combustiveis_df['Status Valor de Venda'] = np.where(combustiveis_df["Valor de Venda"] >= 6.5, "CARO", "BARATO")
print(combustiveis_df[['Revenda', "Valor de Venda", 'Status Valor de Venda']])

# Nova tabela 
num_habitantes_df = pd.read_csv("ibge_num_habitantes_estimado.csv")
print(num_habitantes_df)

# Trocar nome da coluna
num_habitantes_df.rename(columns={'Estado': 'Estado - Sigla'}, inplace=True)
print(num_habitantes_df)

# Criar nova mesclando duas tabelas
colunas = ['Municipio', 'Estado - Sigla']
# merge_df = combustiveis_df.merge(num_habitantes_df, how="right", on=colunas)
# merge_df = combustiveis_df.merge(num_habitantes_df, how="left", on=colunas)
# merge_df = combustiveis_df.merge(num_habitantes_df, how="outer", on=colunas)
merge_df = combustiveis_df.merge(num_habitantes_df, how="inner", on=colunas)
print(merge_df)
print(merge_df.shape)

# Renovendo colunas vazias
merge_df.dropna(axis='columns', inplace=True)
print(merge_df.info())

# Remover colunas
print(merge_df.columns)
columns = ['Regiao - Sigla', 'Nome da Rua', 'Numero Rua', 'Bairro', 'Cep',
       'Produto', 'Valor de Venda', 'Unidade de Medida',
       'Bandeira', 'Ativo', 'Status Valor de Venda', 'Data da Coleta', 'Obs']
merge_df.drop(labels=columns, axis=1, inplace=True)
print(merge_df.info())
print(merge_df.head(100))

# Remover linhas duplicadas
merge_df.drop_duplicates(inplace=True)
print(merge_df.head(100))

# Nova tabela juntando linhas com mesmas informações
postos_por_municipio_df = merge_df.groupby(by=['Estado - Sigla', 'Municipio', "NumHabitantes2021"]).count()
postos_por_municipio_df.drop('CNPJ da Revenda', axis=1, inplace=True)
postos_por_municipio_df.reset_index(inplace=True)
postos_por_municipio_df.rename(columns={"Revenda":"Numero de Postos"}, inplace=True)
print(postos_por_municipio_df)
print(postos_por_municipio_df.info())

# Calculo de postos por habitante
postos_por_municipio_df['PostosPorHabitante'] = postos_por_municipio_df['Numero de Postos'] / postos_por_municipio_df['NumHabitantes2021']
print(postos_por_municipio_df)