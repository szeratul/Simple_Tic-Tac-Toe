prime_numbers = [i for i in range(2, 1001) if all(i % j != 0 for j in range(2, i))]
