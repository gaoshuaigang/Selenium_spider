from urllib.request import urlopen

url = "https://www.tencent.com"

aaa = urlopen(url)

with open("demo.html",mode="w") as f:
    f.write(aaa.read().decode("utf-8"))
print('over!')