import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

stock = ["MRNA" , "CGC" , "PFE"]
# stock = ["MRNA"]

stocks = yf.download(stock, start = "2010-01-01", end = "2020-11-01")
data = stocks.loc[:, "Close"].copy()
# data = stocks.loc[:,:].copy()


# x = data.info
# print(x)

data.plot(figsize = (17,8), fontsize = 18)
plt.style.use("seaborn")
plt.show()