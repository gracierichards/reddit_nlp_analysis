import praw
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
import sys
import math

reddit = praw.Reddit(
    client_id="6MSiXboPbWTdqm72ErnWpQ",
    client_secret="lswiD1a6bjaHLq-a_22lzhJvEOfOjQ",
    user_agent="App 1 by busyhope",
)

sub = reddit.subreddit("OMORI")
for post in sub.search("flair:Art", sort="top"):
  print(post.title)
  sys.exit()