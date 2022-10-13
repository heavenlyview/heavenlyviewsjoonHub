book_sum = int(input())  # 10권 가격 다 더한 값 입력받기

for i in range(9): # 9권 책 가격 빼기
  book_sum -= int(input())  # 맨 첫줄에 입력받는 값과 다르다! 이건 9번 입력해서 빼야한다 
print(book_sum)