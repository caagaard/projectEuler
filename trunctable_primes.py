# A left trunctable prime is a prime number that remains prime
# as you remove digits from the left ex: 3797 -> 797 -> 97 -> 7
# A right trunctable prime is as you would expect
# 3797 -> 379 -> 37 -> 3

# There are only eleven primes that are both left and right trunctable (no single digits)
# This program finds them and returns their sum


# Checks for a number to be prime
def isPrime(n, prime_list):
  i = 0
  while (prime_list[i]**2 <= n):
    if n % prime_list[i] == 0:
      return False
    else:
      i = i +1
  return True

def checkTrunc(n, prime_list):
  right = n
  while right > 10:
    right = right/10
    if right not in prime_list:
      return False
  left = str(n)
  while len(left) > 1:
    left = left [1:]
    if int(left) not in prime_list:
      return False
  return True


trunctables = []
primes = [2, 3, 5, 7]
i = 9
while len(trunctables) < 11:
  if isPrime(i, primes):
    primes.append(i)
    if checkTrunc(i, primes):
      trunctables.append(i)
      print(trunctables)
  i = i +1
# Test line to evaluate program
print(trunctables)
print(sum(trunctables))
