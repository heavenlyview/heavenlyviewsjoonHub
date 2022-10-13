while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:  # 0 두 개이면 무한루프 그만 돌려줘
        break;
    else:
        print(a+b)