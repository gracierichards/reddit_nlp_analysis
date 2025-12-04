n = 0
with open("comments_of_top_posts.csv", "r") as file1:
  for line in file1:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    score = int(line[separator + 1:])
    if score > 600:
      n += 1
      print(comment_body)
print("Total comments:", n)