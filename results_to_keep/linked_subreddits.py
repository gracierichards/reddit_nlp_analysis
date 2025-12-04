import sys

def my_tokenizer(str):
  # Everything except for forward slash
  for punc in '.,?!^<>():;"“”*\\[]…➜':
    str = str.replace(punc, "")
    return str.lower().split()
  
counts = {}
with open("comments_of_top_posts.csv", "r") as file1:
  for line in file1:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    for token in my_tokenizer(comment_body):
      if token.startswith("r/"):
        if token in counts:
          counts[token] += 1
        else:
          counts[token] = 1
with open("comments_flairs.csv", "r") as file2:
  for line in file2:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    for token in my_tokenizer(comment_body):
      if token.startswith("r/"):
        if token in counts:
          counts[token] += 1
        else:
          counts[token] = 1
for pair in sorted(counts.items(), key=lambda x: x[1], reverse=True):
  print(pair[0] + "\t" + str(pair[1]) + "\n")