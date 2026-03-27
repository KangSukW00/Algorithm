test_count = int(input())
answers = []

for _ in range(test_count):
    a, b = input().split()
    num_list = list(str(int(a) + int(b)))

    while '2' in num_list or '3' in num_list:
        for i in range(len(num_list)):
            if num_list[-(i + 1)] == '2':
                num_list[-(i + 1)] = '0'
                if i + 2 <= len(num_list):
                    num_list[-(i + 2)] = str(int(num_list[-(i + 2)]) + 1)
                else:
                    num_list.insert(0, '1')

            if num_list[-(i + 1)] == '3':
                num_list[-(i + 1)] = '1'
                if i + 2 <= len(num_list):
                    num_list[-(i + 2)] = str(int(num_list[-(i + 2)]) + 1)
                else:
                    num_list.insert(0, '1')

    result = int(''.join(num_list))
    answers.append(result)

for x in answers:
    print(x)