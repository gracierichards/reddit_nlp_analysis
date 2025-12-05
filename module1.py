import nltk
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import re

flairs = ["Art", "Meme", "Discussion", "Question", "Merch", "Manga", "Cosplay", "Theory", "Meta", "Music", "Guide", "Mod", "Other"]

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
  if "^with ^issues ^or ^feedback!" in comment_text:
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
  # Removes ![img](emote...)
  comment_body = re.sub(r'!\[img\]\(emote[^)]+\)', "", comment_body)
  # Removes ![gif](giphy|...)
  comment_body = re.sub(r'!\[gif\]\(giphy\|[^)]+\)', "", comment_body)
  # Removes emote:
  comment_body = re.sub(r'emote:\d+', "", comment_body)
  comment_body = comment_body.replace("u/savevideobot", "").replace("u/savevideo", "")
  comment_body = comment_body.replace("\n", ". ").replace("\r", " ").replace("_", "").replace("’", "'")
  return comment_body

stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")
def basic_tokenizer(str):
  for punc in '.,?!^<>():;/"“”*\\[]…➜':
    str = str.replace(punc, "")
  words = str.lower().split()
  tokens = []
  for word in words:
    stemmed = stemmer.stem(word)
    if stemmed not in stop_words:
      tokens.append(stemmed)
  return tokens