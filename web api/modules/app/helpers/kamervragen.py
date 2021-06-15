import requests
import urllib.request
import time
import datetime
from bs4 import BeautifulSoup
import ssl
import os, errno
ssl._create_default_https_context = ssl._create_unverified_context

default_url = 'https://www.tweedekamer.nl/'
default_path = 'kamerstukken/kamervragen'
default_query = '?qry=Infrastructuur+en+Waterstaat&fld_tk_categorie=kamerstukken&srt=date%3Adesc%3Adate&fld_prl_kamerstuk=Kamervragen&dpp=25&clusterName=Kamerstukken&sta=1&fld_prl_soort=Antwoord+schriftelijke+vragen'

def download_file(fileUrl, fileName):
    try:
        directory = '../../data/downloads/'
        if not os.path.exists(directory):
            os.makedirs(directory)

        baseUrl = default_url
        downloadUrl = baseUrl + fileUrl
        fileName = directory + fileName
        urllib.request.urlretrieve(downloadUrl, fileName)
        return fileName
    except Exception as e:
        print(e)


def scrap_link(url, query, mongo, _id):
    if(url == "" ):
        url = default_url + default_path
    if(query == ""):
        query = default_query

    downloads = []

    response = requests.get(url + query)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all('article', class_= "card ___icon-right")

    for link in links:
        #find all titles
        card_content = link.find('div', class_="card__content ___small-horizontal-padding")
        title = card_content.find('p').text
        # webLink = card_content.find('p').previous_sibling
        #file code
        code_nummer = link.find('div', class_="flexer ___space-between")
        code_nummer_content = card_content.find('a', class_="code-nummer")
        codeNumber = code_nummer_content.text

        #author
        author_div = code_nummer.find_next_sibling('div')
        author_name = author_div.find('strong').text + " " + author_div.find('strong').next_sibling
        author_ministry = author_div.find('div').text
        # ministry: Infrastructuur en Waterstaat 

        #find all href
        file_link = link.find('a', class_="document__button")
        file_url = file_link['href']

        #download the file
        fileType = file_url.rsplit(".",1)[1]
        file_name = codeNumber + '.' + fileType
        storage_file_path = download_file(file_url, file_name)

        #prepare json
        data = {
            "downloadId": _id,
            "title": title, 
            "fileName": file_name, 
            "authorName": author_name, 
            "ministry": author_ministry, 
            "fileUrl": file_url,
            "storageFilePath": storage_file_path,
            "insertDate": datetime.datetime.now()
            }

        mongo.db.downloads.insert_one(data)
        downloads.append(data)
        time.sleep(1)
    return downloads
