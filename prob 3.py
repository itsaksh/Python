def digit_sum(number):
    if number < 0:
        raise ValueError("number must be non-negative")
    if number < 10:                 
        return number
    return number % 10 + digit_sum(number // 10)
def digit_sum_traced(number, depth=0):
    pad = "   " * depth
    if number < 10:
        print(f"{pad}digit_sum({number}) -> base case returns {number}")
        return number
    print(f"{pad}digit_sum({number}) = {number % 10} + digit_sum({number // 10})")
    total = number % 10 + digit_sum_traced(number // 10, depth + 1)
    print(f"{pad}digit_sum({number}) returns {total}")
    return total
print("Trace for 5824:")
digit_sum_traced(5824)
print()
print("Sum of digits of 5824 :", digit_sum(5824))
print("Sum of digits of 7    :", digit_sum(7))
print("Sum of digits of 0    :", digit_sum(0))
print("Sum of digits of 99999:", digit_sum(99999))   
print("Sum of digits of 1000 :", digit_sum(1000))   