from requests_html import HTMLSession
import os
from dotenv import load_dotenv

s = HTMLSession()
load_dotenv() 

query = 'italy'
url = 'https://www.google.com/search?q=weather+' + query
user_agent = os.getenv("USER_AGENT")

r = s.get(url, headers={'User-Agent': user_agent})


temp = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

print(query, temp, unit, desc)