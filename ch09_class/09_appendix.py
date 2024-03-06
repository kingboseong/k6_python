class Shape:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

###getter, setter를 정의하는데 decorator 사용
@property #decorator for getter
def get_base(self):
    return self.__base 

@property #decorator for getter
def get_height(self):
    return self.height 

@height.setter
def height(self, value):
    self.height = value

def get_data():
    return 1,2,3

_,a,b = get_data() #첫번째 값은 무시하겠다 = _
print(f"{get_data}")

a=[1,2,3]
b=[11,22,33]
mylist = [*a,*b] #병합
print(mylist)

c=['a','b']
z=zip(a,c) #zip = 지퍼처럼 하나하나 번갈아갈면서 출력해줌
print(list(z))

