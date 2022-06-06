from turtle import circle
from sympy import * 

class USERm:
    a = 1
    b = 2
    c = 0
    d = 0
    def set_num(self, *num) -> None:
        self.a = num[0]
        self.b = num[1]
        self.c = num[2]
        self.d = num[3]

    def f(self, x) -> float:
        return self.a * x**3 + self.b * x**2 + self.c * x + self.d

    def derivative(self, A:float) -> float:
        x, a, h = symbols('x, a, h')
        fx = self.a * x**3 + self.b * x**2 + self.c * x + self.d
        fxa = fx.subs({x: a})    # 함수 f(x) 에 x=a 를 대입
        fxh = fx.subs({x: a + h})    # 함수 f(x) 에 x=a+h 를 대입
        f = Limit((fxh-fxa)/h, h, 0).doit() # 정의를 이용하여 극한값(=미분계수) 계산
        return float(f.subs({a:A}))    
    def size(self) -> tuple:        
        #(x1 < x2),(y1 < y2)
        x = Symbol('x')#
        f = self.a * x**3 + self.b * x**2 + self.c * x + self.d#함수 f(x)를 정의한다.
        
        derivative1 = Derivative(f, x).doit()#도함수 f'(x) 를 derivative1 이라 하자
        critical = solve(derivative1)#f'(x)=0 의 근을 critical 에 저장
        critical.sort()#critical을 오름차순으로 정렬
        y = tuple(map(float,[f.subs({x:critical[0]}), f.subs({x:critical[1]})]))
        return(float(critical[0]),float(critical[1])),y
    
    def addrange(self,li:list, num:int=1):
        addlist = [-num,num]
        li = list(li)
        li.sort()
        return (li[i]+addlist[i]for i in range(len(li)))