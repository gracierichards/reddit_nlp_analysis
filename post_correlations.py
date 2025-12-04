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
docs = []
y = []
total = 0
for post in sub.top(limit=None):
  docs.append(post.title + "" + post.selftext)
  y.append(post.ups)
  total += 1
print(total, "posts included")

vec = CountVectorizer()
X = vec.fit_transform(docs)
print(len(vec.get_feature_names_out()))

# Calculate the Pearson correlation
correlations = []
sumy2 = 0
for n in y:
  sumy2 += n**2
for i in range(X.shape[1]):
  column = X.getcol(i)
  sumx2 = (column.data ** 2).sum()
  dot = column.T @ y
  dot = dot.item()
  n = X.shape[0]
  pearson = (n * dot - sum(column.data) * sum(y))/math.sqrt((n * sumx2 - sum(column.data)**2) * (n * sumy2 - sum(y) ** 2))
  correlations.append(pearson)
  if pearson > 0.25:
    print(vec.get_feature_names_out()[i])
    print(X.getcol(i))

fig, ax = plt.subplots()
ax.bar(vec.get_feature_names_out(), correlations)
ax.set_ylabel('Correlation')
ax.set_title('Correlation of each word with upvote counts')
ax.tick_params(axis='x', labelrotation=90)
plt.show()