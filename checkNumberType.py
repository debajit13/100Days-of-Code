def checkPrime(number):
    for i in range(2,number):
        if number%i != 0:
            print("Number is a Prime Number")
            break
        else:
            print("Number is not a Prime Number")
            break


def checkOddEven(number):
    if number%2 == 0:
        print("Number is a Even Number")
    else:
        print("Number is a Odd Number")


def checkPalindrome(number):
    (temp,reverse) = (number,0)

    while(temp != 0):
        reverse = (reverse*10) + (temp%10)
        temp = temp/10
    if number == reverse:
        print("Number is a Palindrome Number")
    else:
        print("Number is not a Palindrome Number")


def checkArmstrong(number):
    (sum,temp) = (0,number)
    while(temp!=0):
        remainder = temp%10
        sum = sum + (remainder**3)
        temp = temp/10
    if sum == number:
        print("Number is an Armstrong Number")
    else:
        print("Number is not an Armstrong Number")


number = int(input("Enter the number : "))
checkPrime(number)
checkOddEven(number)
checkArmstrong(number)
checkPalindrome(number)
