import yfinance as yf


# fast_info dictionary keys: ['currency', 'exchange', 'timezone', 'shares', 'market_cap', 'last_price', 'previous_close', 'open', 'day_high', 'day_low', 
# 'regular_market_previous_close', 'last_volume', 'fifty_day_average', 'two_hundred_day_average', 'ten_day_average_volume', 'three_month_average_volume', 'year_high', 'year_low', 'year_change']



# Gets basic details for a stock
# This function only finds stocks listed on the ASX (exchange = 'ASX')
def retrieve_current_stats(stockCode,exchange):
    if exchange == "ASX":
        stock = yf.Ticker(stockCode + ".AX")
    stockFastInfo = stock.fast_info # This will print a statement if no matching stock can be found
    stockInfo = stock.info
    stockStats={}  # Creating dictionary of core useful stats
    try:
        stockStats['name'] = stockInfo['longName']
        stockStats["code"] = stockCode.upper()
        stockStats["current"] = stockFastInfo["last_price"]
        stockStats["previousClose"] = stockFastInfo["regular_market_previous_close"]
        stockStats["dayChange"] = stockStats["current"]-stockStats["previousClose"]
        stockStats["dayChangeP"] = (100*(stockStats["current"]-stockStats["previousClose"])/stockStats["previousClose"])
        stockStats["50DayAverage"] = stockFastInfo["fifty_day_average"]
        stockStats["200DayAverage"] = stockFastInfo["two_hundred_day_average"]
        stockStats["52weekhigh"] = stockFastInfo['year_high']
        stockStats["52weeklow"] = stockFastInfo['year_low']
        stockStats["marketCap"] = stockFastInfo["market_cap"]
        stockStats["dividendYieldP"] = stockInfo["dividendYield"]
        return stockStats
    except TypeError:  # Accounting for if stock can not be found
        pass


    
# Demonstration of function in a continuous loop
def main():
    while True:
        code = input("\nEnter code of ASX-listed share to retrieve its data or 'q' to quit: ")
        if code == 'q' or code == 'Q':
            break
        print(retrieve_current_stats(code,"ASX"))

main()