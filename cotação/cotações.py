import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
from IPython.display import display

cotacao_bitcoin = data.DataReader('BTC-USD' , data_source = 'yahoo' , start = '01/01/2020' , end = '11/29/2021')

display(cotacao_bitcoin)

cotacao_bitcoin['Adj Close'].plot()
plt.show()

