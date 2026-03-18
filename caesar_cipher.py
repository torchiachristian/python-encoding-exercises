char = 'a'
position = ord(char) - 97
new_position = (position + 3) % 26
new_char = chr(new_position + 97)
print(new_char)