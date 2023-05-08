# Given an integer return the integer with all the digits reversed:
# Must work for positive and negative numbers 
# and the negative sign must remain on the left of the integer
# If the reverse number has leading zeros you can drop those leading zeros
# Example Input 1:
# 1234
# Example Output 1:
# 4321
# Example Input 2:
# -1234
# Example Output 2:
# -4321
# Example Input 3:
# 100
# Example Output 3:
# 1

def solution(digits):
    str_digits = str(digits)
    if str_digits[0] == '-':
        return int(str_digits[:0:-1]) * -1
    return int(str_digits[::-1])
