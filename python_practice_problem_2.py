a= set('aabbachhdefgg')
b= set('hhdefkkllmmi')
c= set('efggijjppnn')


print(a|b)
print(a-c)
print(a&b&c)

markets = input("입력: ") # melon banana strawberry melon banana blueberry banana strawberry
answer = set(markets.split())
print(answer)
