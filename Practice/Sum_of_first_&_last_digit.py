def sum(n):     #calculate sum of the first and last digit
    last_digit = n%10
    first_digit = n
    while(first_digit > 10):
        first_digit = first_digit//10
    s = first_digit + last_digit
    return s

print("_____SUM OF FIRST AND LAST DIGIT_____")
number = int(input("Enter the number : "))
print(sum(number))
