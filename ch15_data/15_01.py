import matplotlib.pyplot as plt

x = list(range(1,101))
square = [i**2 for i in x]

#1
# fig, ax = plt.subplots()
# ax.scatter(x, square, c=square) #scatter는 점으로 표시됨
# ax.set_title('Square', fontsize=30)
# ax.set_xlabel('X', fontsize=20)
# ax.set_ylabel('Y', fontsize=20)
# ax.tick_params(labelsize=10)
# plt.style.use('seaborn-v0_8-pastel')
# # for s in plt.style.available: #seaborn 의 다양한 버전들
# #     print(s)
# ax.ticklabel_format(style='plain')
# plt.show()

#2  (컬러맵(424p)= 3차원 그래프 시각화 할 때 유용함.)
plt.scatter(x,square,c=square,cmap=plt.cm.Blues)
plt.colorbar()
plt.savefig('colorbar.png')
plt.show()