# This method of parsing requires a download of Chromium which is 137MB, and takes a few seconds to initialise, however all values can be quickly accessed after*
# I used this method as the values are only rendered in after the Javascript is loaded on the HTML is loaded, whereas other methods I used before this could not handle waiting for the Javascript to load
# Feel free to find other faster methods that take up less storage space
# I will next try and find how to access the graphs that are displayed
# Just realised I could have used google's inbuilt finance feature but this is more just testing to see the method of HTML parsing works, I will try access graph data later on tonight maybe (29/01/2023) from google's inbuilt feature to see if this method is still the best
# *Based on how I did not notice a difference between finding a single data entry, and finding the 11 entries this code does find


from requests_html import HTMLSession  # Run 'pip install requests-html' in terminal first
session = HTMLSession()



def stockDataAccess():
    while True:
        stockCode = input("Enter code here to view full stock data, or 'q' to quit: ")  #change this code to any stock code to test, first run this code then verify its values with google
        if stockCode == 'Q' or stockCode == 'q':
            break
        page = session.get('https://www.google.com/search?q=' + stockCode + '+stock')
        page.html.render()
        stockData = {}  # Data is transformed into a dictionary
        stockDataHeaders = ['Open','High','Low','Market Cap','P/E Ratio','Div Yield','52-week High','52-week Low']

        #obtaining data that can not be done iterably
        try:
            stockData["Current"] = page.html.xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]/text()')[0]
        except IndexError:
            print("\nStock code could not be found, please try again\n")
            continue
        stockData["Daily Change"] = page.html.xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[2]/span[1]/text()')[0]
        stockData["Daily Change (%)"] = page.html.xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[2]/span[2]/span[1]/text()')[0]

        #For loop is used to get data that comes from the table below the graph, which can be done iterably
        for i in range(8):
            j = i//3 + 1
            k = i%3 + 1
            stockData[stockDataHeaders[i]] = page.html.xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/div/g-card-section[2]/div/div/div[' + str(j) + ']/table/tbody/tr[' + str(k) + ']/td[2]/div/text()')[0]

        try:
            stockName = page.html.xpath('//*[@id="rcnt"]/div[1]/div/div/div[3]/div[1]/div/div[2]/div/div/div/div[1]/span/text()')[0]
        except IndexError:
            stockName = stockCode.upper()

        # printing the entire dictionary (to see results)
        print(f'\n{stockName}\n{stockData}\n')


stockDataAccess()
