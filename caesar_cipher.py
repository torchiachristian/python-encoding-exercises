#cifra una sola lettera a come esempio
#char = 'a'
#position = ord(char) - 97
#new_position = (position + 3) % 26
#new_char = chr(new_position + 97)
#print(new_char)

#ora che singola lettera viene encryptata, ci serve una funzione che prenda in input una stringa e una chiave, e in output dia una stringa cifrata
#creato stringa result e flow per scorrere il carattere lettera per lettera. problema: carattere maiuscolo richiede base 65 e minuscolo 97, quindi serve if e elif per ogni caso. problema: se è spazio o punteggiatura va inserito così quindi iserisco un altro else. restituisco result.
def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                position = ord(char) - 97
                new_position = (position + key) % 26
                new_char = chr(new_position + 97)
                result += new_char
            elif char.isupper():
                position = ord(char) - 65
                new_position = (position + key) % 26
                new_char = chr(new_position + 65)
                result += new_char
        else:
            result += char
    return result