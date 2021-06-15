import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "data"))

import pandas as pd
from time import time
from code.entities import named_entities
from code.similarity import rank_similarities, doc_vect, build_corpus, print_top_words
from code.articles import extract_articles

def main():
    time_start = time()
    print('Main running...')

    # Read dataframe with test questions
    df = pd.read_csv('data/testq.csv', sep=',', header=0, quotechar="'")
    doc_entities = []
    # doc_tags = []

    questions = []
    # Get the named entities of every question belonging to set
    for index, row in df.iterrows():
        if row['code'] == '2019D00272':
            if row['number'] is not None:
                questions.append(row['question'])
                doc_entities.extend(named_entities(row['question'])[0])
                # doc_tags.append(named_entities(row['question'])[1])

    questions = ['Kent u het bericht Turkije gaat weekendscholen financieren in Nederland?','Is het waar dat het regime van president Erdogan weekendscholen gaat organiseren en financieren in verschillende landen waaronder Nederland? Zo ja, heeft u daar contact over gehad met Turkije?','Is u bekend of er al aanvragen zijn ingediend voor weekendscholen in Nederland die door de Turkse overheid gefinancierd gaan worden? Zo ja, hoeveel zijn dit er en waar worden deze opgericht?','Heeft u kennisgenomen van het feit dat Turks-Nederlandse organisaties twijfels hebben bij de weekendscholen en zich afvragen wie er toezicht houdt op wat er op deze scholen gebeurt? Is het waar dat weekendscholen niet onder toezicht staan van de Inspectie van het Onderwijs en zich niet aan de burgerschapsopdracht hoeven te houden? Zo ja, aan welke wet- en regelge- ving moeten deze scholen wel voldoen en welke mogelijkheden heeft u om misstanden tegen te gaan?','Deelt u de mening dat financiering van onderwijs in Nederland aan jonge kinderen vanuit een onvrij en ondemocratisch land als Turkije risico’s met zich meebrengt voor de integratie en het recht van Nederlanders om zich vrij in de Nederlandse samenleving te kunnen ontwikkelen en mee te doen? Zo ja, hoe gaat u dit risico terugdringen?','Bent u bereid toezicht te houden op weekendscholen die vanuit onvrije en ondemocratische landen als Turkije worden gefinancierd en tijdig in te grijpen als het belang van volwaardige integratie en actief burgerschap in de Nederlandse samenleving wordt aangetast? Zo ja, op welke wijze? Zo nee, waarom niet?']
    query_entities = set(doc_entities)

    query_str = ''
    for word in query_entities:
        query_str = query_str + word + ' '
    
    # TEST TEST TEST TEST
    query_str = 'Turkije gaat weekendscholen financieren in Nederland'

    # get results with query
    article_results = extract_articles(query_str)

    # transform the text from the articles and questions to vectors
    vectors = doc_vect(article_results, questions)
    
    # get ranking of articles most similar to the questions
    rank_similarities(vectors[0], vectors[1], method='hellinger')

    print("Run finished. Done in %0.3fs." % (time() - time_start))
    return
    
if __name__ == "__main__":
    main()