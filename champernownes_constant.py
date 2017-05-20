# Champernowne's constant is created by concatenated all of the integers 
# to 0 as the fraction part: 0.1234567891011...

# If d_n is the nth digit, what is d_1 * d_10 *d_100 * ... d_1000000 ?

# let d<n> represent d_{10^n} ex: d3 => d_1000

d0 = 1
d1 = 1
d2 = 5

# 9 one digit numbers, 90 2 digit, 900 3 digit, etc

digit_counts = [0,9,90,900,9000,90000,900000]

# included value for 10**1 in fencepost because you never round
# down when dividing by 1
magic_nums = [1,1]

for i in range(2,7):
    count = 0
    j = 1
    while count <= 10**i:
      count = count + j*digit_counts[j]
      j = j+1
    j = j - 1
    count = count - j*digit_counts[j]
    number_position = (10**i - count + i -1)//(i)
    actual_number = 10**(i-1)+number_position
    digit_place = (10**i - count - 1) % i
    magic_nums.append(int(str(actual_number)[digit_place]))

print(magic_nums)

