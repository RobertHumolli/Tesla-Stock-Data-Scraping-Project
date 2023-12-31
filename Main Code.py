import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import yfinance as yf #This is the main library that is used for the data Scraping

stocks = 'TSLA'
start_date = '2021-11-10'

data = yf.download(stocks, start=start_date)['Close']
x_values = data.index

fig = plt.gcf()

def animate(i):
    plt.cla()
    x = x_values[:i]
    y = data[:i]
    
    if not y.empty:
        plt.plot(x, y, linestyle='-', linewidth=2.0, label='Tesla Stock', color='black')
        plt.xlabel('Date (Year-Month-Day)')
        plt.ylabel('Close Share Price')
        plt.legend(loc="upper left")
        plt.title('Tesla Stock Share Prices')
        
        print(f'{i} || {x[-1]} || {y.iloc[-1]:.2f}')
    else:
        print(f'No data available at frame {i}')

ani = FuncAnimation(fig, animate, frames=range(len(x_values)), interval=10, repeat=False)
plt.tight_layout()
plt.show()
