def primes_up_to(num):
    primes_list = [2]
    for number in range(2, num):
        for factor in primes_list:
            if number % factor == 0:
                break
        else:
            primes_list.append(number)
    return primes_list

print(primes_up_to(200))

