from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from matplotlib import pyplot as plt
import sys
import math
import heapq
import os
# Import custom module
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from module1 import *

docs = []
y = []
num_thrown_out = 0
with open("askreddit/titles_of_hot_posts.csv") as csv:
  for line in csv:
      separator = line.rfind(",")
      title = line[0:separator]
      score = int(line[separator + 1:])
      # Remove outliers
      if score > 40:
        num_thrown_out += 1
        continue
      docs.append(title)
      y.append(score)

print(num_thrown_out, "comments thrown out")

# Plot upvote amounts
fig, ax = plt.subplots()
ax.hist(y)
ax.set_ylabel('Number of posts with this number of upvotes')
ax.set_title('Distribution of post scores')
plt.show()

#Normalize y
max_y = max(y)
y = np.array(y)
y = y / max_y

vec = CountVectorizer(min_df=2, tokenizer=basic_tokenizer, binary=True)
X = vec.fit_transform(docs)
#print(vec.get_feature_names_out()[62])
#sys.exit()

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
  #print(str(i) + "\t" + vec.get_feature_names_out()[i] + "\t" + str(sum(column.data)))
  pearson = (n * dot - sum(column.data) * sum(y))/math.sqrt((n * sumx2 - (sum(column.data)**2)) * (n * sumy2 - (sum(y) ** 2)))
  correlations.append((vec.get_feature_names_out()[i], pearson))

# Get the top ten correlations
print(heapq.nlargest(10, correlations, key=lambda x : x[1]))

print(heapq.nsmallest(10, correlations, key=lambda x : x[1]))