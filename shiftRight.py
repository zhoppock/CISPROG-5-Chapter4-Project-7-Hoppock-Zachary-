def shiftRight(number):
  bits = number
  result = ''
  if len(bits) > 0:
    result = bits[-1] + bits[:-1]
  print("\nThe shifted bit set is: " + result)
  return result