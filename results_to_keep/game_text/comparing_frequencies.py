from nltk.book import *
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import sys
import heapq
import sys
import os
# Import custom module
sys.path.append("/Users/gracierichards/reddit")
from module1 import *

stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")
def game_tokenizer(str):
  for punc in '.,?!^:;/"“”*[]…➜':
    str = str.replace(punc, " ")
  str = str.replace("’", "'")
  # Remove segments matching the pattern <text>
  str = re.sub(r'<[^>]*>', "", str)
  # Remove instances of VARIABLE(something)
  str = re.sub(r'VARIABLE\(.*?\)', "", str)
  str = str.replace("(", "").replace(")", "")
  words = str.lower().split()
  tokens = []
  for word in words:
    if word.startswith("\\dii"):
      continue
    elif word == "\\i":
      continue
    else:
      word = word.replace("\\", "")
      if not word:
        continue
    if "itemget" in word:
      continue
    stemmed = stemmer.stem(word)
    if stemmed not in stop_words:
      tokens.append(stemmed)
  return tokens

reddit_tokens = []
with open("comments_of_top_posts.csv", "r") as file1:
  for line in file1:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    reddit_tokens.extend(basic_tokenizer(comment_body))
with open("comments_flairs.csv", "r") as file2:
  for line in file2:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    reddit_tokens.extend(basic_tokenizer(comment_body))

reddit_dist = FreqDist(reddit_tokens)

game_tokens = []
with open("results_to_keep/game_text/OMORI_game_text.txt", "r") as file3:
  for line in file3:
    game_tokens.extend(game_tokenizer(line))
game_dist = FreqDist(game_tokens)

ao3_tokens = []
# A list of 20 FreqDists, one for each of the files
ao3_freqdists = []
for i in range(1, 21):
  if i == 6:
    continue
  with open("results_to_keep/game_text/ao3_files/" + str(i) + ".txt", "r") as file4:
    cur_file_tokens = []
    for line in file4:
      ao3_tokens.extend(basic_tokenizer(line))
      cur_file_tokens.extend(basic_tokenizer(line))
    ao3_freqdists.append(FreqDist(cur_file_tokens))
ao3_dist = FreqDist(ao3_tokens)

ao3_spicy_tokens = []
# A list of 10 FreqDists, one for each of the files
ao3_spicy_freqdists = []
for i in range(1, 11):
  with open("results_to_keep/game_text/ao3_spicy_files/" + str(i) + ".txt", "r") as file5:
    cur_file_tokens = []
    for line in file5:
      ao3_spicy_tokens.extend(basic_tokenizer(line))
      cur_file_tokens.extend(basic_tokenizer(line))
    ao3_spicy_freqdists.append(FreqDist(cur_file_tokens))
ao3_spicy_dist = FreqDist(ao3_spicy_tokens)

def found_in_single_fic(dist_name, word):
  if dist_name == "ao3" or dist_name == "spicy":
    # Number of different fics the word appears in
    num_fics_in = 0
    if dist_name == "ao3":
      freqdists_list = ao3_freqdists
    if dist_name == "spicy":
      freqdists_list = ao3_spicy_freqdists
    for dist in freqdists_list:
      # Word must appear 4 times for it to count
      if dist[word] > 3:
        num_fics_in += 1
    if num_fics_in < 2:
      return True
  return False

def compare_datasets(dist_name1, dist_name2):
  dists = {"reddit":reddit_dist, "game":game_dist, "ao3":ao3_dist, "spicy":ao3_spicy_dist}
  if dist_name1 not in dists or dist_name2 not in dists:
    print("Invalid dist name provided to find_unique_words.")
    return
  dist1 = dists[dist_name1]
  dist2 = dists[dist_name2]
  n1 = dist1.N()
  n2 = dist2.N()
  # Contains words found more often in dist2
  percent_greater = {}
  # Contains words found less often in dist2
  percent_less = {}
  for item in dist1.items():
    word_frequency = item[1] / n1
    word = item[0]
    if word in dist2:
      word_frequency2 = dist2[word] / n2
      if word_frequency2 > word_frequency:
        if not found_in_single_fic(dist_name2, word):
          percent_greater[word] = (word_frequency2 - word_frequency) / word_frequency
      else:
        if not found_in_single_fic(dist_name1, word):
          percent_less[word] = (word_frequency - word_frequency2) / word_frequency
    # If a word in not in the distribution is handled below

  print("Words more common in dataset 1:", heapq.nlargest(20, percent_less.items(), key=lambda x : x[1]))
  print("Words more common in dataset 2:", heapq.nlargest(20, percent_greater.items(), key=lambda x : x[1]))


# Finds the words that are only found in the given dataset and not the other 3 datasets
def find_unique_words(dist_name):
  dists = {"reddit":reddit_dist, "game":game_dist, "ao3":ao3_dist, "spicy":ao3_spicy_dist}
  if dist_name not in dists:
    print("Invalid dist name provided to find_unique_words.")
    return
  ref_dist = dists[dist_name]
  del dists[dist_name]
  unique_words = {}
  for item in ref_dist.items():
    word = item[0]
    found = False
    for dist in dists.values():
      if word in dist:
        found = True
    if not found:
      if not found_in_single_fic(dist_name, word):
        unique_words[word] = item[1]

  print("Words unique to dataset", dist_name, "are:", heapq.nlargest(20, unique_words.items(), key=lambda x : x[1]))


find_unique_words("reddit")
find_unique_words("game")
find_unique_words("ao3")
find_unique_words("spicy")

print("\nDataset 1 is", "Reddit", "- Dataset 2 is", "Game Text")
compare_datasets("reddit", "game")

print("\nDataset 1 is", "Reddit", "- Dataset 2 is", "AO3")
compare_datasets("reddit", "ao3")

print("\nDataset 1 is", "Reddit", "- Dataset 2 is", "Spicy AO3")
compare_datasets("reddit", "spicy")

print("\nDataset 1 is", "Game", "- Dataset 2 is", "AO3")
compare_datasets("game", "ao3")

print("\nDataset 1 is", "AO3", "- Dataset 2 is", "Spicy AO3")
compare_datasets("ao3", "spicy")