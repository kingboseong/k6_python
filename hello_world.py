print("hello world")
name='ada lovelace'
print(name.upper())
print(name.title())
first_name='ada'
last_name='lovelace'
full_name=f"{first_name}\t{last_name.title()}!"
print(full_name)
print('lanuage: \npython\tjava')
last_name=' lovelace '
last_name.strip()
print(last_name)

person_name = 'kim boseong'
print(f"안녕하세요 {person_name.upper()}\t{person_name.lower()}\t{person_name.title()}, 오늘 파이썬 배우 보는게 어떨까요?")

print(12_000_00_000)

print("________________")
print("\n")

bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-2])
message=f"bicycles was a {bicycles[0].title()}."
print(message)
motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles.remove('ducati')
motorcycles.append('GM')
print(motorcycles)
motorcycles.insert(1, 'Samcheonri')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles.pop()
print(motorcycles)
popped_motor=motorcycles.pop()
print(motorcycles)
print(popped_motor)
print(f'the last owned motor was a {popped_motor.title()}.')
print("________________")
print("\n")
cars=['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(cars)
print(len(cars))
print((cars[-1]))
print("\n")
cars=['bmw', 'audi', 'toyota', 'subaru']
for car in cars: #확장형 for 문
    print(car)
    print(f'mycar is a {car}')
print('리스트 출력 완료')
for car2 in cars:
    print('my car\n')
    for c2 in cars:
        print('2번째 for문')
print("for문 종료")


