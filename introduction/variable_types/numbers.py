# Integer
integer_number = 3
print("Integer = ", integer_number)

# Floating-point numbers
float_number = 3.14
print("Floating-point number = ", float_number)

# type() -> it returns type of the variable
print("Integer variable type", type(integer_number))
print("Floating-point variable type", type(float_number))

# sum +
sum_calc = 1 + 1
print("1 + 1 = ", sum_calc)

# subtraction -
subtraction = 1 - 1
print("1 - 1 = ", subtraction)

# multiplication *
multiplication = 2 * 2
print("2 x 2 = ", multiplication)

# division /
division = 5 / 2
print("5 / 2 = ", division)
print("Division result type = ", type(division)) # the result of a division will always be a float

# int() -> it converts a value into integer
print("Integer value = ",int(division))

# float() -> it converts a value into float
print("Float value = ", float(division))

# division (integer result) /
division = 5 // 2
print("5 / 2 = ", division)
print("Division result type = ", type(division)) # the result of a division will always be a float

# Modulo %
modulo = 5 % 2
print("Modulo 5 / 2 = ", modulo)