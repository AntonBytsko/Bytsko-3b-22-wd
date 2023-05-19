def check_num(num):
    remains = num % 2
    if remains == 0:
        result = 'Четное'
    else:
        result = 'Не четное'
    return result


print(check_num(2))
