#!/usr/bin/python3.9
import pdfToText
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
from nltk.chunk import ne_chunk
nltk.download('maxent_ne_chunker')
nltk.download('words')

#ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobi	le phone market and ordered the company to alter its practices'

ex = pdfToText.text
neMap = {}

#print(ex)
#list of tuples with associated part-of-speech

def preprocess(sent):
	sent = nltk.word_tokenize(sent)
	sent = nltk.pos_tag(sent)
	return sent
	
sent = preprocess(ex)

#print (sent)

# create a chunk parser
pattern = 'NP: {<DT>?<JJ>*<NN>}'

cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
#print(cs)

#insert IOB tags
iob_tagged = tree2conlltags(cs)
#pprint(iob_tagged)

#recognize named entities using classifier
ne_tree = ne_chunk(pos_tag(word_tokenize(ex)))
#print(ne_tree)

#ne_tree_leaves = ne_tree.leaves()

for chunk in ne_tree:
  if hasattr(chunk, 'label'):
    label = chunk.label()
    value = ' '.join(c[0] for c in chunk)

    if label not in neMap:
      s = set()
      s.add(value)
      neMap[label] = s
    else :
      neMap[label].add(value)


#print(neMap)


