import praw
import re
import sys
import os
# Import custom module
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from module1 import *

reddit = praw.Reddit("app1")

sub = reddit.subreddit("AskReddit")

def hot():
  csv = open("askreddit/titles_of_hot_posts.csv", "w")
  first = True
  for post in sub.hot(limit=None):
    if first:
      print("The top post has", post.num_comments, "comments.")
      first = False
    if " AI " in post.title or " ai " in post.title or "Ai" in post.title or "A.I." in post.title:
      print("1.", post.id)
      print("2.", post.author)
      print("Comments:", post.num_comments)
    csv.write(post.title + "," + str(post.ups) + "\n")

hot()