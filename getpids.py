import requests
import re


def getpids():
    daily_list_page = requests.get('http://www.pixiv.net/ranking.php?mode=daily')
    pattern = re.compile('data-id="(\d*)">')
    # regular expression for pids

    return pattern.findall(daily_list_page.text)
    # return the pid of the daily pics
