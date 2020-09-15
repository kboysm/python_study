a =set('1234567')
b =set('4567890')
print(a)
print(b)

print(a-b) #차집합
print(a|b) #합집합
print(a&b) #교집합
print(a^b) #합집합에서 교집합을 제외한 집합
c = list(a | b)
print('c : ',  c.sort())
print('sorted : ', sorted(c))
market = { 'beef','pork','lamb','beef','pork','lamb','beef','pork','lamb' } #중괄호는 set을 의미한다

print(market)
print(len(market))