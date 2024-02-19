primes = [2, 3]
main_number_list = []

for i in range(4,151):
    main_number_list.append(i)

i_primes = iter(primes)
i_numbers = iter(main_number_list)

while len(main_number_list) > 0:
    current_prime = next(i_primes) # get the next prime number
    for index,num in enumerate(main_number_list):# remove all numbers that are dividable by a prime number from list
        if num % current_prime == 0:
            main_number_list.pop(index)
    i_numbers = iter(main_number_list) # create the iter again because i modified original list
    next_prime = next(i_numbers) # get the next prime number (which is the first number in main number list)
    primes.append(next_prime)
    main_number_list.pop(0) # remove number from list



print(primes)
    


    
