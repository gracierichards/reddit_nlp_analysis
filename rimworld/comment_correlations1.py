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

sub = reddit.subreddit("RimWorld")

def top_of_all_time():
  comments_csv = open("rimworld/comments_of_top_posts.csv", "w")
  for post in sub.top(limit=None):
    posts_seen.add(post.id)
    list_of_posts.write(post.id + "\n")
    post.comments.replace_more(limit=None)
    all_comments = post.comments.list()
    for comment in all_comments:
      if is_bot(comment.body):
        continue
      comment_body = remove_links(comment.body)
      comments_csv.write(comment_body + "," + str(comment.score) + "\n")

def search_flair(flair, csv):
  # Continuing where it leaves off
  list_of_posts = open("posts_seen.txt", "a")

  for post in sub.search("flair:" + flair, sort="top"):
    if post.id in posts_seen:
     continue
    else:
     posts_seen.add(post.id)
     list_of_posts.write(post.id + "\n")
    post.comments.replace_more(limit=None)
    all_comments = post.comments.list()
    for comment in all_comments:
      if is_bot(comment.body):
        continue
      comment_body = remove_links(comment.body)
      csv.write(comment_body + "," + str(comment.score) + "\n")

# list_of_posts = open("rimworld/posts_seen.txt", "w")
# posts_seen = set()
# top_of_all_time()
# comments_csv = open("rimworld/comments_flairs.csv", "w")
# for flair in ["'PC Help/Bug (Vanilla)'", "'PC Help/Bug (Mod)'", "Solved!", "Meta", "'Guide (Vanilla)'", "'Guide (Mod)'", "'Mod Release'", "'Mod Showcase'", "Suggestion", "Discussion", "Scenario", "#ColonistLife", "'Colony Showcase'", "Story", "Art", "Comic", "Misc", "'Xbox Help/Bug'", "'PS Help/Bug'", "Explicit", "'Designer Map'"]:
#   print(flair)
#   search_flair(flair, comments_csv)
# print(len(posts_seen), "posts were collected.")

# Continuing where it leaves off
posts_seen = set()
with open("rimworld/posts_seen.txt", "r") as list_of_posts:
  line = list_of_posts.readline()
  while line != "":
    posts_seen.add(line.strip())
    line = list_of_posts.readline()

comments_csv = open("rimworld/comments_flairs.csv", "a")
for flair in ["'PC Help/Bug (Vanilla)'", "'PC Help/Bug (Mod)'", "Solved!", "Meta", "'Guide (Vanilla)'", "'Guide (Mod)'", "'Mod Release'", "'Mod Showcase'", "Suggestion", "Discussion", "Scenario", "#ColonistLife", "'Colony Showcase'", "Story", "Art", "Comic", "Misc", "'Xbox Help/Bug'", "'PS Help/Bug'", "Explicit", "'Designer Map'"]:
  print(flair)
  search_flair(flair, comments_csv)
print(len(posts_seen), "posts were collected.")