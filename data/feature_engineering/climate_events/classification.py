# ANOM: temperature anomaly
# NINO: temperature in each region of the ocean

# https://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices

# el nino: three-month moving average of ocean temperature 0.5 degrees higher for at least 5 consecutive months
# la niña: three-month moving average of ocean temperature 0.5 degrees lower for at least 5 consecutive months
import pandas as pd


df = pd.read_csv('ORIGINAL.txt', sep=r'\s+', header=None)

df_nino = df[[0, 1, 8, 9]]
df_nino.columns = ['year', 'month', 'nino3.4', 'anom']
df_nino['date'] = pd.to_datetime(df_nino[['year', 'month']].assign(day=1))

df_nino = df_nino.sort_values('date').reset_index(drop=True)
df_nino['oni'] = df_nino['anom'].rolling(window=3).mean()

# classification
def fase_oni(x):
    if x >= 0.5:
        return 'El Nino'
    elif x <= -0.5:
        return 'La Nina'
    else:
        return 'Normal'

df_nino['fase_temp'] = df_nino['oni'].apply(lambda x: fase_oni(x) if pd.notna(x) else 'Normal')
evento_final = ['Normal'] * len(df_nino)

i = 0
while i < len(df_nino):
    fase_atual = df_nino.loc[i, 'fase_temp']

    if fase_atual == 'Normal':
        i += 1
        continue

    j = i
    while j < len(df_nino) and df_nino.loc[j, 'fase_temp'] == fase_atual:
        j += 1

    comprimento = j - i

    if comprimento >= 5:
        for k in range(i, j):
            evento_final[k] = fase_atual

    i = j

df_nino['evento'] = evento_final

# year: year of the temperature register
# month: month of the temperature register
# nino 3.4: temperature registered
# oni: temperature anomaly
# evento: climate event classification (normality, el ninõ, la ninã)
df_final = df_nino[['year', 'month', 'nino3.4', 'anom', 'oni', 'evento']]

df_final.to_csv('nino34_classificado.csv', index=False)

print(df_final.head(10))
