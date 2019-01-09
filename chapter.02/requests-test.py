import requests

r = requests.get("http://api.aoikujira.com/time/get.php")

# read as text type

text = r.text
print(text)

# read as binaray type

bin = r.content
print(bin)

