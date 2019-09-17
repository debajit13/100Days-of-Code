length,breath = map(int, input("Enter the length and breath of the rectangle : ").split(" "))
area = length * breath
perimeter = 2*(length + breath)
print("Area of the rectangle : {}".format(area))
print("Perimeter of the rectangle : {}".format(perimeter))
