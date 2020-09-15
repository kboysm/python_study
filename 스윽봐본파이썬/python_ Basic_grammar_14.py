# 파이썬의 파일 입출력 / 쓰기 : ( 열고 ,쓰고 , 닫고), 읽기 :( 열고 ,읽고 ,닫고 ) 
'''
파일을 입출력하는 것은 프로그래밍의 기본
파일을 입출력할 때 단 세가지만 기억
열고 쓰고 닫고 , 열고 읽고 닫고

파일 쓰기
f = open('파일명','w') 뒤에 붙는 인자값으로 운영체제에 무슨 작업을 할 건지 알려줘야 함 주의!
f.write('data')
f.close()

파일 추가 쓰기
f = open('파일명','a') // add의 약자
f.write('data')
f.close()

파일 읽기
f = open('파일명','r')
print(f.read())
f.close()

바이너리 파일 읽기
f = open('파일명','rb')
data=f.read()
print(data)
f.close()
'''

'''
with를 사용한 파일 읽기 쓰기
파이썬은 사용 후 반드시 제거해야 하는 객체의 경우에는 with를 사용하는 것이 좋음(소켓 등)
파일 핸들의 경우에 닫아주지 않는 상태가 중복되면 메모리 누수가 발생하여 프로그램이 비정상 종료
파일의 객체를 열어주었다면 반드시 닫아서 메모리 누수가 발생하지 않도록 주의하자

with open('파일명','w') as f:
    f.write('data')

with open('파일명','r') as f:
    print(f.read())
'''
# f=open('test.txt','w')
# f.write('2020-09-15 파이썬 공부중')
# f.close()

# f=open('test.txt','a')
# f.write('추가 데이터 줄바꿈 되나?? 아니면 바로 뒤에 붙나?? \n 여기까지 ') #자동 줄바꿈 x 기호로 다 추가해 줘야함
# f.close()

# f=open('test.txt','r')
# print(f.read())
# f.close()

# f=open('test.txt','rb')
# print(f.read().decode('cp949')) # 바이너리 코드를 읽을때는 이런 명령을 사용해서 읽음
# f.close()

with open('test.txt','r') as f:
    data = f.read() # 이게 왜 되지? 자바스크립트와 너무 달라서 혼동... let,const 느낌이 아니라 var 느낌으로 해석...
print(data)