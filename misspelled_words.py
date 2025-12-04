from nltk.book import FreqDist
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
def basic_tokenizer(str):
  for punc in '.,?!^<>():;/"“”*\\[]…➜':
    str = str.replace(punc, "")
  str = str.replace("’", "'")
  words = str.lower().split()
  tokens = []
  for word in words:
    if word not in stop_words:
      tokens.append(word)
  return tokens

tokens = []
with open("comments_of_top_posts.csv", "r") as file1:
  for line in file1:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    tokens.extend(basic_tokenizer(comment_body))
with open("comments_flairs.csv", "r") as file2:
  for line in file2:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    tokens.extend(basic_tokenizer(comment_body))

dist = FreqDist(tokens)
english_vocab = set(w.lower() for w in nltk.corpus.words.words())
for word, count in dist.most_common(100):
  if word not in english_vocab:
    print(word, count)