def make_pizza(*toppings): #tuple로 받은 것
    """요청받은 토핑 리스트를 출력합니다."""
    print("\nMaking a pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mkushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **uset_info):
    """사용자 딕셔너리"""
    uset_info['first_name'] = first
    uset_info['last_name'] = last
    return uset_info

uset_profile = build_profile('albert', 'einstein', location='princeton',field='physics')
print(uset_profile)