import sys
N = int(sys.stdin.readline())
a = []
for n in range(N):
    a.append(list(sys.stdin.readline().strip().split()))
a = sorted(a, key = lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(a[N-1][0])
print(a[0][0])
