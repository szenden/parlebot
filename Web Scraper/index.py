import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

default_url = 'https://www.tweedekamer.nl/'
default_path = 'kamerstukken/kamervragen'
query = 'kamerstukken/kamervragen?qry=Infrastructuur+en+Waterstaat&fld_tk_categorie=kamerstukken&srt=date%3Adesc%3Adate&fld_prl_kamerstuk=Kamervragen&dpp=25&clusterName=Kamerstukken&sta=1&fld_prl_soort=Antwoord+schriftelijke+vragen'
response = requests.get(default_url + default_path + query)

# print(response)

def download_file(fileUrl, fileName):
    try:
        baseUrl = 'https://www.tweedekamer.nl'
        downloadUrl = baseUrl + fileUrl
        fileName = './downloads/' + fileName
        urllib.request.urlretrieve(downloadUrl, fileName)
        time.sleep(1)
    except Exception as e:
        print(e)
        # print('failed to download')

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all('article', class_= "card ___icon-right")

for link in links:
    #find all title
    card_content = link.find('div', class_="card__content ___small-horizontal-padding")
    title = card_content.find('p')
    print(title)
    print('\n')

    #file code
    code_nummer = link.find('div', class_="flexer ___space-between")
    code_nummer_content = card_content.find('a', class_="code-nummer")
    codeNumber = code_nummer_content.text
    print(codeNumber)

    #author
    author_div = code_nummer.find_next_sibling('div')
    author_name = author_div.find('strong').text + " " + author_div.find('strong').next_sibling
    author_ministry = author_div.find('div').text
    print(author_name)
    print(author_ministry)
    # ministry: Infrastructuur en Waterstaat 

    #find all href
    file_link = link.find('a', class_="document__button")
    fileUrl = file_link['href']
    print(fileUrl)

    #download the file
    # fileType = fileUrl.rsplit(".",1)[1]
    # download_file(fileUrl, codeNumber + '.' + fileType)
