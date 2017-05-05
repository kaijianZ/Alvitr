import requests
import re

def Choose(self,opener):     #Deside if get ranking or sth
    if (self.p_choice == 'ranking'):  
        try:  
            p_page = opener.open(self.p_ranking_url)   #p_ranking_url = 'hthttp://www.pixiv.net/ranking.php?mode=daily?
			pattern = re.compile('data-id="(\d*)">')

			return pattern.findall(daily_list_page.text)
			except:
				print"没有，滚"
		else:
		#following:https://www.pixiv.net/bookmark.php?type=user&id=USERID
		#USERID is the numbers (user_pid)
		#TAG:https://www.pixiv.net/search.php?s_mode=s_tag_full&word=TAG
		#RECOMMENDATION ETC
			print"现在还没有 滚"
