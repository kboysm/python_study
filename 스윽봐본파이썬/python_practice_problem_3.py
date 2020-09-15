b ={
    'name':'John',
    'phone':'01012345678',
    'email':'test@test.tes',
    'birth':11111
}
print(b['name'])
b['birth'] =101010
b['city']='Seoul'
print(b)

#삭제 명령어 del

del b['city']
print(b)