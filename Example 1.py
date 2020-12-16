fizzbuzz = int(input("Enter a natural number from 1 to 9999\n"))
if fizzbuzz < 1 or fizzbuzz > 9999:
    print("This number is wrong")
elif fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print("fizzbuzz")
elif fizzbuzz % 3 == 0:
    print("fizz")
elif fizzbuzz % 5 == 0:
    print("buzz")
else:
    print(fizzbuzz)
