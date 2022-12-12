n=int(input(''))

num=[]

for i in range(n):
    N=list(map(int,input('').split()))
    for j in range(2):
        N.remove(max(N))

    num.append(max(N))
    N=[]

for i in range(n):
    print(num[i])