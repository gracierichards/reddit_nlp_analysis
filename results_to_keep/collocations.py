import nltk
from nltk.collocations import *
from nltk.stem import SnowballStemmer
import sys

stemmer = SnowballStemmer("english")
bigram_measures = nltk.collocations.BigramAssocMeasures()
def my_tokenizer(str):
  for punc in '.,?!^<>():;/"“”*\\[]':
    str = str.replace(punc, " ")
  words = str.lower().split()
    
  tokens = []
  for word in words:
    stemmed = stemmer.stem(word)
    if stemmed == "sunni":
      stemmed = "sunny"
    if stemmed == "aubi":
      stemmed = "auby"
    tokens.append(stemmed)
  return tokens

tokens = []
with open("comments_of_top_posts.csv", "r") as file1:
  for line in file1:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    tokens.extend(my_tokenizer(comment_body))
with open("comments_flairs.csv", "r") as file2:
  for line in file2:
    if "HOOKA CHAKA" in line:
      continue
    if "お 休 み" in line:
      continue
    if "Boris Yeltsin" in line:
      continue
    separator = line.rfind(",")
    comment_body = line[0:separator]
    tokens.extend(my_tokenizer(comment_body))
finder = BigramCollocationFinder.from_words(tokens)
finder.apply_freq_filter(3)
print(finder.nbest(bigram_measures.pmi, 10))