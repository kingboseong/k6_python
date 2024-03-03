
for value in range(6):
    print(value)
numbers = list(range(1,10,2))
print(numbers)

number_set = {}
squares = []

for value in range(1, 11):
    # square = value ** 2  -> 가능하면 라인 수를 줄여라.
    squares.append(value ** 2)

print(squares)
print(value)

# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2) 
#파이썬은 아래 코드처럼 줄이는 것을 좋아함 , 같은 출력값.
squares = [value ** 2 for value in range(1, 11)] #list comprehension = 리스트를 for 문으로 만들어 주는 문법
print(squares)
print(squares[5::-2]) #slice = 전체 중에서 일부만 썰어오는 문법. [] 괄호안에 오는 값 매우 다양하니 구글링해서 익히기.

a = [1,2,3,4]
b = [3,4]
c = a + b
print(c)

m = [[1,2,3],[4,5,6],[7,8,9]]
print(m[2][0])

a = [10,20,30,40,50]

b = a #리스트복사 = shallow copy
a[0] = 100
print(b)

b = a[:] #리스트복사 = deep copy
a[0] = 100
print(b)

plasyers = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in plasyers[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #[:]있으면 deep copy / [:]없으면 shallow copy
my_foods.append('cannoli')
print(my_foods)
print(friend_foods)

dimensions = (10, 20, 30, 40, 50)
# dimensions[0] = 30
print(dimensions)
for dimension in dimensions:
    if dimension > 10:
        print(dimension)
    print(dimension)

dimensions = (200, 50)



