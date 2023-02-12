import pandas as pd
import matplotlib.pyplot as plt

# Tabela principal
ver_df = pd.read_csv("paar_nov_2022.csv", encoding='latin-1', sep=";")
ver_df.rename(columns={'Possui Medalha de <br /> Mérito Desportivo Militar': 'Possui Medalha de Mérito Desportivo Militar'}, inplace=True)
df_remove = ver_df.loc[(ver_df['Estado'].isin(['55', '5562']))]
ver_df.drop(df_remove.index, inplace=True)
print(ver_df)

# Tabela com a quantidade de cada sexo
sexo_df = ver_df['Sexo'].value_counts().reset_index()
sexo_df.rename(columns={'Sexo':'Quantidade'}, inplace=True)
sexo_df.rename(columns={'index':'Sexo'}, inplace=True)
print(sexo_df)

# Mostra gráfico
sexo_df.plot(
    x='Sexo', 
    y='Quantidade', 
    kind='bar',
    title="Tabela quantidade por sexo" 
)
plt.show()

# Tabela quantidade por sexo dos participantes por estado
sexo_estado_df = ver_df[['Estado', 'Sexo']].value_counts().reset_index()
sexo_estado_df.rename(columns={0: 'Quantidade'}, inplace=True)
print(sexo_estado_df)

# Mostra gráfico com quantidade de homem por estado
sexo_estado_df.loc[(sexo_estado_df['Sexo']=='Masculino')].plot(x='Estado', y='Quantidade', kind='bar', title='Quantidade de Homens por Estado', figsize=(20, 5))
plt.show()

# Mostra gráfico com quantidade de mulheres por estado
sexo_estado_df.loc[(sexo_estado_df['Sexo']=='Feminino')].plot(x='Estado', y='Quantidade', kind='bar', title='Quantidade de Mulheres por Estado', figsize=(20, 5), color='pink')
plt.show()

# Tabela com a quantidade de participantes de cada intituição militar
forcas_df = ver_df['Força'].value_counts().reset_index()
forcas_df.rename(columns={'Força':'Quantidade'}, inplace=True)
forcas_df.rename(columns={'index':'Força'}, inplace=True)
print(forcas_df)

# Mostra gráfico com a quantidade de participantes de cada intituição militar
forcas_df.plot(x='Força', y='Quantidade', kind='bar', title='Quantidade de pessoas de cada instituição militar', figsize=(10, 5))
plt.show()

# Tabela com os cargos dos militares 
postos_G_df = ver_df['Posto Graduação'].value_counts().reset_index()
postos_G_df.rename(columns={'Posto Graduação':'Quantidade'}, inplace=True)
postos_G_df.rename(columns={'index':'Posto Graduação'}, inplace=True)
print(postos_G_df)

# Grafico das patentes dos militares
postos_G_df.plot(x='Posto Graduação', y='Quantidade', kind='bar', title='Quantidade de pessoas por posto praduação', figsize=(10, 5))
plt.show()

# Tabela com as modalidades
modalidades_df = ver_df['Modalidade'].value_counts().reset_index()
modalidades_df.rename(columns={'Modalidade':'Quantidade'}, inplace=True)
modalidades_df.rename(columns={'index':'Modalidade'}, inplace=True)
print(modalidades_df)

# Tabela sobre o atletismo
atletismo_df = ver_df.loc[ver_df['Modalidade'] == 'Atletismo']
print(atletismo_df)

# Gráfico com quantidade depessoas no atletismo pelo sexo 
atletismo_df = atletismo_df['Sexo'].value_counts().reset_index()
atletismo_df.rename(columns={'Sexo':'Quantidade'}, inplace=True)
atletismo_df.rename(columns={'index':'Sexo'}, inplace=True)
atletismo_df.plot(x='Sexo', y='Quantidade', kind='bar', title='Quantidade de pessoas no atletismo', figsize=(10, 5))
plt.show()

# Verificar quantos tem bolsa atleta
possui_Bolsa_Atleta_df = ver_df['Possui Bolsa Atleta'].value_counts().reset_index()
possui_Bolsa_Atleta_df.rename(columns={'Possui Bolsa Atleta':'Quantidade'}, inplace=True)
possui_Bolsa_Atleta_df.rename(columns={'index':'Possui Bolsa Atleta'}, inplace=True)
print(possui_Bolsa_Atleta_df)

# Gráfico com a quantidade de bolsa atleta
possui_Bolsa_Atleta_df.plot(x='Possui Bolsa Atleta', y='Quantidade', kind='bar', title='Quantidade de pessoas com bolsa atleta', figsize=(10, 5))
plt.show()

