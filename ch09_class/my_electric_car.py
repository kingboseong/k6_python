from Car import ElecticCar

my_leaf = ElecticCar('nissan', 'leaf', 2024)
print(f"전기차는 {my_leaf.get_descriptive_name()}")
print(f"전기차는 {}".format(my_leaf.get_descriptive_name))
my_leaf.