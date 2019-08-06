import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = 'RNZPXZ6Q9FEFMEHM'

ts = TimeSeries(key=api_key, output_format='pandas')
data_ts, meta_data_ts = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')

periods = 14

ti = TechnicalIndicators(key=api_key, output_format='pandas')
data_ti, meta_data_ti = ti.get_rsi(symbol='MSFT', interval='1min',
                         time_period=periods, series_type='close')


df1 = data_ti
df2 = data_ts['4. close'].iloc[periods::]

print(df1)
df1.index = df2.index
print(df2)

fig, ax1 = plt.subplots()
ax1.plot(df1, 'b-')
ax2 = ax1.twinx()
ax2.plot(df2, 'r.')
plt.title('RSI vs Close Price')
plt.show()
