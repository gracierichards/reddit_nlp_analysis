import nltk
from nltk.tokenize import RegexpTokenizer, sent_tokenize
from scipy.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt
import sys

def num_sentences(text):
   sentences = sent_tokenize(text)
   sentences = [s for s in sentences if s.strip() != "."]
   sentences2 = []
   for sentence in sentences:
      has_alnum = False
      for char in sentence:
         if char.isalnum():
            has_alnum = True
            break
      if has_alnum:
         sentences2.append(sentence)
   return len(sentences2)

docs = []
y = []
num_thrown_out = 0
tokenizer = RegexpTokenizer(r'\w+')
for filename in ["comments_of_top_posts.csv", "comments_flairs.csv"]:
  with open(filename) as comment_csv:
    for line in comment_csv:
        separator = line.rfind(",")
        comment_body = line[0:separator]
        score = int(line[separator + 1:])
        # Remove outliers
        # if score > 300:
        #   num_thrown_out += 1
        #   continue
        tokens = tokenizer.tokenize(comment_body)
        # if len(tokens) > 100:
        #    num_thrown_out += 1
        #    continue
        if num_sentences(comment_body) > 10:
           num_thrown_out += 1
           continue
        if len(tokens) > 425 and "sorry for my punctitions" not in comment_body:
           print("This shitpost has", num_sentences(comment_body), "sentences")
           print("START OF COMMENT OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", comment_body)
        docs.append(comment_body)
        y.append(score)

print(num_thrown_out, "comments thrown out")

#Normalize y
max_y = max(y)
y = np.array(y)
y = y / max_y

comment_num_words = []
comment_num_sentences = []
for comment in docs:
  tokens = tokenizer.tokenize(comment)
  comment_num_words.append(len(tokens))
  comment_num_sentences.append(num_sentences(comment))

# Calculate the Pearson correlation
results = pearsonr(comment_num_words, y, alternative='greater')
print("The Pearson correlation for numbers of words is ", results.statistic)
print("The p-value is", results.pvalue)
results = pearsonr(comment_num_sentences, y, alternative='greater')
print("The Pearson correlation for numbers of sentences is ", results.statistic)
print("The p-value is", results.pvalue)

# Graph words
# fig, ax = plt.subplots()
# ax.hist(comment_num_words)
# ax.set_ylabel('Number of comments with this number of words')
# ax.set_title('Distribution of comment lengths')
# plt.show()

# Graph sentences
fig, ax = plt.subplots()
ax.hist(comment_num_sentences)
ax.set_ylabel('Number of comments with this number of sentences')
ax.set_title('Distribution of comment lengths')
plt.show()