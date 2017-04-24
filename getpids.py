import requests
import re
import datetime
import saveimg


class Daily(object):
    def __init__(self, date=""):
        self.date = date

    def get_pids(self):
        if len(self.date):
            year, month, day = date.split('-')
            if datetime.date(year=int(year), month=int(month), day=int(day)) < datetime.date.today():
                date_url = "&date=" + year + month + day
            else:
                date_url = ''
        else:
            date_url = ''
        daily_list_page = requests.get('http://www.pixiv.net/ranking.php?mode=daily' + date_url)
        pattern = re.compile('data-id="(\d*)">')
        # regular expression for pids of daily pics

        return pattern.findall(daily_list_page.text), saveimg.mkdir(self.date)
        # return the pids

# def getpids_tag():
