import turtle as t # as 뒤에 t를 붙였는데 t라는 별칭을 붙여 사용하겠다는 의미

# 정사각형 그리기
for i in range(4):
    t.forward(100) #t.fd()
    t.left(90) # 90도 만큼 꺽어라
print(t.pos()) # t의 위치를 반환 x,y축

t.up() # pen을 그래프에서 때라는 의미
t.goto(200,0)
t.down()

#평행사변형
for i in range(2):
    t.fd(120)
    t.left(120)
    t.fd(80)
    t.left(60)

t.up() 
t.goto(-200,0)
t.down()

#별 모양
    
for i in range(5):
    t.fd(100)
    t.left(360*2//5)

t.up() 
t.goto(0,300)
t.down()

#기하학적 도형

t.color('red','yellow')
t.begin_fill()

while(True):
    t.fd(100)
    t.left(170)
    x,y=t.pos()
    if int(x) == 0 and int(y) == 300:
        break
t.end_fill()
t.done()
