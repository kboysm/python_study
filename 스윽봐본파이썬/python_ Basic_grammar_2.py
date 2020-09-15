import time

a,b,c=1,'2',3 #혹시나 하고 해봤는데 역시나 됌
print(a,b,c)

# print(a+b) b가 str타입이므로 에러 발생
print(str(a)+b)

print('%s시 %s구 %s동'%('사랑','고백','행복')) #다른 언어와 비슷하게 format을 지정해서 할 수도 있음
print('{}시 {}구 {}동'.format('사랑','고백','행복')) # 보통 파이썬에서는 이렇게 많이 쓴다.

####
print(a,b,end='\t')
print(a,b,end='\t')
print(a,b,end='\t')
print(a,b,end='\t') 
#### 프린트를 \t으로 구분

####
print(a,b,end='\n')
print(a,b,end='\n')
print(a,b,end='\n')
print(a,b,end='\n')
#### 프린트를 \n으로 구분


####################
print(1,'재사용 기호 \\r',end='\r')
time.sleep(1)
print(2,'재사용 기호 \\r',end='\r')
time.sleep(1)
print(3,'재사용 기호 \\r',end='\r')
time.sleep(1)
print(4,'재사용 기호 \\r',end='\r')
time.sleep(1)
print(5,'재사용 기호 \\r',end='\r')
time.sleep(1)
print(6,'재사용 기호 \\r',end='\r')
time.sleep(1)
print(7,'재사용 기호 \\r',end='\r')
############### 