import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER = "testGuest"
PASS=  "test1234"

#start session

session = requests.session()

#log in

login_info = { "m_id" : USER, "m_passwd": PASS }

url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login , data =login_info)
res.raise_for_status() # error > excetion 

# go to my page 

url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# get mileage & e-coin

soup = BeautifulSoup(res.text,"html.parser")
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print(" Mileage : ", mileage)
print(" E-Coin : ", ecoin)