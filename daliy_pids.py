import re
import datetime
import requests
import saveimg

# this code is used to get pixiv id from daily ranking
class Daily(object):
    def __init__(data, date = ""):
        data.date = date

    def get_pids(data):
        date_url = ''
        if len(data.date):
            year, month, day = data.date.split('-')
            if datetime.date(year = int(year), month = int(month), day = int(day)) < datetime.date.today():
                date_url = "&date=" + year + month + day
            else:
                data.date = str(datetime.date.today())

        daily_list_page = requests.get('http://www.pixiv.net/ranking.php?mode=daily' + date_url)
        pattern = re.compile('data-id="(\d*)">')

        return pattern.findall(daily_list_page.text), saveimg.mkdir(date = data.date)


