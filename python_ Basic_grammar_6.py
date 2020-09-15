# dictionary 자바스크립트의 object느낌
data ={ 1 : 'a' , 2: 'b'}
print(data.keys())
print(data.values())

data2 = {
    '김영수':{'영어':80, '수학':90},
    '최희수':{'영어':70, '국어':60}
}
print(data2.keys())
print(data2.values())
print(data2.items())

## 데이터 변경

print(data2['김영수'])

data2['김영수']['수학']=100
print(data2['김영수'])

data2['김영수']['가정'] =100
print(data2['김영수'])

for i in data2.keys():
    print(i, ':', data2[i])