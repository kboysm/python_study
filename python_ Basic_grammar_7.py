# pip install requests 다운
import requests
import json
# dns = input('dns:')
res=requests.get('http://ip-api.com/json/naver.com') #naver.com 자리에 dns를 넣으면 원하는 사이트의 정보를 얻음
print(res.text)

result = json.loads(res.text) # load는 파일에서 loads는 스트링에서 사용
print(result)
print(type(result)) #dict

for i in result.keys():
    print(i, ':',result[i])