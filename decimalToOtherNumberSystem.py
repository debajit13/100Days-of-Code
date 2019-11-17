# Function to convert decimal to binary
def decimal_to_binary(dec):
	decimal = int(dec)
	print(decimal, " in Binary : ", bin(decimal))

# Function to convert decimal to octal
def decimal_to_octal(dec):
	decimal = int(dec)
	print(decimal, "in Octal : ", oct(decimal))

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(dec):
	decimal = int(dec)
	print(decimal, " in Hexadecimal : ", hex(decimal))

dec = 8
decimal_to_binary(dec)
decimal_to_octal(dec)
decimal_to_hexadecimal(dec)
