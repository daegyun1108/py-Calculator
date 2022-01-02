from sympy import * 
from sympy.plotting import plot
import numpy as np

init_printing(use_latex='mathjax')
x, y, n = symbols('x y n')

while 1:
    q = int(input("0은 종료, 1은 계속 : ")) 
    print()

    if q == 0:
        print("종료")
        break
        
    elif q == 1:
        print("무엇을 하실건가요?")
        a = int(input("1은 함수값, 2은 미분, 3은 적분, 4는 최대공약수와 최소공배수, 5는 수열 : "))
        print()

        if a == 1:
            f = input("함수 입력 : ")
            print()
            print("solve : {}".format(solve(f)))
            plot(f)

        elif a == 2:
            f = input("함수 입력 : ")
            print()
            f_prime = Derivative(f, x).doit()
            pprint("f의 도함수: {}".format(f_prime))
            print("solve : {}".format(solve(f_prime)))
            plot(f_prime)
            print()

            b = int(input("이계도함수를 구하려면 0, 아니면 1 : "))

            if b == 0:
                f_prime2 = Derivative(f_prime, x).doit()
                pprint("f의 이계도함수: {}".format(f_prime2))
                print("solve : {}".format(solve(f_prime2)))
                plot(f_prime2)
                print()

            elif b == 1:
                pass

        elif a == 3:
            b = int(input("부정적분은 0, 다변수 부정적분은 1, 정적분은 2 : "))

            if b == 0:
                f = input("함수 입력 : ")
                print()
                f_Integral = integrate(f, x)
                print("부정적분 값 : {} + C (단, C는 적분 상수)".format(f_Integral))
                print("적분 상수 C를 무시하고 그립니다.")
                print()
                plot(f_Integral)
                print()

            elif b == 1:                                 
                f = input("함수 입력 : ") # x, y 함수
                print()
                c == int(input("0은 x에 대해, 1은 y에 대해 : "))

                if c == 0:
                    f_Integral = integrate(f, x)
                    print("부정적분 값 : {}".format(f_Integral))

                elif c == 1:
                    f_Integral = integrate(f, y)
                    print("부정적분 값 : {}".format(f_Integral))
                print()

            elif b == 2:
                f = input("함수 입력 : ")
                z1 = int(input("범위 1 : "))
                z2 = int(input("범위 2 : "))
                F = integrate(f, (x, z1, z2))
                print("정적분 값 : %s" %F)
                print()
                
        elif a == 4:
             lst = list(map(int, input("공백을 두고 입력하세요 : ").split())) 
             print() 
 
             def Euclidean(a, b): 
                 while b != 0:
                     a, b = b, a%b 
                 return a 

             gcd_lst = lst[0] 
             lcm_lst = lst[0]
             for i in range(len(lst)): 
                 gcd_lst = Euclidean(gcd_lst, lst[i])
             print("최대공약수는 {}".format(gcd_lst), end = ', ')

             for i in range(len(lst)):
                 gcd_lst = Euclidean(lcm_lst, lst[i])
                 lcm_lst = lcm_lst * lst[i] // gcd_lst
             print("최소공배수는 {} 입니다.".format(lcm_lst))
             print()
        
        elif a == 5:
             b = int(input("0은 등차수열, 1은 등비수열, 2는 파보나치수열 : "))

             if b == 0:
                 a1, a2 = map(int, input("공백을 두고 첫번째 항과 두번째 항을 입력하세요 : ").split())
                 print()
                 d = abs(a1 - a2) 
                 s = expand(a1 + (n - 1) * d)
                 print("일반항 : {}".format(s))
                 print("공차 : {}".format(d))
                 print()
             
             elif b == 1:
                 a1, a2 = map(int, input("공백을 두고 첫번째 항과 두번째 항을 입력하세요 : ").split())
                 print()
                 r = round(a2 / a1, 2)
                 s = a1 * r ** (n - 1)
                 print("일반항 : {}".format(s))
                 print("공비 : {}".format(r))
                 print()

             elif b == 2:
                 print("파보나치 수열")
                 t = int(input("수 : "))
                 print()
                 u = np.matrix( [ [1, 1], [1, 0] ] )
                 print((u**t)[0, 1])

                 lst = []
                 for i in range(1, t + 1):
                     lst.append((u**i)[0, 1])
                  
                 for j in lst:
                     print(j, end = ' ')
                 print() 
