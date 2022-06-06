import matplotlib.pyplot as plt
from sympy import maximum, minimal_polynomial
from user_math import USERm 
from numpy import arange
class MAIN(USERm):
    alpha = 0.5

    Minimum = [0,0]
    Maximum = [0,0]

    def __init__(self):
        pass
    def get(self):
        user = list(map(float, input().split()))
        if user: self.set_num(*user)
        self.alpha = float(input("움직임의 배수:"))
        self.draw()

    def draw(self):
        x = arange(-100, 100, 0.01)
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        
        # 그리드 추가
        plt.grid(color = "gray", alpha=.5,linestyle='--')

        # 범례 작성
        xylim = self.size()

        j = xylim[:]
        j = [(j[0][0],j[1][0]),(j[0][1],j[1][1])]
        j.sort(key=lambda x: (x[1])) #극소, 극대 정렬
        #print(j)
        self.Minimum = j[0]#작은건 극소
        self.Maximum = j[1]#큰건 극대
        #print(self.Minimum, self.Maximum)

        xa = self.addrange(xylim[0],0.05)
        ya = self.addrange(xylim[1],0.05)
        #print(xylim)
        plt.xlim(xa)
        plt.ylim(ya)
        plt.plot(x,self.a*x**3+self.b*x**2+self.c*x+self.d,label=f'y = {self.a}*x^3+{self.b}*x^2+{self.c}*x+{self.d}')
        plt.legend()

        x, y = self.Maximum #초기 위치 설정
        if(self.Maximum[0] < self.Minimum[0]): x += 0.01 #최댓값의 x값이 최솟값의 x 좌표보다 작다면 최솟값쪽으로 +0.01
        else: x -= 0.01 #최댓값의 x값이 최솟값의 x 좌표보다 크다면 최솟값쪽으로 -0.01
        y = self.f(x) #y값 옮기기

        safety = 0
        while(safety<=500 and y >= self.Minimum[1]+0.00001):
            plt.scatter(x,y) #점찍기
            x -= self.derivative(x)*self.alpha
            y = self.f(x)
            safety += 1
        plt.scatter(x,y)
        if safety == 500: print("연산이 500회가 넘어 자동으로 중지 되었습니다.")
        else: print(f"연산횟수:{safety}")
        print(f"최솟값으로 추정되는 좌표{round(x,5),round(y,5)}")
        plt.show()



if __name__ == '__main__':
    app = MAIN()
    while True:
        print("x^3, x^2, x, 상수항의 배수를 각각 공백을 기준으로 입력해 주세요")
        try:app.get()
        except: print("불가능합니다.")
        if 'a' == input("input 'a' to stop:"):break