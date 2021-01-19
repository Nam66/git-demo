
import requests
from bs4 import BeautifulSoup

s =  requests.session()
payload = {
	'log': 'admin',
	'pwd': '123456aA'
}
url = "http://45.79.43.178/source_carts/wordpress/wp-login.php"
respone = s.post(url, data = payload)
soup = BeautifulSoup(respone.content, 'lxml')
finddivs = soup.findAll('div', {'class':'quicklinks'})
username = finddivs[0].findAll('li', {'class':'with-avatar'})[0].find('a').text
print('username: ', username)


	