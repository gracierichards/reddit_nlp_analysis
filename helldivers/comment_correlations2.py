from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import numpy as np
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
with open("helldivers/comments_of_top_posts.csv") as comment_csv:
  for line in comment_csv:
      separator = line.rfind(",")
      comment_body = line[0:separator]
      score = int(line[separator + 1:])
      # Remove outliers
      # if score > 300:
      #   num_thrown_out += 1
      #   continue
      docs.append(comment_body)
      y.append(score)

print(num_thrown_out, "comments thrown out")

#Normalize y
max_y = max(y)
y = np.array(y)
y = y / max_y

vec = CountVectorizer(min_df=3, tokenizer=my_tokenizer, binary=True)
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

#fig, ax = plt.subplots()
#ax.bar(vec.get_feature_names_out(), correlations)
#ax.set_ylabel('Correlation')
#ax.set_title('Correlation of each word with upvote counts')
#ax.tick_params(axis='x', labelrotation=90)
#plt.show()

# Get the top ten correlations
print(heapq.nlargest(10, correlations, key=lambda x : x[1]))

print(heapq.nsmallest(10, correlations, key=lambda x : x[1]))

# Get rankings of the characters
correlations.sort(key=lambda x : x[1], reverse=True)
print("Rankings out of", len(correlations), "elements")
printed = 0
i = 1
for tuple in correlations:
  if tuple[0] in ["sunny", "mari", "hero", "kel", "aubrey", "basil", "omor", "auby", "maverick", "sweetheart", "snaley", "mewo", "humphrey", "jawsum", "hellmari", "snuuy", "omocat", "bagel", "stair"]:
    printed += 1
    print(str(i) + "th place:", tuple[0])
    if printed == 19:
      sys.exit()
  i += 1
