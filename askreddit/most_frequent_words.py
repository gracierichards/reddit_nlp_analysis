from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.book import *
import sys
import os
# Import custom module
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from module1 import *

tokens = []
with open("askreddit/titles_of_hot_posts.csv", "r") as file1:
  for line in file1:
    separator = line.rfind(",")
    title = line[0:separator]
    tokens.extend(basic_tokenizer(title))
    if "ai" in basic_tokenizer(title):
      print(title)

dist = FreqDist(tokens)
i = 1
for tuple in dist.most_common(100):
  print(str(i) + ". " + str(tuple))
  i += 1