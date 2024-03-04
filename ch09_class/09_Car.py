class Car:
    """자동차 클래스"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        

    def get_descriptive_name(self):
        long_name = f"{self.year}{self.make}{self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"이 차의 주행거리는 {self.odometer_reading}")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("주행기록계를 줄일 수 없다.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23 
my_new_car.read_odometer()
my_new_car.update_odometer(11)
my_new_car.read_odometer()
my_new_car.increment_odometer(23_500)
my_new_car.read_odometer()