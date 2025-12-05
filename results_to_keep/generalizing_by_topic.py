import praw
import re
import nltk
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import sys
import os
# Import custom module
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from module1 import *

# Results:
# There are twice as many instances of "sunburn" as "jawsum" or "sprout mole"
# There are twice as many instances of "undertale" as "humphrey" or "Maverick"
# There are less instances of "heromari" than "suntan"
# There are about the same number of instances of "polly" and "sprout mole"
# "Adachi" appears 6 times

# All comments will be sorted into one of these 27 categories, or none of the above
primary_topics = ["sunny", "mari", "hero", "kel", "aubrey", "basil", "sweetheart", "humphrey", "omocat", "jawsum", "pluto", "music", "manga", "sunflower", "sunburn", "heromari", "undertale", "persona", "earthbound", "deltarune", "ddlc", "mewo", "spaceboy", "stranger", "sprout", "maverick", "boen"]

reddit = praw.Reddit(
    client_id="6MSiXboPbWTdqm72ErnWpQ",
    client_secret="lswiD1a6bjaHLq-a_22lzhJvEOfOjQ",
    user_agent="App 1 by busyhope",
)

sub = reddit.subreddit("OMORI")

def determine_topic(text, parent_topic=None):
  primary_presence = [0] * len(primary_topics)
  for i in range(len(primary_topics)):
    if primary_topics[i] == "boen":
      # Regex searches if the comment solely consists of "close"
      primary_presence[i] = text.count("bo en") + len(re.findall('^close$', text)) + text.count("your eyes") + text.count("my time") + len(re.findall('o+y+a+s+u+m+i+', text)) + text.count("o ya su mi")
      if len(re.findall('o+y+a+s+u+m+i+', text)) >= 1:
        print(re.findall('o+y+a+s+u+m+i+', text))
    elif primary_topics[i] == "sprout":
      primary_presence[i] = text.count("sprout mole") + text.count("sproutmole")
    elif primary_topics[i] == "spaceboy":
      primary_presence[i] = text.count("spaceboy") + text.count("space boy") + text.count("space ex-husband")
    elif primary_topics[i] == "persona":
      primary_presence[i] = len(re.findall(r'persona\b', text)) + len(re.findall(r'\badachi\b', text))
    elif primary_topics[i] == "hero":
      primary_presence[i] = len(re.findall(r'\bhero\b', text))
    elif primary_topics[i] == "mari":
      primary_presence[i] = len(re.findall(r'\bmari\b', text))
    else:
      primary_presence[i] = text.count(primary_topics[i])
    if primary_topics[i] == "sunny":
      primary_presence[i] += text.count("snuuy")
    elif primary_topics[i] == "aubrey":
      primary_presence[i] += text.count("auby")
    elif primary_topics[i] == "basil":
      primary_presence[i] += text.count("bagel")
    elif primary_topics[i] == "jawsum":
      primary_presence[i] += text.count("jawsom") + text.count("jawsome")
    elif primary_topics[i] == "music":
      primary_presence[i] += text.count("song")
    elif primary_topics[i] == "maverick":
      primary_presence[i] += text.count("mikhael") + text.count("mikael") + text.count("mikeal") + text.count("mikhail")
    elif primary_topics[i] == "ddlc":
      primary_presence[i] += text.count("doki doki")
  # if sum(primary_presence) == 0:
  #   secondary_presence = [0] * len(secondary_topics)
  #   for i in range(len(secondary_topics)):
  #     secondary_presence[i] = text.count(secondary_topics[i])
  #   if sum(secondary_presence) == 0:
  #     return None
  #   first_greatest = 0
  #   first_greatest_i = -1
  #   second_greatest = 0
  #   for i in len(secondary_presence):
  #     if secondary_presence[i] > first_greatest:
  #       first_greatest = secondary_presence[i]
  #       first_greatest_i = i
  #     elif secondary_presence[i] > second_greatest:
  #       second_greatest = secondary_presence[i]
  #   if first_greatest > 2 * second_greatest:
  #     return secondary_topics[first_greatest_i]
  #   else:
  #     return None
  if sum(primary_presence) == 0:
    return parent_topic
  else:
    first_greatest = 0
    first_greatest_i = -1
    second_greatest = 0
    second_greatest_i = -1
    for i in range(len(primary_presence)):
      if primary_presence[i] > first_greatest:
        first_greatest = primary_presence[i]
        first_greatest_i = i
      elif primary_presence[i] > second_greatest:
        second_greatest = primary_presence[i]
        second_greatest_i = i
    if first_greatest > second_greatest:
      return primary_topics[first_greatest_i]
    else:
      if primary_topics[first_greatest_i] == parent_topic:
        return parent_topic
      if primary_topics[second_greatest_i] == parent_topic:
        return parent_topic
      return None

def determine_post_topic(title, body):
  return determine_topic(title.lower() + " " + body.lower())

def determine_comment_topic(comment, parent_topic):
  return determine_topic(comment.lower(), parent_topic)

"""Assumes the input is a valid, non-empty comment"""
def explore_comment(comment, parent_topic):
  if is_bot(comment.body) or "yes you did" in comment.body.lower() or comment.body.count("i hate basil") > 70:
    if comment.body.count("i hate basil") > 70:
      print("I found Basil!")
    for reply in comment.replies._comments:
      explore_comment(reply, parent_topic)
  else:
    comment_body = remove_links(comment.body)
    comment_topic = determine_comment_topic(comment_body, parent_topic)
    if comment_topic:
      txts[comment_topic].write(comment_body + "\n")
    for reply in comment.replies._comments:
      explore_comment(reply, comment_topic)

def top_of_all_time():
  for post in sub.top(limit=None):
    posts_seen.add(post.id)
    list_of_posts.write(post.id + "\n")
    post.comments.replace_more(limit=None)
    post_topic = determine_post_topic(post.title, post.selftext)
    for comment in post.comments:
      explore_comment(comment, post_topic)

def search_flair(flair):
  # list_of_posts = open("sorted_txts/posts_seen.txt", "a")
  for post in sub.search("flair:" + flair, sort="top"):
    if post.id in posts_seen:
     continue
    else:
     posts_seen.add(post.id)
     list_of_posts.write(post.id + "\n")
    post.comments.replace_more(limit=None)
    post_topic = determine_post_topic(post.title, post.selftext)
    for comment in post.comments:
      explore_comment(comment, post_topic)

list_of_posts = open("sorted_txts/posts_seen.txt", "w")
posts_seen = set()
txts = {}
for topic in primary_topics:
  txts[topic] = open("sorted_txts/" + topic + ".txt", "w")
top_of_all_time()
print(len(posts_seen), "posts were collected.")

# Continuing from before
# for topic in primary_topics:
#   txts[topic] = open("sorted_txts/" + topic + ".txt", "a")
# posts_seen = set()
# with open("sorted_txts/posts_seen.txt", "r") as list_of_posts:
#   line = list_of_posts.readline()
#   while line != "":
#     posts_seen.add(line.strip())
#     line = list_of_posts.readline()

for flair in flairs:
  print(flair)
  search_flair(flair)
print(len(posts_seen), "posts were collected.")

txts = {}
for topic in primary_topics:
  txts[topic] = open("sorted_txts/" + topic + ".txt", "r")
cfd = nltk.ConditionalFreqDist((topic0, word)
                               for topic0 in primary_topics
                               for word in basic_tokenizer(txts[topic0].read()))

for topic in primary_topics:
  print("---" + topic + "---")
  top_words = cfd[topic].most_common(1)
  for word, frequency in top_words:
      print(f"  {word}: {frequency}")