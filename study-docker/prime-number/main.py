primes = [3, 5, 7, 11, 13, 17, 23]
current = 25
IS_PRIME = True
while current <= 10000:
    IS_PRIME = True
    for x in primes:
        if current % x == 0:
            IS_PRIME = False
            break
    if IS_PRIME:
        primes.append(current)
        print("new prime: " + str(current))
    current += 2
