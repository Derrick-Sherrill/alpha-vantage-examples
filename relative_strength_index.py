import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = 'RNZPXZ6Q9FEFMEHM'

ti = TechIndicators(key=api_key, output_format='pandas')
data, meta_data = ti.get_rsi(symbol='MSFT', interval='1min', time_period=60, series_type='close')

data.plot()
plt.title('Relative Strength Index')
plt.show()
