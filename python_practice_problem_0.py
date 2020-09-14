# print('''\
#     *
#    * *
#   *   *
#  *     *
# *********\
# ''') shell에서는 에러가 안나는데 vscode에서는 에러발생

# a=input('a : ')
# b=input('b : ')
# print('a+b={}'.format(int(a)+int(b)))

# 위의 코드를 한줄로 변경

print('a + b ={}'.format(int(input('a: '))+int(input('b: '))))