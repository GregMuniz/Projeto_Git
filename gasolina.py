import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura dos dados
df = pd.read_csv('gasolina.csv')

# Plotagem do gráfico de linha
plt.figure(figsize=(12, 6))
sns.lineplot(x='dia', y='preco', data=df)
plt.title('Preço da Gasolina ao Longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Salvando o gráfico em gasolina.png
plt.savefig('gasolina.png')
