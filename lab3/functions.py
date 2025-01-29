#1
def grams_to_ounces(grams):
    return 28.3495231 * grams
print(grams_to_ounces(3))

#2
def fahrenheit_to_centigrade(F):
    return (5 / 9) * (F - 32)
print(fahrenheit_to_centigrade(3))

#3
def heads(head, legs):
    for i in range(1,head):
        if i*2 + (head-i)*4==legs:
            return f"chicken {i}, rabbits {head-i} "
print(heads(35, 94))

#4
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % 2 == 0:
            return False
    return True
numlist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
prime_numlist = list(filter(lambda x: isprime(x), numlist))
print(prime_numlist)

#5
def permutations(some):
    n = len(some)

    for i in range(n):
        for j in range(n):
            print(some[(j-i)], end=" ")
        print()
k=str(input("soz:"))
permutations(k)