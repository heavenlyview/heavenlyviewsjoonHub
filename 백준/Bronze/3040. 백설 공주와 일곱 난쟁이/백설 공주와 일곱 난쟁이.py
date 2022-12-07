height = []    # 키들을 리스트에 모두 입력 받는다.
for i in range(9): 
    height.append(int(input()))
for i in height: 
    for j in height:
        if sum(height) - i - j == 100 and i != j:# 키 합친 값 - 2명 키 뺀 값 == 100이라면
            height.remove(i) # 키 리스트에서 i를 빼줘
            height.remove(j) # 키 리스트에서 j를 빼줘
height.sort()     # 오름차순으로 정렬해줘       
for i in height:
    print(i)      # 다시 리스트 정렬된 값을 출력해줘