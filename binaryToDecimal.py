def decimalToBinary(n):

	if(n > 1):
		decimalToBinary(n//2)


	print(n%2, end=' ')




if __name__ == '__main__':
	decimalToBinary(8)
	print("\n")
	decimalToBinary(18)
	print("\n")
	decimalToBinary(7)
	print("\n")
