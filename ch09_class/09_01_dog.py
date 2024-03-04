class Dog:
    """개 클래스"""

    def __init__(self, name, age):
       #속성 > 자바의 클래스 내 field와 같은 역할
       self.name = name
       self.age = age

    def sit(self): # 모든 클래스의 메서드는 self를 포함(지정)하고 있음. 여기서 self는 아래에 my_dog.sit()에서 my_dog임.
      print(f"{self.name} is 앉기")

my_dog = Dog('willie', 6) #생성자 호출 > 인스턴스 생성 > __init__함수(위에 self, name, age함수)가 자동으로 출력 / self는 필수임.
my_dog.sit()
print(f"개 이름은 {my_dog.name} + {my_dog.age}.")

your_dog = Dog('Lucy', 3)
your_dog.sit()
print(f"너의 개는{your_dog.name}")







# 클래스 내에서는 self.
# 클래스 밖에서는 변수.

###
# class Dog{
#    #파이썬은 이런 필드가 없음.
#    string name:
#    int age:
#    public Dog(String name, int age){
#       thid.name = name;
#       this.age = age
#    }
# }