import spacy
import pandas as pd
from spacy import displacy

def named_entities(text):

	# Load Dutch tokenizer, tagger, parser, NER and word vectors
	nlp = spacy.load('nl_core_news_sm')

	# Process whole documents or single questions
	doc = nlp(text)

	# Display the POS-visualization of the phrase
	# displacy.serve(doc, style='dep')
	
	entity_list = []

	# List of important POS-tokens from phrase
	important_tokens = ['nsubj', 'nmod']
	token_list = []

	# Find named entities, phrases and concepts
	for entity in doc.ents:
		entity_list.append(entity.text)
		# print(entity.text, entity.label_)

	for token in doc:
		if token.dep_ in important_tokens:
		 token_list.append(token)
		
	# print(entity_list)
	return [entity_list, token_list]
