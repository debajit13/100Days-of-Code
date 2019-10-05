def checkPrime(number):
    if number%2 == 0:
        print("Number is not prime")
    else:
        print("Number is prime")

print("_____Prime Number Checker_____")
num = int(input("Enter a number : "))
checkPrime(num)
