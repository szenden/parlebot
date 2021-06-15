from requests import get
from bs4 import BeautifulSoup as bs

def extract_articles(query):
    """
    Scrapes the NOS website for news articles. Returns dict of first page news
    results containing title, date, tagline, url and text content.

    Keyword arguments:
    query -- string that will be added to the search url
    """

    # set global variables
    article_results = []
    base_url = 'https://nos.nl'
    search_url = 'https://nos.nl/zoeken/?q='
    
    # request search results page with a query
    soup = bs(get(search_url + query).content, 'lxml')

    # find firstpage articles
    results = soup.find_all('a', {'search-results__link'}, href=True)
    for article in results:

        # extract article data of firstpage results
        article_title = article.find('h3', {'search-results__title'}).text
        article_date = article.find('time', {'search-results__time'})['datetime'][:10]
        article_tagline = article.find('div', {'search-results__description'}).text
        article_url = base_url + article['href']
    
        # extract article text
        article_text = ''
        article_page = bs(get(article_url).content, 'lxml')
        article_content = article_page.find_all('div', {'article_textwrap'})
        for block in article_content:
            article_text = article_text + block.text

        # return dict of results
        article_dict = {'title':article_title,
                        'date':article_date,
                        'tagline':article_tagline,
                        'text':article_text,
                        'url':article_url}

        # add article to article results list
        article_results.append(article_dict)

    # return dict of first page results for the entered query
    # print(article_results)

    return article_results

# extract_articles('warm onthaal iss astronauten')