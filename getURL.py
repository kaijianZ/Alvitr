import requests
import re

# img_data = requests.get("https://avatars3.githubusercontent.com/u/14187523?v=3&s=460").content
# with open('image_name.jpg', 'wb') as handler:
#     handler.write(img_data)

# def getid(r18=False, date=''):

URL = requests.get('http://www.pixiv.net/ranking.php?mode=daily')

content = URL.text
pattern = re.compile('(?<=data-id=")\d*(?=">)')  # regular expression for pids
dataids = re.findall(pattern, content)
print(dataids)
