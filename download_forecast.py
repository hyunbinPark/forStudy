import urllib.request
import urllib.parse

# 기상청 rss api url
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수 
value = {'stnId':'109'}
# 매개변수를 url 인코딩
params = urllib.parse.urlencode(value)

# 요청 전용 url 생성
url = API +"?"+params
print("url = ",url)

# download
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)