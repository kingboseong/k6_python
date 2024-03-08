data = []
for _ in range(10):
    data.append(int(input()) % 42)

answer = []
for d in data:
    if d not in answer:
        answer.append(d)

print(len(answer))
