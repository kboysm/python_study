# a=input('원하는 정수를 넣어주세요:')
# print(a)
 # shell 에서는 _를 사용하면 마지막으로 나온 결과를 확인할 수 있음

# numbers=input('숫자 여러 개를 공백으로 구분해서 넣어주세요:').split(" ") # 애초에 데이터를 받을 때 input에서 split을 사용할 수 있음
# print(numbers)
a,b,c,d=input('숫자 4개를 공백으로 구분해서 넣어주세요:').split(" ") # 애초에 데이터를 받을 때 input에서 split을 사용할 수 있음
e=int(a)+int(b)+int(c)+int(d)
print('{},{},{},{}의 합은 {}이다'.format(a,b,c,d,e))
#int() : 인트형으로 강제형변환
#str() : 문자열로 강제형변환
#float() : 부동소수점으로 강제형변환