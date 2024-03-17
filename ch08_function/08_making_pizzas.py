import pizza #파일 이름의 첫 글자가 숫자면 오류가 남
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'peppers', 'cheese')
#==
import pizza as p #클래스 이름 간결하게 바꾸기  = as
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'peppers', 'cheese')
