'''
일반적인 문자열을 입력하면 입력한 내용을 세 번씩 프린트함(공백)
help를 입력하면 '에코'문구가 떠야 함
quit를 누르면 진짜로?(y/n) 문구를 띄움
y를 누르면 종료 n을 누르면 계속 실행
'''
# 내가 한거
while(True):
    data1=input('문자열:')
    if data1 == 'help':
        print('echo')
    elif data1 == 'quit':
        result=input('진짜로?(y/n)')
        if result =='y':
            print('종료')
            break
    else:
        for i in range(3): #여기 부분에서 내가 아직 파이썬에 익숙하지 않다는게 느껴짐
            print(data1)

# 답지
# while(True):
#     input1 = input('> ')
#     if input1 == 'help':
#         print('~~')
#     elif input1 == 'quit':
#         input2 = input('정말 종료하시겟?')
#         if input2 == 'y':
#             break
#     else:
#         input1 = input1 + '  '
#         print(input1 *3)