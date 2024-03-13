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
    'bro':'blue',
}
print(f'엄마가 좋아하는 색깔은 {family["mammy"]}입니다.')
#키-값 쌍 순회
for k,v in family.items():
    print(f'{k}가 좋아하는 색깔은 {v}입니다.')
#key정렬 = .key(): key 출력은 기본제공이라  .key()는 생략해도 됨.
for k in sorted(family):
    print(k)
#값 순회
for v in family.values():
    print(f'색 종류 : {v}')
#중복제거
for v in set(family.values()):
    print(v)

# alines = []
# for alien_number in range(10):
#     new_alien = {'color':'green','point':5,'speed':'slow'}
#     alines.append(new_alien)
# for alien in alines[:5]:
#     print(aline)
# print('...')
# print(f'Total number of aliens: {len(alines)}')

