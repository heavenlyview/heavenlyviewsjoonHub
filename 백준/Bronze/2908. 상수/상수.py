try: 
  a, b = input().split()

  a = int(a[::-1])
  b = int(b[::-1])

  if a > b:
    print(a)
  else:
    print(b)
except ValueError:
  print("예외가 발생했습니다")