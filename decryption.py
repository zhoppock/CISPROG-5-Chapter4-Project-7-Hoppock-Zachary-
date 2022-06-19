def decryption(code):
  print("\nYour encrypted text is:", code)
  encryptedText = str(code)
  distance = 1
  text = ""
  for ch in encryptedText:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('0'):
      cipherValue = ord('9') - (distance - abs(ord('0') - ordvalue - 1))
    text += chr(cipherValue)
  print("The plaintext is:", text)
  return text