import re

import requests


def login(id, password):
    session = requests.session()
    url = 'https://accounts.pixiv.net/login'

    # get a post_key for login
    # check ref [2] for details
    login_page = session.get(url)
    pattern = re.compile('name="post_key" value="(.*?)">')
    result = pattern.findall(login_page.text)
    post_key = result[0]

    data = ({
        'pixiv_id': id,
        'password': password,
        'captcha': '',
        'g_recaptcha_response': '',
        'post_key': post_key,
        'source': 'pc',
    })

    # actual login
    session.post(url, data=data)

    login_fail_flag = re.compile('イラストコミュニケーションサービス')
    login_success = not len(
        login_fail_flag.findall(session.get("https://www.pixiv.net").text))

    return login_success, session.cookies
    # return cookies
