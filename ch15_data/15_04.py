import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# Set Korean font
plt.rcParams['font.family'] = 'NanumBarunGothic'

x1 = 50
y1 = 30

x2 = 70
y2 = 50

x3 = 20
y3 = 70

fig, ax = plt.subplots()
ax.scatter(x1,y1, label="홍길동", color='red')
ax.scatter(x2,y2, label="이순신", color='blue')
ax.scatter(x3,y3, label="감강찬", color='yellow')

ax.set_xlabel('국어')
ax.set_ylabel('영어')
ax.set_xticks([10,20,30,40,50,60,70,80,90,100])
ax.set_yticks([10,20,30,40,50,60,70,80,90,100])

plt.legend()
plt.show()
