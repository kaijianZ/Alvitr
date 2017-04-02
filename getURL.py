import requests
import re


def getpid():
    URL = requests.get('http://www.pixiv.net/ranking.php?mode=daily')

    content = URL.text
    pattern = re.compile('data-id="(\d*)">')  # regular expression for pids
    return re.findall(pattern, content)
