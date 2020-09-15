# 구글 입사 문제
'''
 1퉈 10000까지 8이라는 숫자가 총 명 번 나오는가 ?
 8이 포함되어 있는 숫자의 개수를 카운팅하는 것이 아니라 8이라는 숫자를 모두 카운팅해야 한다.
'''
result=0
for i in range(1,10000):
    result+=str(i).count('8')
print(result)
# 위에는 내가 푼거 내가 푼게 더 좋은듯


# 아래는 답지
count =0
for i in range(1,10000):
    for j in str(i):
        if j == '8':
            count +=1