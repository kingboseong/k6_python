#복습
import matplotlib.pyplot as plt



x1 = list(range(5))
y1 = [i**2 for i in x1]

x2 = list(range(5))
y2 = [i**3 for i in x2]

fig, ax = plt.subplots()
ax.scatter(x1,y1, label="AAA", color='red')
ax.plot(x2,y2, label="BBB", color='blue', linewidth=5)

ax.set_title('AAA vs BBB')
ax.set_xlabel('x1')
ax.set_ylabel('y1')
ax.set_xticks([0,1,2,3,4])

#legend() = label표시해줌
plt.legend()
plt.show()