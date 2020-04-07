import json
import requests
user1=input("Enter First User ")
user2=input("Enter Second User ")
r1=requests.get('https://www.reddit.com/user/%s.json' % user1,headers = {'User-agent': 'wtf 0.1'})
r2=requests.get('https://www.reddit.com/user/%s.json' % user2,headers = {'User-agent': 'wtf 0.1'})
data1=r1.json()
data2=r2.json()
ups1=data1["data"]['children'][0]["data"]['ups']
ups2=data2["data"]['children'][0]['data']['ups']
if ups1>ups2:
	print(user1,"got more up votes")
else:
	print(user2,"got more up votes")
