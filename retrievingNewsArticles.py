from GoogleNews import GoogleNews

# Initialising the google search
googlenews = GoogleNews()
googlenews.enableException(True)
googlenews = GoogleNews(lang='en', region='AU')
googlenews = GoogleNews(period='28d')
googlenews = GoogleNews(encode='utf-8')


#defining a search function
def googleSearch(searchParameter):
    googlenews.search(searchParameter + ' financial stock')
    allSearchResults = googlenews.results()

    # These two lines are required for each added page of results obtained
    googlenews.get_page(2)
    allSearchResults += googlenews.results()

    return allSearchResults

print(googleSearch("APPL"))