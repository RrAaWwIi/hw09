def count_digits(n):
    n = abs(n)

    if n < 10:
        return 1

    return 1 + count_digits(n // 10)

def power(base, exponent):
    if exponent == 0:
        return 1

    if exponent < 0:
        return 1 / power(base, -exponent)

    return base * power(base, exponent - 1)

def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


print(count_digits(0))
print(count_digits(7))
print(count_digits(2026))

print(power(2, 10))
print(power(5, 0))

print(is_palindrome("racecar"))
print(is_palindrome("level"))
print(is_palindrome("python"))
