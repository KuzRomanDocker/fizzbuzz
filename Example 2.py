n = int(input("Enter a natural number from 1 to 9999\n"))
def fizzbuzz(n):
    if n < 1 or n > 9999:
        print("This number is wrong")
    elif n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n

print(fizzbuzz(n))