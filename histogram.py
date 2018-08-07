import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
plot = df.plot.hist(x='match',
                       y='scale',
                       colormap='viridis')

plt.show()
