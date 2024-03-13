import matplotlib.pyplot as plt

fig, ax = plt.subplots() 

#좌표 만드는 또 다른 방법
# def plot(x, y,label):
#   ax.plot(x, y, label=label)

x1 = [1, 2, 3, 4]
y1 = [2, 3, 4, 6]
ax.plot(x1, y1, label='blue') #라인 특징 

x2 = [1, 2, 3, 4]
y2 = [1, 2, 3, 4]
ax.scatter(x2, y2, label='yellow') #점으로 표시 
# ax.plot(x2, y2, label='yellow') 

ax.set_title('Plot A and B') #그래프 이름 
ax.set_aspect('equal') 
ax.set_xlabel('BMI') #x축 이름 
ax.set_ylabel('Age')
ax.set_xlim(0,10) #x축 길이 (xlimit)
ax.set_ylim(0,10)
ax.legend() #x,y축 라인 특징 표시 
plt.savefig('plot.png') #해당 그래프 파일 다이랙트로 저장.
plt.show() #실행하면 그래프 보이게 해줌.