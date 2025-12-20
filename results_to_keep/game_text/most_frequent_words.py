from nltk.book import *
import sys
import os
# Import custom module
sys.path.append("/Users/gracierichards/reddit")
from module1 import *

tokens = []
with open("results_to_keep/game_text/ao3_text.txt", "r") as file1:
  for line in file1:
    tokens.extend(basic_tokenizer(line))
dist = FreqDist(tokens)
print("Most common words in ao3 dataset:", dist.most_common(100))

tokens = []
with open("results_to_keep/game_text/ao3_text_spicy.txt", "r") as file1:
  for line in file1:
    tokens.extend(basic_tokenizer(line))
dist = FreqDist(tokens)
print("Most common words in spicy ao3 dataset:", dist.most_common(100))

# ao3_tokens = []
# for i in range(1, 21):
#   if i == 6:
#     continue
#   with open("results_to_keep/game_text/ao3_files/" + str(i) + ".txt", "r") as file4:
#     for line in file4:
#       ao3_tokens.extend(basic_tokenizer(line))
# dist = FreqDist(ao3_tokens)
# print("Most common words in ao3 dataset:", dist.most_common(100))

# ao3_spicy_tokens = []
# for i in range(1, 11):
#   if i == 8:
#     continue
#   with open("results_to_keep/game_text/ao3_spicy_files/" + str(i) + ".txt", "r") as file5:
#     for line in file5:
#       ao3_spicy_tokens.extend(basic_tokenizer(line))
# dist = FreqDist(ao3_spicy_tokens)
# print("Most common words in spicy ao3 dataset:", dist.most_common(100))