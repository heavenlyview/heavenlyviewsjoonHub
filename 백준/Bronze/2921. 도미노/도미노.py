N = int(input())
sum = 0
for i in range(0, N + 1):   # 왼쪽
    for j in range(i, N + 1): # 오른쪽
        sum += i + j
print(sum)