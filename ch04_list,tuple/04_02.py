def test():
    return(10,20)

a, b = test() #tuple 값을 리턴.
print(f"a = {a}, b = {b}")
lst = ['a','b','c','d']
for i, value in enumerate(lst): #enumerate()함수(배열이나 리스트에서 많이 사용됨)가 tuple을 리턴한다.
    print(f"i = {i}, value = {value}")

