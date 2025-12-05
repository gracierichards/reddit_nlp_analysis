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

# hate_basil = """just makes people hate Basil more I've got; the people who hate Basil
# and defend Aubrey; why everyone would hate basil he's my favorite; how
# could you hate basil I actually went; eh I don't hate Basil I just
# hate; basil I don't hate basil he's just an; How can you hate Basil I
# wish there; How can you hate basil It is a; tell me You hate basil
# because of a; him I don't hate Basil but I think; flowerboy I don't
# hate Basil I just wanna; kel I dont hate Basil at all I; Wait people
# actually hate basil I wish we'd; fandom makes me hate basil they use
# the; even if people hate Basil that's valid Because; her mind I hate
# Basil Heheany second now; see people who hate Basil it makes me; panic
# attacker I hate basil because he is; Yup I fuckin hate Basil but I'll
# be; his shoes you hate Basil that much Maybe; many people still hate
# Basil with disturbing passion; get why people hate basil now Bruh Kel;
# again I FUCKING HATE BASIL BASIL SHOULD FUCKING; that's why i hate
# basil Wdym can throw; alone if you hate Basil Just Ignore them; VOTE
# BASIL I HATE BASIL ITS EITHER MEWO; the dumbass i hate basil im gonna
# murder; essay Everyone doesn't hate Basil the majority don't; I sort
# of hate basil as more as; understand if people hate Basil Faking
# Mari's suicide; haha pretend to hate basil running gag sorta; killable
# I honestly hate Basil fans more specially; why some people hate Basil
# dude writing stuff; vegan personally don't hate Basil he is a; i
# personally don't hate Basil he is a; He silly People hate Basil He's
# mine and; are jelly people hate basil i thought you; person who does
# hate Basil Like have you; why else You hate basil because he hung; I
# do not hate basil as I think; of people who hate basil You'd be
# surprised; I do not hate Basil or Sunny I'm; why some people hate
# basil So I noticed; if they're gonna hate Basil do it from; way I
# don't hate Basil Well headspace isn't; why do people hate basil I was
# answering; why shouldn't people hate basil I don't hate; is why i hate
# basil Fuck you Basil; Fourthly Omori doesn't hate Basil I think if;
# Omori does not hate Basil the reason Omori; softboi I dont hate basil
# Sunny still killed; true sunny may hate basil but that just; of basil
# i hate basil because they keep; why would you hate Basil posts we're
# only; Fuck people who hate basil Weird kink but; anyways I don't hate
# Basil I hate how; WHY DO PEOPLE HATE BASIL BLEND THE MINT; the people
# who hate basil are mentally stable; is overrated I hate basil gimme
# downvotes I; exist I don't hate Basil he's a very; Ngl I don't hate
# Basil but I don't; Why does everyone hate basil so much When; once
# seen someone hate Basil I mean i; people i meet hate basil and yell
# at; a secret ending Hate Basil this isnt a; game but just hate Basil
# cuz yes remember; hates sunnyhe would hate basil too but has; and
# comment i hate basil anyone with me; stan and I hate Basil Basil pulls
# of; Omori fans who hate Basil baffle me I; all I don't hate Basil but
# I do; y'all I don't hate basil but still don't; understand why some
# hate basil but bro was; why do people hate Basil He might have; s s i
# hate basil and don't stan; BOTH I don't hate Basil I love both; me why
# people hate basil As a Basil; Aubrey stan who hate Basil I hate Basil;
# developed I just hate basil cause its fun; why do people hate basil
# tho i'm not; is If you hate basil you like aubrey; hate Aubrey or hate
# basil I hate Aubrey; Me who doesn't hate basil because I like; know
# why people hate basil Screw Basil stan; all my homies hate basil Well
# technically in; ship lmfao i hate basil because he is; my mind i hate
# basil dont read my; all my homies hate Basil I see more; hate people
# who hate basil or aubrey I; the people who hate basil stan aubrey and;
# know why people hate basil and they are; ALL MY HOMIES HATE BASIL this
# has been"""

# basil_hate = """PINK-HAIRED FAVORITE but Basil hate is so disproportionate; BOI BAGEL
# The Basil hate makes me sad; Lmfao if this Basil hate is the worst;
# Most of the Basil hate is from people; did his friends Basil hate
# isn't the worst; But does the Basil hate actual justify and;
# complaining about the Basil hate and then leading; something with the
# Basil hate on this sub; DONT UNDERSTAND THE BASIL HATE I like
# brasilbagelbabel; It's like the Basil hate posts or defending; the
# post about basil hate No you're thinking; response specifically to
# Basil hate not an argument; response specifically to Basil hate not an
# argument; I think the basil hate is super unwarranted; from me no
# Basil hate at all friend; overated though Good basil hate is ok Fuck;
# there so much Basil hate in this sub; did It ain't Basil hate is just
# that; a lot of basil hate a lot of; just reinvigorated my basil hate
# FUCK BASIL THAT; their OC with Basil Hate to be that; haven't seen
# active Basil hate here Most people; barely see any basil hate posts
# and if; was full of Basil hate posts but not; downvoted lol but basil
# hate comments have lots; real than Deserved Basil hate I actually
# like; that gif as basil hate at first thought; dont carry for basil
# hate again this is"""

# print("---Matches for Hate Basil---")
# for result in hate_basil.replace("\n", " ").split(";"):
#   print(result)
# print("---Matches for Basil Hate---")
# for result in basil_hate.replace("\n", " ").split(";"):
#   print(result)

# print("---Matches for Love Basil---")
# text = nltk.Text(tokens)
# text.findall(r'<.*> <.*> <.*> <[Ll][Oo][Vv][Ee]> <[Bb][Aa][Ss][Ii][Ll]> <.*> <.*> <.*> <.*> <.*> <.*> <.*> <.*> <.*> <.*> <.*> <.*>')
# Zero matches for Basil Love
love_basil = """plant boy I love Basil his personality and hobbieslikes really hit
home When I played the game; Seriously though I love Basil so much
it's nice to have a character to relate to 3; stfu i fucking love
basil I don't hate basil he's just an alpha male lucky enough to; Bro
I fkin love BAsil because hes that on the outside obnoxiously happy
person but while helping; like Basil i love basil his birthday is
right next to mine and his beta name is; the game I love basil because
I feel like my personality is some sort of amalgam of; but I do love
Basil on his own Sunny too but we're talking basil politics here
guess; of hate I love Basil but now I need to see this What Link The
machine Unfortunate; tell but I love Basil umeomoc207 id either be
brazil or sunny Mari's a psychic type There; though because I love
basil he's very very cute Haven't done the other routesendings yet The
photo; incidents i do love basil to the moon and back and he is my
favourite out of; then Basil I love Basil I fucking hate this so much
for one thing Basil did try; were close I love Basil so much but yeah
Kel sets a standard of friend that's hard; spoiling assholes I Love
basil omg hiiii He is in fact baby Also I'd be careful reading; so
cute I love basil Tbh watermellons are cool idk why but i wanted to
say it; game and I love basil so much i want him to be happy and
healthy &#x200B Basil; is holy i love basil and reads books Aubrey
knows basil Related This is only based on; I know I love basil Nah
Basil can go both versions I love Space Ex-husband Same Why; Basil
because I love Basil Basil omori cuz he is just like me Omor because
knifu The; world I really love Basil for his cute flower crown and I
love Mari's detailed outfit Hero's; gotta worry We love basil I'm bi
and i don't care if he's real or not I'm; pansexual and I love Basil
so your not the only one lol He's such a soft boi; mr jawsum I LOVE
BASIL Stranger DD Basil auby snuuy omor and hero Wee cactus bi for;
AND BASIL I LOVE BASIL Mari Kel is the only correct answer Basil hes
hot this gif; best boy I love Basil I liked him since he was first
introduced very complex character I; all seriousness i love basil no
there's more My favorite started as hero then went to Aubrey; life
Basil is love Basil is Basil How in the Heck do I have 272 upvotes I;
babil dw i love basil he's my favorite too 3 even did a cosplay of him
like; alone lol I LOVE BASIL SO MUCH Bagel my beloved bail is the best
i have never; my heart I LOVE BASIL SO MUCH I DONT UNDERSTAND THE
BASIL HATE I like brasilbagelbabel but; but i do love basil I LOVE
BASIL VTCDXRCY I thinm a lot of people oike Basil; BOY No I love Basil
Nah i'm setting up a cosplay as him I really don't get; Basil speen i
love basil as well i dont know how people hate this little fella
Sooooo; is basil I love basil I LOVE HIM 🥰😍🥰🥰😍 Basil 🔛🔝 I like Basil
One of my; Mari Nope I love BASIL with all my heart Basil is one of my
favorites no i; cop Babil i love basil my partner loves basil they
have a basil tattoo D bagel our; Honestly Basil I love Basil so much
he's my precious plant child but he's so goddamn helpless; gotta sleep
I love basil but damn that kid is scary Aubrey emo chick is scary and;
5 enjoy I love Basil ❤️ he's my favorite silly goober babil He
breathed burn him I; wrong I actually love basil He's my favorite
character and sunflower is my favorite ship Downvote me; care Idk I
love basil and can't understand why people like Aubrey so much It's
all about; Left ❤️ I love basil both as a relatable character and as
an interestingly written character his; probably wasureta We love
Basil It's hard to explain but making fun of him is simply our; said
so I love basil Umwtf I thought I had the whole omori story Apparently
I don't; he did I love Basil he's one of my favorites the only thing
is that while playing; primal instincts I love Basil he's my favorite
character and i relate to him a bit too; hate him I love Basil idk
what you are talking aboutI love this plant loving child because; and
Dude I love Basil now How the fuck I don't like the Omori fandom's
tendency to; And why I love Basil Tbf most people here aren't
psychologists Everyone is being really sensitive about; pattern
baldness I love basil Im working on my collection little by little i
am aspiring to; that Also I love Basil with glasses Peak fiction alert
I want to say one thing about; fuck man i love basil with every cell
in my body but i would absolutely shove him; SLAYING AAAAA I LOVE
BASIL COSPLAYERS IMMA SOON BECOME ONE TOO D omg it's amazing removed
removed; guy Anyway I love Basil and not Rowan who is not Basil ergo I
think Basil is; and design I love Basil I could hug him so much yeah
Apperantly Basil was called Rowan; fans Like we love Basil we just
took him out for other reasons Not planning on taking; side effects I
love basil he so adorable an cute I mean sounds to me like you're; the
skrunkly i love basil I love the Babil He's so goofy he's so small I
want; stan i fucking love basil and crave violence against those who
hate him Nah no Omori character; their opinions I love Basil and
Aubrey because I relate to both of them a bit to; tho I kinda love
basil so— You finding out that chads exist why do people hate basil;
Aubrey and I love basil Shut up Me who doesn't hate basil because I
like Aubrey but; sunny and i love basil i'm the same age as him So I
like to imagine the"""
print("---Matches for Love Basil---")
for result in love_basil.replace("\n", " ").split(";"):
  print(result)