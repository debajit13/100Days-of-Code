def sod(n):     #function to calculate sum of digits
    sum = 0
    while n != 0:
        sum = sum + n%10
        n = n//10
    return sum


print("_____SUM OF DIGITS_____")
num = int(input("Enter the number : "))
print("Sum of Digits : {}".format(sod(num)))
