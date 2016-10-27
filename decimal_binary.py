# Finds the sum of all the numbers less than 10**6 which are palindroes
# in both base 10 and base 2

# Checks if an integer is a palindrome
def isPalindrome(int_to_check):
    if len(int_to_check) <= 1:
        return(True)
    elif int_to_check[0] == int_to_check[-1]:
        return(isPalindrome(int_to_check[1:-1]))
    else:
        return(False)

# Converts a decimal integer into a binary integer
def convertToBinString(int_to_convert):
    binary_version = ''
    while int_to_convert > 0:
        binary_version = str(int_to_convert % 2) + binary_version
        (int_to_convert) = int(int_to_convert / 2)
    return(binary_version)

palindromes = []
# Only odd integers can be binary palindromes, because no integer
# starts with '0'
for number in range(1,500001):
    test_int = (2*number - 1)
    if isPalindrome(str(test_int)):
        binary_test = convertToBinString(test_int)
        if isPalindrome(str(binary_test)):
            palindromes.append(test_int)

print(sum(palindromes))
