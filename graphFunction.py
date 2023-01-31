import yfinance as yf
import matplotlib.pyplot as plt



def retrieve_stock_history(stock, period):
    stock = yf.Ticker(stock)
    stock_history = stock.history(period=period)
    return stock_history

#resolution to be decided
def graph_stock_history(stock_history):
    low_column = stock_history['Low'].values.tolist()
    high_column = stock_history['High'].values.tolist()
    avg_column = [(x+y)/2 for x, y in zip(low_column, high_column)]
    dates = []
    for i in range(len(stock_history.index)):
        dates.append(stock_history.index[i].strftime("%Y-%m-%d %H:%M:%S").split()[0])
    plt.plot(dates, avg_column)
    plt.show()

graph_stock_history(retrieve_stock_history("AAPL", "10d"))





