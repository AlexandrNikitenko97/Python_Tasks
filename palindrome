from math import sqrt  # import square root from math library

from_num = 10000   # lowest 5-digit
to_num = 99999     # biggest 5-digit

primes = []                               # initialize empty array for all primes
multiplication = max_palindrome = 0       # initializing variables
palindrome = {}                           # initialize dictionary for all palindromes

# creating array of primes from 10000 to 99999
for i in range(to_num, from_num+1, -1):
    if i % 2 != 0:
        for j in range(2, int(sqrt(i))+1):
            if i % j == 0:
                break
        else:
            primes.append(i)

print("Search started....")

# finding multiplication of each primes and check is it palindrome or no
for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        multiplication = primes[i] * primes[j]
        if str(multiplication) == str(multiplication)[::-1]:          # check palindrome it or no
            if multiplication > max_palindrome:
                max_palindrome = multiplication
                palindrome[max_palindrome] = (primes[i], primes[j])   # adding palindromes and their factors to the dict

# printing results
print("Search is finished. Here's result:")
print("%d * %d = %d" % (palindrome[max(palindrome)][0], palindrome[max(palindrome)][1], max(palindrome)))
