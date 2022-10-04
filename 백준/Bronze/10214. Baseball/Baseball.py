n = int(input())

result =[]
for i in range(n):
    y = 0
    k = 0
    for j in range(9):
        a, b= map(int, input().split())
        y += a
        k += b
    if y>k:
        result.insert(i,'Yonsei')
    elif y<k:
        result.insert(i, 'Korea')
    else:
        result.insert(i, 'Draw')

for i in range(n):
    print(result[i])