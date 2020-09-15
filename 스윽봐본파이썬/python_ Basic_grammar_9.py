# if
num = 1

if num > 0:
    print(1)
elif num == 0:
    print(2)
elif num < 0:
    print(3)
else:
    print(4)

#elif정도만 외우고 조건 바로 뒤에 콜론(:)이 붙는다 들여쓰기 신경쓰면 다른 언어의 문법과 매우유사

#예제
'''
def robot_action(x):
    x=int(input("x:"))

    if x==0:
        print('우회전')
    elif x >1:
        print('점프')
    elif x<-1:
        print('유턴')
    else:
        print('전진')
'''