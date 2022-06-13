import requests
url = ""
print(url)
r = requests.get(url)
with open('test.html', 'wb') as output_file:
    output_file.write(r.text.encode('utf-8'))
output_file.close() 