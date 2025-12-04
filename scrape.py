import requests

data = {'grant_type': 'password', 'username': 'busyhope', 'password': 'btbY22ZK%879'}
auth = requests.auth.HTTPBasicAuth('6MSiXboPbWTdqm72ErnWpQ', 'lswiD1a6bjaHLq-a_22lzhJvEOfOjQ')

r = requests.post('https://www.reddit.com/api/v1/access_token', data=data, headers={'User-Agent': 'App 1 by busyhope'}, auth=auth)
d = r.json()

access_token = 'bearer ' + d['access_token']

headers = {"Authorization": access_token, "User-Agent": "App 1 by busyhope"}
#response = requests.get("https://oauth.reddit.com/r/OMORI/top", headers=headers, params={"t": "all", "limit": 100})
#print(len(response.json()['data']['children']))
#first_post = response.json()['data']['children'][0]
#print(first_post['data']['title'] + ' by u/' + first_post['data']['author'])
#for post in response.json()['data']['children']:
#  if post['data']['selftext']:
#    print("Title:", post['data']['title'])
#    print("Title:", post['data']['selftext'])
#response = requests.get("https://oauth.reddit.com/r/OMORI/comments/1ov2y5v/theory_about_something_i_hope_its_not_popular/", headers=headers, params={})

response = requests.get("https://oauth.reddit.com/r/OMORI/comments/kt1fsk", headers=headers, params={})
for comment in response.json()[0]['data']['children']:
  print(comment['data']['body'])


  