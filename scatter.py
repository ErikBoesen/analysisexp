import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
plot = df.plot.scatter(x='match',
                       y='scale',
                       c='allied-switch',
                       colormap='viridis')

plt.show()
