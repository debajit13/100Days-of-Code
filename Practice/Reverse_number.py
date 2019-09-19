def reverse(n):
    rev_number = 0
    while n > 0:
        rev_number = (rev_number * 10) + (n % 10)
        n = n//10
    return rev_number

print("_____REVERSE OF NUMBER_____")
number = int(input("Enter a number : "))
print("Reverse of the number : {}".format(reverse(number)))
