# lib - urllib read
import urllib.request

# url and save path 지정

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# download
urllib.request.urlretrieve(url,savename)
print("save finish")
