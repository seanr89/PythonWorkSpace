import requests

res = requests.get('https://codedamn.com')
# res = requests.get('https://www.better.org.uk/leisure-centre/belfast')
txt = res.text
status = res.status_code

print(txt, status)
# print the result
ls
