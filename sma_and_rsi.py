import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = 'RNZPXZ6Q9FEFMEHM'

periods = 60

ti = TechIndicators(key=api_key, output_format='pandas')
data_rsi, meta_data_rsi = ti.get_rsi(symbol='MSFT', interval='1min',
                         time_period=periods, series_type='close')

ti = TechIndicators(key=api_key, output_format='pandas')
data_sma, meta_data_sma = ti.get_sma(symbol='MSFT', interval='1min',
                         time_period=periods, series_type='close')


df1 = data_sma.iloc[1::]
df2 = data_rsi

print(df1)
df1.index = df2.index
print(df2)

fig, ax1 = plt.subplots()
ax1.plot(df1, 'b-')
ax2 = ax1.twinx()
ax2.plot(df2, 'r.')
plt.title('SMA (In blue) vs RSI (Red)')
plt.show()
