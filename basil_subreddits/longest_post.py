import praw
import re

reddit = praw.Reddit(
    client_id="6MSiXboPbWTdqm72ErnWpQ",
    client_secret="lswiD1a6bjaHLq-a_22lzhJvEOfOjQ",
    user_agent="App 1 by busyhope",
)
sub = reddit.subreddit("basil_cult")

def is_bot(comment_text):
  if "Your comment's content violated our spoiler policy" in comment_text:
    return True
  if "Your post's title violated our spoiler policy" in comment_text:
    return True
  if "Your submission has been removed" in comment_text:
    return True
  if "If you or anyone you know are struggling, please, PLEASE reach out for help." in comment_text:
    return True
  if "This bot is created by" in comment_text:
    return True
  if "removal request for savevideo" in comment_text:
    return True
  if "This bot wants to find the best and worst bots on Reddit" in comment_text:
    return True
  if "sausage fingers" in comment_text:
    return True
  if "This comment was left automatically (by a bot)" in comment_text:
    return True
  if "this comment was written by a bot." in comment_text:
    return True
  if "*beep. boop.*" in comment_text:
    return True
  if "*Beep, I'm a bot.*" in comment_text:
    return True
  if "Bleep-bloop, I'm a bot." in comment_text:
    return True
  if "^(I am a bot.)" in comment_text:
    return True
  if "^^I'm ^^a ^^bot," in comment_text:
    return True
  if "I am a bot" in comment_text:
    return True
  if "I'm a robot." in comment_text:
    return True
  if "Reposted from the bot profile" in comment_text:
    return True
  if "OTHERS CLICKED THIS LINK" in comment_text:
    return True
  if "CLICK THIS LINK" in comment_text:
    return True
  if "haikusbot" in comment_text:
    return True
  if "LimbRetrievalBot" in comment_text:
    return True
  if "AyyLmao2DongerBot" in comment_text:
    return True
  # Not a bot comment but still messes things up
  if "⣿" in comment_text:
    return True
  if comment_text == "[deleted]":
    return True
  if comment_text == "[removed]":
    return True
  if comment_text == "[Removed by reddit]":
    return True
  return False

def remove_links(comment_body):
  while "https://" in comment_body:
    for word in re.split(r'[\s()]+', comment_body):
      if "https://" in word:
        url_length = len(word)
        break
    start_of_url = comment_body.index("https://")
    comment_body = comment_body[0:start_of_url] + comment_body[start_of_url + url_length:]
  while "![img](emote" in comment_body:
    start = comment_body.index("![img](emote")
    i = start
    while comment_body[i] != ")":
      i += 1
    comment_body = comment_body[0:start] + comment_body[i + 1:]
  while "![gif](giphy|" in comment_body:
    start = comment_body.index("![gif](giphy|")
    i = start
    while comment_body[i] != ")":
      i += 1
    comment_body = comment_body[0:start] + comment_body[i + 1:]
  while "emote:" in comment_body:
    start = comment_body.index("emote:")
    i = start
    while comment_body[i] != ":":
      i += 1
    i += 1
    while comment_body[i].isnumeric():
      i += 1
    comment_body = comment_body[0:start] + comment_body[i:]
  while "u/savevideobot" in comment_body:
    start = comment_body.index("u/savevideobot")
    comment_body = comment_body[0:start] + comment_body[start+14:]
  while "u/savevideo" in comment_body:
    start = comment_body.index("u/savevideo")
    comment_body = comment_body[0:start] + comment_body[start+11:]
  comment_body = comment_body.replace("\n", ". ").replace("\r", " ").replace("_", "")
  return comment_body

def top_of_all_time():
  
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

# def search_flair(flair):
#   # Continuing where it leaves off
#   # list_of_posts = open("posts_seen.txt", "a")

#   for post in sub.search("flair:" + flair, sort="top"):
#     # if post.id in posts_seen:
#     #  continue
#     # else:
#     #  posts_seen.add(post.id)
#     #  list_of_posts.write(post.id + "\n")
#     post.comments.replace_more(limit=None)
#     all_comments = post.comments.list()
#     for comment in all_comments:
#       if 'Adachi' in comment.body or "adachi" in comment.body:
#         print("1.", post.id)
#         print("2.", comment.id)
#         print("3.", comment.author)
#         print("4.", comment.body)
#       if is_bot(comment.body):
#         continue
#       #comment_body = remove_links(comment.body)
#       #csv.write(comment_body + "," + str(comment.score) + "\n")

list_of_posts = open("basil_subreddits/posts_seen_basilcult.txt", "w")
posts_seen = set()
comments_csv = open("basil_subreddits/comments_top_basilcult.csv", "w")
top_of_all_time()
# comments_csv = open("comments_flairs.csv", "w")
# for flair in ["Art", "Meme", "Discussion", "Question", "Merch", "Manga", "Cosplay", "Theory", "Meta", "Music", "Guide", "Mod", "Other"]:
#   print(flair)
#   search_flair(flair)
print(len(posts_seen), "posts were collected.")

sub = reddit.subreddit("antibasil")
list_of_posts = open("basil_subreddits/posts_seen_antibasil.txt", "w")
posts_seen = set()
comments_csv = open("basil_subreddits/comments_top_antibasil.csv", "w")
top_of_all_time()
print(len(posts_seen), "posts were collected.")
# Continuing where it leaves off
# posts_seen = set()
# with open("posts_seen.txt", "r") as list_of_posts:
#   line = list_of_posts.readline()
#   while line != "":
#     posts_seen.add(line.strip())
#     line = list_of_posts.readline()

#comments_csv = open("comments_flairs.csv", "a")
# for flair in ["Other"]:
#   print(flair)
#   search_flair(flair)
#print(len(posts_seen), "posts were collected.")




# longest_comment = ""
# for filename in ["comments_of_top_posts.csv", "comments_flairs.csv"]:
#   i = 0
#   with open(filename) as comment_csv:
#     for line in comment_csv:
#         i += 1
#         separator = line.rfind(",")
#         comment_body = line[0:separator]
#         if len(comment_body) > len(longest_comment):
#            longest_comment = comment_body
#            print(i)
# print(longest_comment)

# Longest post

# sub = reddit.subreddit("OMORI")
# longest_title = ""
# num_with_longest_title = 0
# id_of_longest_post = ""
# len_of_longest_post = 0  

# for post in sub.top(limit=None):
#   if len(post.title) > len(longest_title):
#     longest_title = post.title
#     num_with_longest_title = 1
#   elif len(post.title) == len(longest_title):
#     num_with_longest_title += 1
  
#   if len(post.selftext) > len_of_longest_post:
#     len_of_longest_post = len(post.selftext)
#     id_of_longest_post = post.id

# for flair in ["Art", "Meme", "Discussion", "Question", "Merch", "Manga", "Cosplay", "Theory", "Meta", "Music", "Guide", "Mod", "Other"]:
#   print(flair)
#   for post in sub.search("flair:" + flair, sort="top"):
#     if len(post.title) > len(longest_title):
#       longest_title = post.title
#       num_with_longest_title = 1
#     elif len(post.title) == len(longest_title):
#       num_with_longest_title += 1
    
#     if len(post.selftext) > len_of_longest_post:
#       len_of_longest_post = len(post.selftext)
#       id_of_longest_post = post.id
# print("Number of post titles with length", len(longest_title), "=", num_with_longest_title)
# print(longest_title)
# print("ID of longest post:", id_of_longest_post)