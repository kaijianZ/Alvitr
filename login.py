import requests
import re


def login():
    session = requests.session()
    url = 'https://accounts.pixiv.net/login'
    r = session.get(url)
    pattern = re.compile('name="post_key" value="(.*?)">')
    result = pattern.findall(r.text)
    print(result[0])
    postkey = result[0]

    data = ({
        'pixiv_id': "chimoe",
        'password': "opensource",
        'captcha': '',
        'g_recaptcha_response': '',
        'post_key': postkey,
        'source': 'pc',
    })

    session.post(url, data=data)
    return session.cookies
