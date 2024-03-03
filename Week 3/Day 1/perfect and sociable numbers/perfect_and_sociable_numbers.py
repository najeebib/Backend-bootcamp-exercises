def summ_list(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

def print_list(arr):
    for num in arr:
        print(num)

def sum_of_divisors(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    sum = summ_list(divisors)
    return sum, divisors
def check_perfect(number):
    sum, divisors = sum_of_divisors(number)
    print(sum)
    if sum == number:
        print_list(divisors)

def check_friendly(number1, number2):
    sum_number1_divs, divisors1 = sum_of_divisors(number1)
    sum_number2_divs, divisors2 = sum_of_divisors(number2)
    if sum_number1_divs == number2 and sum_number2_divs == number1:
        print("The numbers are friendly")
        print(f"sum of {divisors2} is equal to {number1} and sum of {divisors1} is equal to {number2}")
    else:
        print("The numbers aren't friendly")

def find_sociable(number, sociable_numbers, steps=10):
    sum, _ = sum_of_divisors(number)
    if sum == number or sum in sociable_numbers:
        sociable_numbers.append(number)
        print(f"social chain found: {sociable_numbers}")
        return
    
    sociable_numbers.append(number)

    if steps > 0:
        find_sociable(sum, sociable_numbers, steps - 1)
    else:
        print("No social chain found")


check_friendly(220, 284)
find_sociable(200, [])