try :
	a = 3
	if a < 4 :
		b = a/(a-3)

	print("Value of b = ", b)

except(ZeroDivisionError, NameError):
	print("\nError Occurred and Handled")
