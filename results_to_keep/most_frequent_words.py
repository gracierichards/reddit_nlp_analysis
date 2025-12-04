from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.book import *

stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")
def my_tokenizer(str):
  for punc in '.,?!^<>():;/"“”*\\[]…➜':
    str = str.replace(punc, "")
  str = str.replace("’", "'")
  words = str.lower().split()
    
  tokens = []
  for word in words:
    stemmed = stemmer.stem(word)
    if stemmed == "sunni":
      stemmed = "sunny"
    if stemmed == "aubi":
      stemmed = "auby"
    if stemmed == "jawsom" or stemmed == "jawsome":
      stemmed = "jawsum"
    if stemmed not in stop_words:
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
    separator = line.rfind(",")
    comment_body = line[0:separator]
    tokens.extend(my_tokenizer(comment_body))

dist = FreqDist(tokens)
print(dist.most_common(100))