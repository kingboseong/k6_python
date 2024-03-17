class Restaurant:
    def __init__(self, rname, rtype):
        self.restaurnat_name = rname
        self.cuisine_type = rtype

    def describe_restaurant(self):
        print(f"{self.restaurnat_name} 에 오신걸 환영합니다.")

    def open_restaurant(self):
        print(f"{self.cuisine_type}전문")

#서브 클래스 만드는 연습 계속하기
class IceCreamStand(Restaurant):
    def __init__(self, rname, rtype, flavors):
        super().__init__(rname, rtype)
        self.flavors = flavors

    def show_flavors(self):
        print(f"맛이 {self.flavors}")


new_rest = Restaurant('보성식당', '양식')
print(f"레스토랑 이름과 타입 {new_rest.restaurnat_name} {new_rest.cuisine_type}")
new_rest.describe_restaurant()
new_rest.open_restaurant()

my_rest = Restaurant('나만의식당','중식')
my_rest.describe_restaurant()
my_rest.open_restaurant()
    

