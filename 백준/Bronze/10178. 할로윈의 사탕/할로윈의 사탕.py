T = int(input()) # 테스트 케이스 개수
# 사탕의 개수 c, 형제의 수 v
for i in range(T): 
  c, v = map(int, input().split()) # 사탕 개수, 형제 수 차례대로 입력
  print('You get {0} piece(s) and your dad gets {1} piece(s).'.format(c//v, c%v))