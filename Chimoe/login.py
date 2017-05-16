import requests
import re


def login():
    session = requests.session()
    url = 'https://www.pixiv.net/login.php'

    login_page = session.get(url)
    pattern = re.compile('name="post_key" value="(.*?)">')
    result = pattern.findall(login_page.text)
    post_key = result[0]

    data = ({
        'pixiv_id': "SAMPLE",#DEPEND ON USER
        'password': "SAMPLE",
		'pid'："SAMPLE"
        'post_key': post_key,
        'source': 'pc',
    })

	#'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

    session.post(url, data=data)
    
    return session.cookies
