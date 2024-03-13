alien = {}
alien['color'] = 'green'
alien['points'] = 5
print(alien['color'])
aline = {'color':'red'}
print(aline['color'])
#해당 키-값이 없을 때
speed_value = alien.get('speed', 'No speed value assigned') 
print(speed_value)

MyBro = {'first_name':'KIM','age': 25 , 'city':'busan'}
print(MyBro)
print(f'내 동생이 사는 곳은 {MyBro["city"]}입니다.')
family = {
    'daddy':'blue',
    'mammy':'pink',
    'me':'red',
    'bro':'skyblue',
}
print(f'엄마가 좋아하는 색깔은 {family["mammy"]}입니다.')