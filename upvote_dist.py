import praw

reddit = praw.Reddit(
    client_id="6MSiXboPbWTdqm72ErnWpQ",
    client_secret="lswiD1a6bjaHLq-a_22lzhJvEOfOjQ",
    user_agent="App 1 by busyhope",
)

sub = reddit.subreddit("OMORI")
#for post in sub.new(limit=10):
#  print("Title:", post.title, "\tUpvotes:", post.ups, "Downvotes:", post.downs)
#post = reddit.submission("uopblx")
#print("Title:", post.title, "\tUpvotes:", post.ups, "Downvotes:", post.downs)
#print(vars(post))
comment = reddit.comment("nqhozeo")
print("Body:", comment.body, "\tUpvotes:", comment.ups, "Score:", comment.score)