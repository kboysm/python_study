 # range
'''
리스트를 자동으로 생성해 주는 생성기 range
for문에서 사용되는걸로 추정
range(시작 숫자,끝 숫자,연산할 숫자)
끝 숫자는 생략 불가 그 외 생략 가능 default (시작 :0, 연산 :1)
'''

# for i in range(2,10,2): #시작 숫자 2 , 끝숫자 10 ,연산 숫자 2 : 끝 숫자까지 출력이 안됌
#     print(i)

#문제 구구단 2단 출력
for i in range(1,10,1): # 답지에서는 1,10 으로 했음 디폴트가 1이라서 안써도 되는거 같음
    print('2 x{} = {}'.format(i ,2*i))