# A 1-9 pandigital is a number containing the digits 1,2,3,4,5,6,7,8,9
# Take 192 * 1, 192 *2, and 192*3.  These equal 192, 384, and 576
# Then the concatenated product 192* (1,2,3) = 192384576 which is a pandigital

# Goal - Find the largest 9 digit pandigital that can be formed as 
# the concatenated sum of some (1,2,...n) where n > 1

# Brute force

# Check if a given number is a pandigital

def checkPandigital(number):
  for digit in range(1,10):
    if str(digit) not in number:
      return False
  return True

def test(number):
  digit_sum = sum(int(digit) for digit in number)
  if digit_sum == 45:
    if checkPandigital(number):
      return int(number)
  return 0

longest = 0

for i in range(6,10):
  big_number =str(i)+str(2*i) + str(3*i) + str(4*i) + str(5*i)
  big_test = test(big_number)
  if big_test > longest:
      longest = big_test

for i in range(26, 32):
  big_number = str(i)+str(2*i)+str(3*i)+str(4*i)
  big_test = test(big_number)
  if big_test > longest:
      longest = big_test

for i in range(123, 328):
  big_number = str(i) + str(2*i) + str(3*i)
  big_test = test(big_number)
  if big_test > longest:
      longest = big_test

for i in range(5123, 9877):
  big_number = str(i) + str(2*i)
  big_test = test(big_number)
  if big_test > longest:
      longest = big_test

print(longest)
