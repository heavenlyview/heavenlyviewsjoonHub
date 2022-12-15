for _ in range(int(input())):
    l = []
    s = 0
    m = 0
    l = list(map(int, input().split()))
    l.sort()
    for i in l:
        if i % 2 == 0: 
            s += i
            if m == 0: m = i
  
    print(s, m)