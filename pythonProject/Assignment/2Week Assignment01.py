import turtle as t

#터틀 정사각형
t.shape('turtle')

t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)

#파일명을 turtle로 지정하면 함수명과 혼동되어 turtle 그래픽이 실행되지 않는다.

#터틀 직사각형
t.shape('turtle')

t.forward(400)
t.right(90)
t.forward(200)
t.right(90)
t.forward(400)
t.right(90)
t.forward(200)

#터틀 원
t.Pen('turtle')
t.circle(100)

t.done()