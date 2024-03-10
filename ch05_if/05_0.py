alpabat_list = ['A','B','C']
alpabat = 'D'
if alpabat not in alpabat_list:
    alpabat_list.append(alpabat)
print(alpabat_list)

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car =='subaru')

print("\nIs car == 'audi'? I predict False.")
print(car =='audi')

tree = 'sonamu'
print(tree == 'SONAMU'.lower())

alien_color = 'yellow'
if alien_color == 'green':
    print('player plus point 5')
elif alien_color == 'red':
    print('player plus point 10')
elif alien_color == 'yellow':
    print('player plus point 15')
age = 18
if age < 2:
    print('baby')
elif 2 <= age  < 4:
    print('toddler')
elif 4 <= age < 13:
    print('kid')
elif 13 <= age < 20:
    print('teenager')
elif 20 <= age < 65:
    print('adult')
else:
    print('elder')

user_names = ['admin','bosung','jimin','one','zeor']

for user_name in user_names:
    if user_name == 'admin':
        print("hi admin")
    else:
        print(f"{user_name}님 안녕하세요.")
user_name = []
if user_name:
    for user_name in user_names:
        print('사용자 출력중')
    print('사용자 출력완료')
else:
    print('사용자를 추가하세요.')

current_users = ['A','B','C','E','F']
new_users = ['A','D','B']

for new_user in new_users:
    if new_user not in current_users:
        print(f"{new_user}사용가능")
    elif new_user in current_users:
        print(f'{new_user}닉네임 변경요망')
        
    