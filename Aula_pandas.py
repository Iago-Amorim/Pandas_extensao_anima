# Pimeiro código com python e pandas
# Autor: Iago Amorim e professor

import pandas as pd

combustivel_df = pd.read_csv("precos_combustivel_2022.csv", on_bad_lines='skip')

print(combustivel_df)