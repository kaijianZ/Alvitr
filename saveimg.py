import requests
import re
import os
import datetime

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/\
537.36'
header = ({
    'Referer': 'http://www.pixiv.net/',
    'User-Agent': user_agent
})


def mkdir():
    path_today = 'images/' + str(datetime.date.today())
    if not os.path.exists(path_today):  # create the directory if it doesn't exist
        os.makedirs(path_today)
    return path_today


def saveimg(pids, cookies):
    image_dir = mkdir()
    for pid in pids:
        image_page = requests.get('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + pid,
                                  cookies=cookies)
        pattern_image_address = re.compile('data-src="(.*?)" class="original-image">')
        # get the actual URL of the pictures
        pattern_image_title = re.compile('<meta property="og:title" content="(.*?)">')
        image_address = pattern_image_address.findall(image_page.text)
        image_title = pattern_image_title.findall(image_page.text)[0]

        if len(image_address):
            image_address = image_address[0]
            # if it's Manga, do not download
        else:
            continue
        print(image_address)
        img_data = requests.get(image_address, cookies=cookies, headers=header).content
        with open(image_dir + '/' + image_title.replace('/', '_').replace(' [pixiv]',
                                                                          '') + 'pid=' + pid + image_address[
                                                                                               -4:],
                  'wb') as handler:
            handler.write(img_data)
