from caesar_cipher import encrypt

text = input("enter the text: ")
key = int(input("enter the key "))
print(encrypt(text, key))

