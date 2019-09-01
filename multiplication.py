"""
    if a user enter a number it returns the multiplication table of that number
"""
def multiplication(number):
    for i in range(1,11):
        print("{} * {} = {}" .format(number,i,number * i))
        
n = int(input("Enter the number : "))
multiplication(n)
