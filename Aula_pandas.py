# Pimeiro código com python e pandas
# Autor: Iago Amorim e Professor

import pandas as pd

combustiveis_df = pd.read_excel("ca-2021-02.xlsx")

# Tabela somente com 10 linhas -----------
print(combustiveis_df.head(10))

# Lista de colunas e tamanho de colunas -----------
print(combustiveis_df.columns)
print(len(combustiveis_df.columns))

# Tamanho da lista e colunas -------------------------
print(combustiveis_df.shape)
print(combustiveis_df.shape[1])

# Informação e tipo de colunas ----------------------------
print(combustiveis_df.info())

# Mostra o valor max, min, 25%, 50%, 75% e std. 
print(combustiveis_df.describe())

# Tabela so com a coluna Revenda e com 15 linhas
print(combustiveis_df['Revenda'].head(15))

# Nova tabela so com colunas expecificas de outra tabela
ca_df = combustiveis_df[['Estado - Sigla', 'Revenda', 'Municipio', 'Produto', 'Valor de Venda']] 
print(ca_df.info())

print(ca_df)

# Mostra so uma linha ou mais
print(ca_df.loc[23243])
print(ca_df.loc[[2, 5, 10]])

# Mostra uma tabela começando do 10 e pulando de 5 em 5
print(ca_df.loc[10::5])

# Nova tabela para gasolina utilizando um filtro
gas_df = ca_df.loc[ca_df["Produto"] == "GASOLINA"]
print(gas_df)

# Verificar o maior e mínimo valor da tabela
print(gas_df.max())
print(gas_df.min())

# Tabela com produto ETANOL em Itacaranha
etn_ba = ca_df.loc[(ca_df["Produto"] == "ETANOL") & (ca_df["Municipio"] == "SALVADOR") & (ca_df["Bairro"] == "ITACARANHA")]
print(etn_ba)

# Ordenar tabela do etanol pelo valor
# etn_ba = etn_ba.sort_values(by=["Valor de Venda"])
etn_ba.sort_values(by=["Valor de Venda"], inplace=True, ascending=False)
print(etn_ba)

# Tabela com GASOLINA e GASOLINA ADITIVADA em Itacaranha
# A = combustiveis_df.loc[(combustiveis_df['Bairro'] == "ITACARANHA") & (combustiveis_df['Municipio'] == "SALVADOR") & ((combustiveis_df['Produto'] == "GASOLINA") | (combustiveis_df['Produto'] == "GASOLINA ADITIVADA"))]
print(combustiveis_df.loc[(combustiveis_df['Bairro'] == "ITACARANHA") & (combustiveis_df['Municipio'] == "SALVADOR") & (combustiveis_df['Produto'].isin(["GASOLINA", "GASOLINA ADITIVADA"])),['Valor de Venda']].mean())

# Tabela com grupo de produtos para tirar a média, min e max de cada
media_por_combustivel = ca_df[['Produto', 'Valor de Venda']].groupby(by="Produto")
print(media_por_combustivel.mean().round(2))
print(media_por_combustivel.min().round(2))
print(media_por_combustivel.max().round(2))

# Criação de tabela
combustiveis_df['Ativo'] = True
print(combustiveis_df)

# Salvar tabela
etn_ba.to_excel("Etanol_Itacaranha.xlsx")