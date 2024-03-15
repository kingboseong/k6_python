import datetime

from datetime import datetime as dt

#문자열을 데이터 타입으로 바꿈
today = dt.strptime('2024-03-15', '%Y-%m-%d')

print(today, type(today), type('2024-03-15'))

print(today + datetime.timedelta(days=3))
