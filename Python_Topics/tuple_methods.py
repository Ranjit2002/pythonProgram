'''
tup = (23, 6, 23)  # Tuples are immutable
print(type(tup), tup)
tup = (32, 45, 76, 345, "Ranjit", True)
print(type(tup), tup)
print(len(tup))
print(tup[-1])
print(tup[0:])
print(tup[:])
print(tup[:4])
if 345 in tup:
    print("Yes")
else:
    print("No")
tup2 = tup[1:4]
print(tup2)

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)
'''

# tuple1 = (1, 2, 3, 2, 3, 4, 6, 3, 5)
# print(tuple1.index(3))
# print(tuple1.index(3, 5, 10))
# print(tuple1.count(3))
# print(len(tuple1))

# for i in range(1, 8):
#     print(i)

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

# Example usage:
limit = 50
prime_list = sieve_of_eratosthenes(limit)
print(prime_list)
