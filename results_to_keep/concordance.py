import nltk
import sys
import os

def my_tokenizer(str):
  for punc in '.,?!^<>():;/"“”*\\[]…➜':
    str = str.replace(punc, "")
  str = str.replace("’", "'")
  return str.split()

tokens = []
with open("comments_of_top_posts.csv", "r") as file1:
  for line in file1:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    tokens.extend(my_tokenizer(comment_body))
with open("comments_flairs.csv", "r") as file2:
  for line in file2:
    separator = line.rfind(",")
    comment_body = line[0:separator]
    tokens.extend(my_tokenizer(comment_body))

# print("---Matches for Hate Basil---")
# text = nltk.Text(tokens)
# text.findall(r'<.*> <.*> <.*> <[Hh][Aa][Tt][Ee]> <[Bb][Aa][Ss][Ii][Ll]> <.*> <.*> <.*>')

# print("---Matches for Basil Hate---")
# text.findall(r'<.*> <.*> <.*> <[Bb][Aa][Ss][Ii][Ll]> <[Hh][Aa][Tt][Ee]> <.*> <.*> <.*>')
# sys.exit()

hate_basil = """just makes people hate Basil more I've got; the people who hate Basil
and defend Aubrey; why everyone would hate basil he's my favorite; how
could you hate basil I actually went; eh I don't hate Basil I just
hate; basil I don't hate basil he's just an; How can you hate Basil I
wish there; How can you hate basil It is a; tell me You hate basil
because of a; him I don't hate Basil but I think; flowerboy I don't
hate Basil I just wanna; kel I dont hate Basil at all I; Wait people
actually hate basil I wish we'd; fandom makes me hate basil they use
the; even if people hate Basil that's valid Because; her mind I hate
Basil Heheany second now; see people who hate Basil it makes me; panic
attacker I hate basil because he is; Yup I fuckin hate Basil but I'll
be; his shoes you hate Basil that much Maybe; many people still hate
Basil with disturbing passion; get why people hate basil now Bruh Kel;
again I FUCKING HATE BASIL BASIL SHOULD FUCKING; that's why i hate
basil Wdym can throw; alone if you hate Basil Just Ignore them; VOTE
BASIL I HATE BASIL ITS EITHER MEWO; the dumbass i hate basil im gonna
murder; essay Everyone doesn't hate Basil the majority don't; I sort
of hate basil as more as; understand if people hate Basil Faking
Mari's suicide; haha pretend to hate basil running gag sorta; killable
I honestly hate Basil fans more specially; why some people hate Basil
dude writing stuff; vegan personally don't hate Basil he is a; i
personally don't hate Basil he is a; He silly People hate Basil He's
mine and; are jelly people hate basil i thought you; person who does
hate Basil Like have you; why else You hate basil because he hung; I
do not hate basil as I think; of people who hate basil You'd be
surprised; I do not hate Basil or Sunny I'm; why some people hate
basil So I noticed; if they're gonna hate Basil do it from; way I
don't hate Basil Well headspace isn't; why do people hate basil I was
answering; why shouldn't people hate basil I don't hate; is why i hate
basil Fuck you Basil; Fourthly Omori doesn't hate Basil I think if;
Omori does not hate Basil the reason Omori; softboi I dont hate basil
Sunny still killed; true sunny may hate basil but that just; of basil
i hate basil because they keep; why would you hate Basil posts we're
only; Fuck people who hate basil Weird kink but; anyways I don't hate
Basil I hate how; WHY DO PEOPLE HATE BASIL BLEND THE MINT; the people
who hate basil are mentally stable; is overrated I hate basil gimme
downvotes I; exist I don't hate Basil he's a very; Ngl I don't hate
Basil but I don't; Why does everyone hate basil so much When; once
seen someone hate Basil I mean i; people i meet hate basil and yell
at; a secret ending Hate Basil this isnt a; game but just hate Basil
cuz yes remember; hates sunnyhe would hate basil too but has; and
comment i hate basil anyone with me; stan and I hate Basil Basil pulls
of; Omori fans who hate Basil baffle me I; all I don't hate Basil but
I do; y'all I don't hate basil but still don't; understand why some
hate basil but bro was; why do people hate Basil He might have; s s i
hate basil and don't stan; BOTH I don't hate Basil I love both; me why
people hate basil As a Basil; Aubrey stan who hate Basil I hate Basil;
developed I just hate basil cause its fun; why do people hate basil
tho i'm not; is If you hate basil you like aubrey; hate Aubrey or hate
basil I hate Aubrey; Me who doesn't hate basil because I like; know
why people hate basil Screw Basil stan; all my homies hate basil Well
technically in; ship lmfao i hate basil because he is; my mind i hate
basil dont read my; all my homies hate Basil I see more; hate people
who hate basil or aubrey I; the people who hate basil stan aubrey and;
know why people hate basil and they are; ALL MY HOMIES HATE BASIL this
has been"""

basil_hate = """PINK-HAIRED FAVORITE but Basil hate is so disproportionate; BOI BAGEL
The Basil hate makes me sad; Lmfao if this Basil hate is the worst;
Most of the Basil hate is from people; did his friends Basil hate
isn't the worst; But does the Basil hate actual justify and;
complaining about the Basil hate and then leading; something with the
Basil hate on this sub; DONT UNDERSTAND THE BASIL HATE I like
brasilbagelbabel; It's like the Basil hate posts or defending; the
post about basil hate No you're thinking; response specifically to
Basil hate not an argument; response specifically to Basil hate not an
argument; I think the basil hate is super unwarranted; from me no
Basil hate at all friend; overated though Good basil hate is ok Fuck;
there so much Basil hate in this sub; did It ain't Basil hate is just
that; a lot of basil hate a lot of; just reinvigorated my basil hate
FUCK BASIL THAT; their OC with Basil Hate to be that; haven't seen
active Basil hate here Most people; barely see any basil hate posts
and if; was full of Basil hate posts but not; downvoted lol but basil
hate comments have lots; real than Deserved Basil hate I actually
like; that gif as basil hate at first thought; dont carry for basil
hate again this is"""

print("---Matches for Hate Basil---")
for result in hate_basil.replace("\n", " ").split(";"):
  print(result)
print("---Matches for Basil Hate---")
for result in basil_hate.replace("\n", " ").split(";"):
  print(result)