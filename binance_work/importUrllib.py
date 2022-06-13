import urllib

url = 'https://www.wikiart.org/ru'

response = urllib.urlopen(url)
webContent = response.read()

print(webContent[0:300])