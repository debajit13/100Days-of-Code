num1,num2 = map(int, input("Enter the two numbers : ").split(" "))
print("Numbers before swap: \nNumber1 = {} \nNumber2 = {}".format(num1,num2))
temp = num1
num1 = num2
num2 = temp
print("\nNumbers after swap: \nNumber1 = {} \nNumber2 = {}".format(num1,num2))
