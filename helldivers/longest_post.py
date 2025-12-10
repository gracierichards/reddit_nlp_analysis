import praw
import os
import sys
# Import custom module
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from module1 import *

longest_comment = ""
for filename in ["helldivers/comments_of_top_posts.csv"]:
  i = 0
  with open(filename) as comment_csv:
    for line in comment_csv:
        i += 1
        separator = line.rfind(",")
        comment_body = line[0:separator]
        if len(comment_body) > len(longest_comment):
           longest_comment = comment_body
           print(i)
print(longest_comment)

# # Longest post
# reddit = praw.Reddit("app1")
# sub = reddit.subreddit("Helldivers")
# longest_title = ""
# longest_title2 = ""
# num_with_longest_title = 0
# id_of_longest_title = ""
# id_of_longest_title2 = ""
# id_of_longest_post = ""
# len_of_longest_post = 0  

# num_posts = 0
# for post in sub.top(limit=None):
#   num_posts += 1
#   if len(post.title) > len(longest_title):
#     longest_title = post.title
#     num_with_longest_title = 1
#     id_of_longest_title = post.id
#   elif len(post.title) == len(longest_title):
#     num_with_longest_title += 1
#     longest_title2 = post.title
#     id_of_longest_title2 = post.id
  
#   if len(post.selftext) > len_of_longest_post:
#     len_of_longest_post = len(post.selftext)
#     id_of_longest_post = post.id

# for flair in ["DISCUSSION", "MEDIA", "FEEDBACK/SUGGESTION", "FAN CREATION", "QUESTION", "TIPS/TACTICS", "HUMOR", "TECHNICAL ISSUE", "LORE", "HELLDIVERS (2015)", "HELLDRIP", "HellBrag"]:
#   print(flair)
#   for post in sub.search("flair:" + flair, sort="top"):
#     num_posts += 1
#     if len(post.title) > len(longest_title):
#       longest_title = post.title
#       num_with_longest_title = 1
#       id_of_longest_title = post.id
#     elif len(post.title) == len(longest_title):
#       num_with_longest_title += 1
#       longest_title2 = post.title
#       id_of_longest_title2 = post.id
    
#     if len(post.selftext) > len_of_longest_post:
#       len_of_longest_post = len(post.selftext)
#       id_of_longest_post = post.id

# print("Number of posts encountered:", num_posts)
# print("Number of post titles with length", len(longest_title), "=", num_with_longest_title)
# print("ID:", id_of_longest_title, "with title:", longest_title)
# print("Tied is ID:", id_of_longest_title2, "with title:", longest_title2)
# print("ID of longest post:", id_of_longest_post)