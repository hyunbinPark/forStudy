import requests
r = requests.get("http://wikibook.co.kr/wikibook.png")

# save data as Binary 

with open("test.png", "wb") as f :
    f.write(r.content)

print("saved")