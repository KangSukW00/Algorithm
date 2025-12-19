start_num = int(input())

longest_sequence = []

# 두 번째 숫자를 1부터 입력받은 숫자까지 모두 시도
for second_num in range(1, start_num + 1):
    current_sequence = [start_num]
    current_sequence.append(second_num)

    index = 1
    while True:
        # 앞의 숫자에서 뒤의 숫자를 뺌
        next_val = current_sequence[index - 1] - current_sequence[index]
        
        if next_val < 0:
            break
            
        current_sequence.append(next_val)
        index += 1

    # 현재 만든 수열이 지금까지 찾은 가장 긴 수열보다 길다면 갱신
    if len(longest_sequence) < len(current_sequence):
        longest_sequence = current_sequence

# 결과 출력
print(len(longest_sequence))
for num in longest_sequence:
    print(num, end=' ')