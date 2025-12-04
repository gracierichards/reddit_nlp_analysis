import praw
import os
import sys
# Import custom module
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from module1 import *

# longest_comment = ""
# for filename in ["comments_of_top_posts.csv", "comments_flairs.csv"]:
#   i = 0
#   with open(filename) as comment_csv:
#     for line in comment_csv:
#         i += 1
#         separator = line.rfind(",")
#         comment_body = line[0:separator]
#         if len(comment_body) > len(longest_comment):
#            longest_comment = comment_body
#            print(i)
# print(longest_comment)

# Longest post
reddit = praw.Reddit(
    client_id="6MSiXboPbWTdqm72ErnWpQ",
    client_secret="lswiD1a6bjaHLq-a_22lzhJvEOfOjQ",
    user_agent="App 1 by busyhope",
)
sub = reddit.subreddit("OMORI")
longest_title = ""
num_with_longest_title = 0
id_of_longest_post = ""
len_of_longest_post = 0  

for post in sub.top(limit=None):
  if len(post.title) > len(longest_title):
    longest_title = post.title
    num_with_longest_title = 1
  elif len(post.title) == len(longest_title):
    num_with_longest_title += 1
  
  if len(post.selftext) > len_of_longest_post:
    len_of_longest_post = len(post.selftext)
    id_of_longest_post = post.id

for flair in flairs:
  print(flair)
  for post in sub.search("flair:" + flair, sort="top"):
    if len(post.title) > len(longest_title):
      longest_title = post.title
      num_with_longest_title = 1
    elif len(post.title) == len(longest_title):
      num_with_longest_title += 1
    
    if len(post.selftext) > len_of_longest_post:
      len_of_longest_post = len(post.selftext)
      id_of_longest_post = post.id
print("Number of post titles with length", len(longest_title), "=", num_with_longest_title)
print(longest_title)
print("ID of longest post:", id_of_longest_post)