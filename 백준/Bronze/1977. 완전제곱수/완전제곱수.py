# M <= N

import math # 제곱근의 값을 반환하기 위해 사용(math.sqrt)

M = int(input())    # M과 N을 입력받는다.
N = int(input())

a = []
for i in range(M, N+1):
  if int(math.sqrt(i)) ** 2 == i: # 제곱근을 정수형으로 변환하고 다시 제곱한 값이
    a.append(i)                   # i와 같을 경우 완전 제곱수이기 때문에 리스트 a에 담기

if a:                             
  print(sum(a))                   # 완전제곱수의 합
  print(min(a))                   # 완전제곱수의 최소값
else:
  print(-1)                       # 없을 경우 -1 출력