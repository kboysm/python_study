# 리스트 컴프리헨션 (회사 프로젝트에서 소장님이 쓰신 문법이 포함되어 있음)

a= ['a','b','c']
b=[]
for i in a:
    b.append(i.upper())
print(a)
print(b)

    # 위의 a를 b로 인자를 변환하여 담는 코드를 한줄로 처리 가능
c = [i.upper() for i in a] # 이것이 리스트 컴프리헨션 !!!!!
print(c)


# f스트링
let1 = 'hello'
let2 = 'world'
let3 = f'{let1}...{let2}?' # 간결하면서 속도도 가장 빠르다
print(let3)

# str.split

