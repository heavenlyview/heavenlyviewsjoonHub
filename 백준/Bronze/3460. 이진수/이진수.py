t=int(input())
for _ in range(t):
  n=bin(int(input()))[2:] # 앞에 두자리 잘라주기
  for i in range(len(n)):
    if n[-i-1]=='1': #문자열 거꾸로 탐색
      print(i, end=" ")