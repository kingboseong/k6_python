def greet_user(username): #usernam은 스트링은 immutable
    """단순한 인사말을 표시합니다."""
    print(f"HELLO!, {username.title()}")
    username ='kim'

input_name = 'jesse'
greet_user(input_name) #함수 호출
input_name = 'kim' #값 변경이 아니라 변수를 다시 설정하는 것.
print(input_name)
# help(greet_user)
# print(greet_user.__doc__)

def describe_pet(animal_type, pet_name='dog'): #기본값 = default parameter = 전달할 파라미터가 없으면 여기서 선언한 값을 사용하겠다
    """반려동물 정보 표시"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry') 
# describe_pet(pet_name = 'harry') #동등한 함수 호출(위 줄과 같음)
describe_pet(pet_name = 'harry', animal_type = 'hamster') #순서대로 안하고 싶을 때 = 키워드 인수(198p.)

def get_formatted_name(first_name, last_name, middle_name):
    """ 실제 이름 형식 """
    if middle_name: #빈스트링이면 False로 간주
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)
