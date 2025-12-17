import requests
from requests_html import HTMLSession
#from pprint import pprint
import sys

output_file = open("results_to_keep/game_text/OMORI_game_text.txt", "w")

url = "https://goats.dev/omori/maptext.html#"
session = HTMLSession()
r = session.get(url)
r.html.render()
for option in r.html.find("select#characters", first=True).find("option"):
  text_page = url + option.text
  r = session.get(text_page)
  r.html.render()
  actual_content_div = r.html.find("#textboxes", first=True)
  for textbox in actual_content_div.find("div.textbox"):
    output_file.write(textbox.text + "\n")