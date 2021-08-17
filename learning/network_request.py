from urllib import request

with request.urlopen("https://formidable.com/") as response:
    html = response.read()
    print(html)

