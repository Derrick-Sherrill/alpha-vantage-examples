# alpha-vantage-examples
Alpha Vantage Examples and Scripts that I will use in YouTube videos. Feel free to check them out.

My YouTube to see the videos:
https://www.youtube.com/channel/UCJHs6RO1CSM85e8jIMmCySw

I left an API key in all these scripts so they would run out of the box. You'll need to get your own API key which can be found here: 
https://www.alphavantage.co/support/#api-key


## 1. Time Series Intraday 
(Script provided by Alpha Vantage https://www.alphavantage.co/documentation/ )

Returns data on the intraday timeseries of a stock specified by the symbol keyword arguement in the ts.get_intraday method.

![Time Series png found in Example-Images](Example-Images/Timeseries-Example.png)

Multiple output formats, pandas was selected in this script 
https://github.com/Derrick-Sherrill/alpha-vantage-examples/blob/master/timeseries_example.py

Close prices of each minute plotted with matplotlib

## Simple Moving Average VS. Intraday Time Series

Combination of the technical indicators and time series API calls. Plotted against each other here:

![Simple Moving Average Example](Example-Images/SMA-vs-Timeseries.png)

Simple moving average here being calculated by last 60 minutes. Adjust for own purposes. 

https://github.com/Derrick-Sherrill/alpha-vantage-examples/blob/master/sma_vs_close.py
