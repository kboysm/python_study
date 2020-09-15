dataString=' i like you'
dataString0=" i don't like you"
testString = 'please, don\'t say to me' # \기호로 '의 특수문자 특성을 없앤다.
print(dataString)
print(dataString0)
print(testString)

print('1st\n2nd') #출력해보면 1st 엔터 2nd로 출력된다.
print('1st\t2nd') #출력해보면 1st 탭 2nd로 출력된다.

print('C:\new_forder') #경로를 입력할 때 이런식으로 작성하면 줄바꿈이 되어버림
print('C:\test') #이것도 경로를 쓴건대 tab이 들어가게 됌

#해결방법

print(r'C:\new_forder') # or , r은 현재 문자열을 한개의 로우로 취급하겠다는 의미
print('C:\\new_forder') # 여기서는 역슬래쉬의 특성을 뒤에 있는 역슬래쉬가 지워준다.

print(r'C:\test')
print('C:\\test')

print('''
엔터를 친 위치는 엔터가 돼어 출력된다.
''')

print('''\
역슬래쉬를 입력하면 엔터를 무시한다.\
''')

a = 'test'
print(a*3)
print(a+a)
# print(a-'est') - 연산자는 먹지 않음 
print(testString[0]) #첫번째 문자가 나오는것으로 보아 내부적으로 배열처리
print(testString[0:5]) # 0~4까지의 문자가 나옴 [:5] 앞에 것을 생략하면 자동으로 0부터 , [4:] 뒤에것을 생략하면 맨 마지막까지 출력

print(testString.find('to')) # find함수를 활용하면 몇번째에 존재하는지 index를 반환 , 존재하지 않는 문자열이면 -1을 리턴

# index() vs find() 거의 비슷한데 index를 사용할 시 없는 문자열을 찾으면 에러가 발생함