# 이중 for

# for dan in range(2,10):
#     print("{}단 ".format(dan))
#     for i in range(1,10):
#         print("{}x{}={}".format(dan,i,dan*i))

result=''

for dan in range(2,10):
    result += "\n{}단\n ".format(dan)
    for i in range(1,10):
        result +="{}x{}={}\n".format(dan,i,dan*i)

print(result)

# print 를 한번만 호출하게 하여 실행 속도를 향상 시킴