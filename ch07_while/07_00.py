# massage = input("who are you? : ")
# print(massage)

# prompt = 'hi'
# prompt += '\nwho are you?' #출력문에 문장을 더 추가하는 방법 +=
# prompt = input(prompt)
# print(f'hello {prompt}')

# toping = '추가할 토핑을 고르시오'
# while True:
#     tp = input(toping)
#     if tp == 'quit':
#         break
#     else:
#         print(tp)        

customer_age = '나이가 어떻게 되세요?'
while True:
    c_age = input(customer_age)
    if c_age == '0': #input은 기본 문자열이라서 0이라도 따옴표로 감싸줘야 함.
        break
    c_age = int(c_age)
    if 0 < c_age < 3:
        print("Free")
    elif 3 <= c_age < 12:
        print("10$")
    elif 12 <= c_age:
        print('15$')

