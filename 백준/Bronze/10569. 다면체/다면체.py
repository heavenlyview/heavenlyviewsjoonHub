T = int(input()) # 자연수 T
for i in range(T):
    V, E = map(int, input().split()) # V = 꼭짓점 개수, E = 모서리 개수
    print(E - V + 2) # 꼭짓점의 수 - 모서리의 수 + 면의 수 = 2