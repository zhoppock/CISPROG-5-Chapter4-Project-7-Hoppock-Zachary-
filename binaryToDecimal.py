def binaryToDecimal(number):
  binary = number
  exponent = 0
  while exponent >= 0:
    decimal = 0
    exponent = len(binary) - 1
    for digit in binary:
      decimal += int(digit) * (2 ** exponent)
      exponent = exponent - 1
  print("\nThe decimal integer value is", decimal)
  return decimal