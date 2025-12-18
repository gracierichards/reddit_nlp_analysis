from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.book import *
import sys
import heapq

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

reddit_tokens = []
with open("comments_of_top_posts.csv", "r") as file1:
  for line in file1:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    reddit_tokens.extend(my_tokenizer(comment_body))
with open("comments_flairs.csv", "r") as file2:
  for line in file2:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    reddit_tokens.extend(my_tokenizer(comment_body))

reddit_dist = FreqDist(reddit_tokens)

game_tokens = []
with open("results_to_keep/game_text/OMORI_game_text.txt", "r") as file3:
  for line in file3:
    game_tokens.extend(my_tokenizer(line))
game_dist = FreqDist(game_tokens)

reddit_n = reddit_dist.N()
game_n = game_dist.N()
percent_greater = {}
percent_less = {}
unique_to_reddit = {}
for item in reddit_dist.items():
  word_frequency = item[1] / reddit_n
  word = item[0]
  if word in game_dist:
    word_frequency2 = game_dist[word] / game_n
    if word_frequency2 > word_frequency:
      percent_greater[word] = (word_frequency2 - word_frequency) / word_frequency
    else:
      percent_less[word] = (word_frequency - word_frequency2) / word_frequency
  else:
    unique_to_reddit[word] = item[1]

unique_to_game = {}
for item in game_dist.items():
  if item[0] not in reddit_dist:
    unique_to_game[item[0]] = item[1]

# print("Words unique to Reddit:", heapq.nlargest(20, unique_to_reddit.items(), key=lambda x : x[1]))
# print("Words unique to the game:", heapq.nlargest(20, unique_to_game.items(), key=lambda x : x[1]))

print("Words more common in the game:", heapq.nlargest(20, percent_greater.items(), key=lambda x : x[1]))
print("Words more common on Reddit:", heapq.nlargest(20, percent_less.items(), key=lambda x : x[1]))