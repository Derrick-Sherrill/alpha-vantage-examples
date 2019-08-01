import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = 'RNZPXZ6Q9FEFMEHM'

ti = TechIndicators(key=api_key, output_format='pandas')
data, meta_data = ti.get_stoch(symbol='MSFT', interval='1min')

data.plot()
plt.title('Stochastic Oscillator')
plt.show()