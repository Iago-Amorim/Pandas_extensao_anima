# Pimeiro código com python e pandas
# Autor: Iago Amorim e Professor

import pandas as pd

combustivel_df = pd.read_excel("ca-2021-02.xlsx")

# Tabela somente com 10 linhas -----------
print(combustivel_df.head(10))

# Lista de colunas e tamanho de colunas -----------
print(combustivel_df.columns)
print(len(combustivel_df.columns))

# Tamanho da lista e colunas -------------------------
print(combustivel_df.shape)
print(combustivel_df.shape[1])

# Informação e tipo de colunas ----------------------------
print(combustivel_df.info())

# Mostra o valor max, min, 25%, 50%, 75% e std. 
print(combustivel_df.describe())

# Tabela so com a coluna Revenda e com 15 linhas
print(combustivel_df['Revenda'].head(15))

# Nova tabela so com colunas expecificas de outra tabela
ca_df = combustivel_df[['Estado - Sigla', 'Revenda', 'Municipio', 'Produto', 'Valor de Venda']] 
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

# Verificar o maior valor da tabela
print(gas_df.max())