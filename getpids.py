import datetime
import re

import requests

import saveimg


class Downloader(object):
    def get_pids(self):
        pass


class Daily(Downloader):
    def __init__(self, date=""):
        self.date = date

    def get_pids(self):
        date_url = ''
        # date_url being empty means show today's result

        if len(self.date):
            year, month, day = self.date.split('-')
            if datetime.date(year=int(year), month=int(month), day=int(day)) < datetime.date.today():
                date_url = "&date=" + year + month + day
            else:
                self.date = str(datetime.date.today())

        daily_list_page = requests.get('http://www.pixiv.net/ranking.php?mode=daily' + date_url)
        pattern = re.compile('data-id="(\d*)">')
        # regular expression for pids of daily pics

        return pattern.findall(daily_list_page.text), saveimg.mkdir(date=self.date)
        # return the pids


class Tag(Downloader):
    def __init__(self, tag):
        self.tag = tag

    def get_pids(self):
        tag_list_page = requests.get('https://www.pixiv.net/search.php?s_mode=s_tag_full&word=' + self.tag)
        pattern = re.compile('data-id="(\d*)"')
        # regular expression for pids of popular pics of specific tag

        return list(set(pattern.findall(tag_list_page.text))), saveimg.mkdir(tag=self.tag)
        # avoid duplicate pid
