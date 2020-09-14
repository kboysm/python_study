# python 에서는 None이 아무것도 없다라는 의미
print(bool(1)) # T
print(bool(-1)) # T
print(bool(0)) # F
print(bool([])) # F
print(bool([''])) # T
print(bool('')) # F
print(bool(None)) # F

a= [1,2,3,4,5]
b=[[1,2,3],'asd','cvb']
print(a[-3:])
print(a[1:4])

print(2 in a) # 'a'안에 2가 있냐고 물어봄
print(a.index(2))

print(a+b) #list끼리 덧셈 가능 , 곱셈도 가능
a.append('맨 마지막 인덱스로')
print(a)

# list.count( 데이터가 리스트에 몇개가 있느냐 ) , list.sort( 정렬) , list.index('찾는 문자열이 몇번째 인덱스인지')