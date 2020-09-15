'''
a= set('aabbachhdefgg')
b= set('hhdefkkllmmi')
c= set('efggijjppnn')


print(a|b)
print(a-c)
print(a&b&c)

markets = input("입력: ") # melon banana strawberry melon banana blueberry banana strawberry
answer = set(markets.split())
print(answer)
'''
a= {} # 내용물을 ,단위로 잘라서 넣으면 set이 됌 , 그러나 아무것도 넣지 않으면 dict임 ...
b =set()
print(type(a))
print(type(b))
print(a)
print(b)