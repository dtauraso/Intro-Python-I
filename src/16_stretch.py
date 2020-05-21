import math
def sieve_of_eratosthenes(number):

    #  maybe use root(number) later
    list_of_numbers = [i for i in range(2, number)]

    i = 0
    print(int(math.sqrt(number)))
    while(i < len(list_of_numbers)):
        # print(i, list_of_numbers)
        # print(list_of_numbers[0:i])
        # not exactly sure why i+1 is needed here but it works
        list_of_numbers = list_of_numbers[0:i + 1] + [number for number in list_of_numbers[i:]
                                                                if(number % list_of_numbers[i] > 0)]
        # print('next set of numbers', list_of_numbers)
        i += 1
    return list_of_numbers
primes_below_number = sieve_of_eratosthenes(33000)
print(primes_below_number)