T = int(input())

for i in range(T) :
  s = int(input())   # 자동차 가격 s

  n = int(input())   # 해빈이가 구매하려고 하는 서로 다른 옵션 개수 n
  if n == 0 :        # 옵션 개수가 0이면
    print(s)         # 자동차 가격 s를 출력해줘
  else :             # 옵션 개수가 0이 아니라면
    option = 0       # 0을 option이라는 변수에 할당하고
    for j in range(n): # 옵션 개수 n으로 for문을 돌린다
      q, p = map(int, input().split()) # q: 해빈이가 사려하는 특정 옵션 개수, p: 해당 옵션 가격
      option += q * p

    print(s + option)  # 자동차 가격에 옵션을 더한 값
    
