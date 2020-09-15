# 함수 : 인풋 ->아웃풋
# def 함수명(..인자값):
import requests
import json
 #연습문제 1

def add_num2(listB):
    sum=0
    for j in listB:
        sum+=j
    return sum
'''
답지
def add_num2():
    list1 = input("띄어쓰기로 나눠서 숫자를 4개 입력:")
    a,b,c,d = list1.split()
    a,b,c,d = int(a),int(b),int(c),int(d)
    return a+b+c+d
'''
userInput = input('띄어쓰기로 나눠서 숫자를 4개만 입력: ')
listA = userInput.split()
listB =[]
for i in listA:
    listB.append(int(i))
print(add_num2(listB))

#연습문제 2

def getLocation(ip):
    res = requests.get('http://ip-api.com/json/'+ip)
    return json.loads(res.text) #res.json()으로도 가능
req =input('ip:')
print(getLocation(req))

'''
답지
def getLocation(ip):
    url='http://ip-api.com/json/'+ip
    res=requests.get(url)
    return res.json()
'''