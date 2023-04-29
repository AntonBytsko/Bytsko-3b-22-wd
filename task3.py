def check_num(num):
    remains = num % 2
    if remains == 0:
        result = 'Четное'
    else:
        result = 'Не четное'
    return result

print(check_num(2))

for i in range(1,10 + 1):
    if i == 4 or i == 5:
        pass
    else:
        print(i)