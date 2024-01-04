
import pandas as pd
import seaborn as sns

gasolina = pd.read_csv('gasolina.csv')

line_plot = sns.lineplot(data= gasolina, x = 'dia', y = 'venda', color = 'red')
line_plot.set_xlabel('Dia')
line_plot.set_ylabel('Venda')
line_plot.set_title('Preço da Gasolina a Cada Dia')
