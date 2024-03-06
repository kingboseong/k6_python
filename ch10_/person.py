class Person:
    count = 0 ###클래스 변수
    def __init__(self,name,age, address):  #생성자 역할
        self.name = name
        self.age = age
        self.address = address
        self.weight = [65,67,70,71]     #공개(public) 속성
        self.height = 1.70  #__ ~~ private 속성
        print("{}객체가 생성됨".format(self.name))
        Person.count += 1 ###클래스 변수를 증가

 #call, getitem 많이 씀.중요함.강조.
    # def __call__(self):
    #     return self.weight / (self.height**2)

    # def __len__(self):
    #     return len(self.weight)

    # def __str__(self): #Person은 객체, 출력 시 필요한 것은 스트링
    #     return "{}\t{}\t{}".format(self.name, self.age, self.address)

    # def __eq__(self, other):
    #     return self.address == other.address
        

    @classmethod ###decorator / 자바에서는 annotation(자바 컴파일러한테 알린다.)
    def printing(cls): ###cls(class) 고정. self아님
        print("객체수는 {}".format(cls.count))

    def __getitem__(self, index):
        return self.weight[index]
    
    def __del__(self): #자바의 가비지 컬랙션 느낌 
        print("객체 {}이 소멸됨".format(self.name))

Person('guest',11,'jeju') #생성되자 마자 소멸됨. 왜냐면 가르키는 변수가 없기 때문에 가비지 컬렉션이 수거해감.

new_person = Person('kim',28,'busan')
other_person = Person('hong', 23, 'busan')  
Person.printing() ###클래스 매소드 호출

print(f'person 객체의 나이는**{new_person.age:5}***')
print("객체의 타입은{}".format(isinstance(new_person, Person))) #isinstance = 왼쪽에 있는 놈이 오른쪽에 있는 놈의 객체냐,아니냐(boolean)
print(f"현재 체중은 {new_person[2]}")
print(f"{Person.count} 객체가 생성됨") ##Person. 자리에 new_person, other_person 둘다 됨. person객체들이 공유함

# print(f"체질량은 {new_person()}") ###__call__() 함수가 호출
# print(new_person == other_person) # def __eq__(self, other):  함수가 호출됨.
# print("이 사람은 {}".format(new_person.name))
# print(f"몸무게는 {new_person.weight}")
# print("시력은 {}".format(new_person.__vision))
# new_person.show_person_vision() // 시력 출력 함수였는데 지움

# print(new_person)
# print(str(new_person))
# print(new_person.__str__()) #print(이 괄호 안에는 string을 요구함 -> str 이라서 오류 없이 출력.)
# print(str(new_person))        
# print(new_person.str()) #오류!! 괄호안에는 함수가 들어가야 함?

# print(f"리스트 길이 {len(new_person)}") #위에     def __len__(self): 함수 호출됨.

# my_list=[1,2,3,4]
# print(len(my_list))






