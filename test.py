#coding:utf-8
import requests
import json
import time
from bs4 import BeautifulSoup

group_id = '105259197447'
token = 'CAACEdEose0cBAA5EuEyycDZAk0QHQOw15A1CxEhEZAhTZB0fsb0ubzJUrD2ZAGduRE7iQ4TVVrZC19IjncqvuIKI9KlYLD46qdSVO0O8eV6ljIMKM2JF1aFYiZBqSRNRA87DZChIjc4Lce7gfgd8lD8UAfLRncu3f19V6uvI4QDaZBxTf7PW23Ol5oIeidJbJxCuHZCoOunuHFEx5KI4LkpVX'
field = '?fields=name,posts.limit(5).since(1404144000){link,id,message,likes,comments}&access_token='
url = 'https://graph.facebook.com/' + group_id + field + token
response = requests.get(url)
print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
