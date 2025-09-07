# 파이썬 다운 생각
import this

# PEP를 따라가자.
# 클래스는 두 줄을 띄운다.
class A:

    # 내부에서 사용하는 인스턴스 속성 _,__을 이용하면 아래처럼 Name Mangling을 이용해서 새로운 변수를 생성함.
    # 메서드는 한 줄을 띄운다.
    def __init__(self):
        self.__a = 3
        self.__b = 4


class B(A):

    def __init__(self, a, b):
        super().__init__()
        self.__a = a
        self.__b = b


c = B(1, 2)
print(vars(c))

a = [1, 2, 3, 4]
# a가 비어있지 않다면 의 의미임.
if a:
    print("not empty")

# byte,str, unicode
# python version 2: str(8 bit),encode <--> decode unicode(유니 코드로 표현)
#                3: byte(8 bit)encode <-->  str(유니코드)
# python3에서는 byte와 str의 연산은 허용되지 않으나, python2에서는 str이 유니코드를 가지고 있다면 허용됨.


a = "한글"
b = a.encode()
print(type(a))
print(type(b))


def returnZeroIfBLK(a):
    if a == '':
        return 0
    return a


# 복잡한 표현식의 경우 헬퍼함수를 이용하자.
c = [2, '', '']
for i in range(3):
    c[i] = returnZeroIfBLK(c[i])
print(c)

# 슬라이싱할 수 있는 방법
q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(q[:3])
# -1:11 10:-2 9:-3
print(q[:-3])

# 슬라이싱 후에 대입하면 shallow copy가 됨.
# 하지만 int,str은 파이썬에서는 불변형이므로 변경시에 기존의 리스트의 변수가 변경되지 않고,
# 반면 list는 가변형이라 영향을 받는다.
# 객체의 참조가 변경이 된다.
copyQ = q[:3]
copyQ[2] = 13
print(q[:3])
print(copyQ)
copyQ2 = q[:]
# same
print("same" if copyQ2 == q else "not same")

# 슬라이싱 시 start,end,stride를 다 사용하면 오히려 가독성이 떨어진다.
print(q[::2])

# map과 filter를 이용해서 새로운 리스트를 만들기 보다는 리스트 컴프리헨션을 사용해야함
# 리스트에서 짝수인 수-> 제곱수를 새로 생성하는 예제
a = [1, 2, 3, 4]
b = [x*x for x in a if x % 2 == 0]
print(b)

# 리스트 컴프리헨션의 표현식을 두개를 초과하지 말자.
# 다중식에서의 리스트 컴프리헨션은 왼쪽->오른쪽으로 구성됨.
a = [[1, 2, 3, 4, 5]]
b = [x*2 for c in a for x in c]
print(b)

a = [[[1, 2, 3, 4, 5]]]
b = [x*2 for c in a for w in c for x in w] # 이렇게 쓰지 말라는 거
b=[]
for suba in a:
    for subaa in suba:
        b.extend(subaa)
print(b)

# 리스트 컴프리헨션은 입력값이 매우 많은 경우에 메모리가 터질 위험이 있으므로, 제너레이터를 이용해서
# iter로 동적으로 메모리를 생성하면 해당 문제를 해결할 수 있음.
numsCom = [x for x in range(10**8)]
numsGen = (x for x in range(10**8))
print(next(numsGen))  # 0 --> 이 때마다 동적으로 생성된다.
print(next(numsGen))  # 1
print(next(numsGen))  # 2

# 리스트를 순회하면서 현재의 위치,value를 알고 싶다면 enumerate로 감싸서 사용하자
a = [1, 2, 3, 4, 5]
for idx,value in enumerate(a):
    print('%d %d' %(idx,value))