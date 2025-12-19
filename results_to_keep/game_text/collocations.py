# -*- coding: utf-8 -*-
import nltk
from nltk.collocations import *
import sys
import os
# Import custom module
sys.path.append("/Users/gracierichards/reddit")
from module1 import *

bigram_measures = nltk.collocations.BigramAssocMeasures()

tokens = []
with open("results_to_keep/game_text/ao3_text.txt", "r") as file1:
  for line in file1:
    tokens.extend(basic_tokenizer(line))
finder = BigramCollocationFinder.from_words(tokens)
finder.apply_freq_filter(3)
print("Most associated words in ao3 dataset:", finder.nbest(bigram_measures.pmi, 10))

def isEnglish(s):
  try:
      s.encode(encoding='utf-8').decode('ascii')
  except UnicodeDecodeError:
      return False
  else:
      return True

tokens = []
with open("results_to_keep/game_text/ao3_text_spicy.txt", "r") as file1:
  for line in file1:
    if not isEnglish(line):
       continue
    tokens.extend(basic_tokenizer(line))
finder = BigramCollocationFinder.from_words(tokens)
finder.apply_freq_filter(4)
print("Most associated words in spicy ao3 dataset:", finder.nbest(bigram_measures.pmi, 10))