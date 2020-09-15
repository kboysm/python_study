#연습문제 1
listA=[1,2,3,'string']
# listA.append(1)
# listA.append(2)
# listA.append(3)
# listA.append('a')
# listA.append('b')
# listA.append('c')
listA += ['a','b','c',1,2,3] # 위의 append를 한줄로 처리 가능

print(listA)
print(listA.index(1))
print(listA.index(2))
print(listA.index(3))
print(listA.index('string'))
print(listA.count(1))

#연습문제 2
stringA = 'I love you, John!'
a=stringA.split()
print(a)
print('John!' in a)
print(a.__len__())
print(len(a)) #21라인과 동일

### 연습문제로 배우는 tuple

tuple1 = 1234,5678,'abcd','efgh'
print(type(tuple1))
print(tuple1[0])
print(tuple1[1])
# tuple1[0] =1234 tuple의 내용은 바꿀 수 없다 . 바꾸려고 하면 에러 발생