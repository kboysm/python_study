import os
os.chdir('./파이썬파일이름변경/test') # 경로 변경
print(os.getcwd()) #현재 경로 출력
# for i in range(5): #파일 생성
#     os.mkdir("./dirNameupdate_test({})".format(i))

# for i in os.listdir():
#     print(i) 현재 경로의 디렉토리 리스트 출력

# for i in os.listdir():
#     os.rename(i , i.replace("_","-"))  파일명 전부 변경
# for i in os.listdir():
#     os.rename(i , "{}_{}".format(i.split('-')[1],i.split('-')[0])) 파일 -기준으로 쪼개서 앞 뒤 이름 바꾸기

'''
os.getcwd() : 현재 경로를 알려줌
os.listdir() : 해당 결로의 디렉토리 리스트를 불러옴
os.mkdir("fileName") : 해당 결로에 파일을 만듬
os.rename(현재파일네임,바꿀파일네임)
'''