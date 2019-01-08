# lib - urllib read
import urllib.request

# url and save path 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

#download
mem = urllib.request.urlopen(url).read()

#save as file
with open(savename,mode="wb") as f:
    f.write(mem)
    print("save finish")