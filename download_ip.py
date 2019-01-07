# lib - urllib read
import urllib.request

# read data
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()
print(data)
# convert to binaray txt 
text = data.decode('utf-8')
print(text)