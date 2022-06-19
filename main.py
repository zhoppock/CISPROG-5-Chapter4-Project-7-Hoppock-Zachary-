from shiftRight import shiftRight
from binaryToDecimal import binaryToDecimal
from decryption import decryption

bitString = input("Input a string of bits: ")

shiftedNum = shiftRight(bitString)
decimal = binaryToDecimal(shiftedNum)
plainText = decryption(decimal)

print("\nYour unencrypted decimal number is: " + plainText)