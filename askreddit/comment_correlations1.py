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
  comments_csv = open("askreddit/comments_of_hot_posts.csv", "w")
  for post in sub.hot(limit=10):
    # posts_seen.add(post.id)
    list_of_posts.write(post.id + "\n")
    post.comments.replace_more(limit=None)
    all_comments = post.comments.list()
    for comment in all_comments:
      # if comment.body == "Close":
      #   print("1.", post.id)
      #   print("2.", comment.id)
      #   print("3.", comment.author)
      #   print("4.", comment.body)
      #   sys.exit()
      if is_bot(comment.body):
        continue
      # print(comment.id)
      # print(comment.replies._comments)
      # if comment.id == "gijivt3":
      #   print(comment.replies._comments)
      #   sys.exit()
      comment_body = remove_links(comment.body)
      comments_csv.write(comment_body + "," + str(comment.score) + "\n")

list_of_posts = open("askreddit/posts_seen.txt", "w")
# posts_seen = set()
hot()
# comments_csv = open("comments_flairs.csv", "w")
# for flair in flairs:
#   print(flair)
#   search_flair(flair)
# print(len(posts_seen), "posts were collected.")

# Continuing where it leaves off
# posts_seen = set()
# with open("posts_seen.txt", "r") as list_of_posts:
#   line = list_of_posts.readline()
#   while line != "":
#     posts_seen.add(line.strip())
#     line = list_of_posts.readline()

#comments_csv = open("comments_flairs.csv", "a")
# for flair in ["Other"]:
#   print(flair)
#   search_flair(flair)
#print(len(posts_seen), "posts were collected.")