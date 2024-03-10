magicians = ['alice','david','carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"i can't wait to see your next trick, {magician.title()}\n")
print('Thank you, everyone. That was a great magic show!\n\n')

pizzas = ['cheecs','meet','potato']
for pizza in pizzas:
    print(f'나는 {pizza}pizza를 좋아햐')
print(f'{pizza}pizza들은 내가 좋아하는 pizzas입니다.')

squares = []
for number in range(1,11):
    squares.append(number**2)
print(squares)


num = range(1,1000000)
# print(num)
print(min(num))
print(max(num))
print(sum(num))
# for num in range(1,21,2):
#     print(num)
# for num in range(3,31,3):
#     print(num)
# for square in range(1,11):
#     print(square**3)
squares = [value**3 for value in range(1,11)]
print(squares)

lst = [1,2,3,4,5,6,7]
print(lst[:])
pizzas = ['cheecs','meet','potato']
friend_pizzas = pizzas[:] #friend_pizzas 하면 append한거까지 똑같아짐.
pizzas.append('newpizza')
print(pizzas)
print(friend_pizzas)
for i in friend_pizzas:
    print(f'내 친구가 가장 좋아하나느 피자는 {i}입니다.')
for j in pizzas:
    print(f'내가 좋아하는 피자는{j}입니다.')

foods = ('apple','banana','curry','dimsum','drink')
# foods[2] = 'fooog' 튜플은 불변리스트라서 리스트 변경 불가
for food in foods:
    print(food)
foods = ('annk','bommg','curry','dimsum','drink') #튜플 변경하기
for food in foods:
    print(food)