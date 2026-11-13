def digit_sum(number):
    if number < 10:
        return number
    return number % 10 + digit_sum(number // 10)


for number in [5824, 7, 0]:
    print("Sum of digits:", digit_sum(number))
