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

sub = reddit.subreddit("Helldivers")

# for post in sub.top(limit=5):
#   post.comments.replace_more()
#   all_comments = post.comments.list()
#   for comment in all_comments:
#     print(comment.score)

def top_of_all_time():
  comments_csv = open("helldivers/comments_of_top_posts.csv", "w")
  i = 1
  for post in sub.top(limit=100):
    print(i, ":", post.id, "has", post.num_comments, "comments.")
    # posts_seen.add(post.id)
    # list_of_posts.write(post.id + "\n")
    post.comments.replace_more()
    all_comments = post.comments.list()
    for comment in all_comments:
      if is_bot(comment.body):
        continue
      comment_body = remove_links(comment.body)
      comments_csv.write(comment_body + "," + str(comment.score) + "\n")
    i += 1
    # if i >= 10:
    #   break

# def search_flair(flair, csv):
#   # Continuing where it leaves off
#   # list_of_posts = open("posts_seen.txt", "a")

#   for post in sub.search("flair:" + flair, sort="top"):
#     if post.id in posts_seen:
#      continue
#     else:
#      posts_seen.add(post.id)
#      list_of_posts.write(post.id + "\n")
#     post.comments.replace_more(limit=None)
#     all_comments = post.comments.list()
#     for comment in all_comments:
#       if is_bot(comment.body):
#         continue
#       comment_body = remove_links(comment.body)
#       csv.write(comment_body + "," + str(comment.score) + "\n")

# list_of_posts = open("helldivers/posts_seen.txt", "w")
# posts_seen = set()
top_of_all_time()
# comments_csv = open("helldivers/comments_flairs.csv", "w")
# for flair in ["DISCUSSION", "MEDIA", "FEEDBACK/SUGGESTION", "FAN CREATION", "QUESTION", "TIPS/TACTICS", "HUMOR", "TECHNICAL ISSUE", "LORE", "HELLDIVERS (2015)", "HELLDRIP", "HellBrag"]:
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

# comments_csv = open("comments_flairs.csv", "a")
# for flair in ["Other"]:
#   print(flair)
#   search_flair(flair)
# print(len(posts_seen), "posts were collected.")