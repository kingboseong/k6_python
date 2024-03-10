name = ['kim', '유미진', '김진성', '김들레']
print(f'{name[0].title()}은 {name[1]}과 서울여행 중 {name[2]}를 만나 {name[-1]}에 대한 이야기를 했습니다.')

name1 = ['자전거','기차','자동차']
print(f'내가 제일 좋아하는 교통수단은 {name1[0]}입니다.')

partylist = ['하성진','서지성','안찬희','정재환','배정현']
print(f'{partylist[:]}을 파티에 초대합니다.')
partylist[0] = '유미진'
print(f'{partylist[:]}을 파티에 초대합니다.')
print(f'{partylist[:]}님 더 큰 테이블로 자리를 옮겨주세요.')
partylist.insert(0,'김경환')
partylist.insert(2,'반민호')
partylist.append('김민국')
print(f'{partylist}을 파티에 초대한다.')
partylist.pop()
partylist.pop()
del partylist[0]
print(partylist)

travellist = ['도쿄','괌','미국','홍콩','알프스']
print(sorted(travellist))
print(travellist)
travellist.reverse()
print(travellist)
travellist.reverse()
print(travellist)
travellist.sort()
print(travellist)
print(f'저녁 식사에 초대할 인원은 {len(partylist)}명 입니다.')



