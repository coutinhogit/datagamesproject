import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vgsales.csv')
print(df.head(10))

df.dropna(inplace=True)
df['Year'] = df['Year'].astype(int)

print("Dados limpos com sucesso! Agora estamos prontos para criar os gráficos.")