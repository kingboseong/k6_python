# def get_formatted_name(first_name, last_name):
#     """실제 이름 반환"""
#     full_name = f"{first_name}{last_name}"
#     return full_name.title()

# #무한 루프입니다.
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     if f_name =='q':
#         break
#     l_name = input("Last name: ")
#     if l_name =='q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    """빈 리스트일때 까지 출력"""

while unprinted_designs: #빈 리스트이면 false =>while문 탈출
    current_design = unprinted_designs.pop() #pop 한개씩 삭제
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def modify_string(s): ##스트링 값을 전달받음
    ##immutable변수는 튜플, 숫자, 스트링, 불리언 형태이다
    s = s + "world" #변수 s는 원래 변수가 가리키는 주소와 다름
    print(s)

    st = "hello"
    modify_string(st)
    print(st) ##출력 결과가 hello => 변경안됨
