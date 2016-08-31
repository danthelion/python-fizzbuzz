def fizzbuzz(n):
    msg = ''
    if num % 3 == 0:
        msg += 'Fizz'
    if num % 5 == 0:
        msg += 'Buzz'
    return msg or num

for num in range(1, 101):
    print(fizzbuzz(num))
