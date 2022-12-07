a = []
K = int(input())
for i in range(K):
    num = int(input())
    if num == 0:
        a.pop()
    else:
        a.append(num)
print(sum(a))