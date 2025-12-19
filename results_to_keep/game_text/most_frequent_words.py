from nltk.book import *
import sys
import os
# Import custom module
sys.path.append("/Users/gracierichards/reddit")
from module1 import *

tokens = []
with open("results_to_keep/game_text/aoc_text.txt", "r") as file1:
  for line in file1:
    tokens.extend(basic_tokenizer(line))
dist = FreqDist(tokens)
print("Most common words in aoc dataset:", dist.most_common(100))

tokens = []
with open("results_to_keep/game_text/aoc_text_spicy.txt", "r") as file1:
  for line in file1:
    tokens.extend(basic_tokenizer(line))
dist = FreqDist(tokens)
print("Most common words in spicy aoc dataset:", dist.most_common(100))