T = int(input()) # 테스트 케이스 개수
for i in range(T):
    a, b = map(int, input().split()) # 주사위 2개 a, b
    print("Case {}:".format(i+1),a+b)