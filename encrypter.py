import hashlib
import codecs
import qrcode


# Get text input from user
text = input("Enter text to convert to MD5 hash: ")

# Convert text to MD5 hash
md5_hash = hashlib.md5(text.encode()).hexdigest()

# Print the MD5 hash
print("MD5 hash of", text, "is:", md5_hash)

text2 = md5_hash

# Convert the text to a SHA256 hash
hash_object = hashlib.sha256(text2.encode())

# Get the hexadecimal representation of the hash
hex_digest = hash_object.hexdigest()
print(" ")
print("The generated hash is converted to SHA256 hash which is given as below")
print(" ")
print("SHA256 hash:", hex_digest)


text3 = hex_digest

# Encode the string using ROT13
rot13_string = codecs.encode(text3, 'rot13')

print(" ")
print("The generated hash is converted to Rot13 hash which is given as below")
print(" ")
# Print the result
print("Rot13 hash :" , rot13_string)



text4 = rot13_string
res_hash = hashlib.new('ripemd160', text4.encode()).hexdigest()
print(" ")
print("The generated hash is converted to RES hash which is given as below")
print(" ")
print("RES Hash",res_hash)

# joined_text = (res_hash+res_hash)
# print("Joined RES text : " , joined_text)


morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
'X': '-..-', 'Y': '-.--', 'Z': '--..', 'a': '.-', 'b': '-...',
'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
'5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
'.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.', '-': '-....-',
'(': '-.--.', ')': '-.--.-'}

def to_morse_code(text6):
    morse_code = []
    for char in text6:
        if char in morse_dict:
            morse_code.append(morse_dict[char])
    return ' '.join(morse_code)

text6 = res_hash
morse_code = to_morse_code(text6)
print(" ")
print("The generated hash is converted to Moorse code hash which is given as below")
print(" ")
print("Moorse Code : ",morse_code)


text5 = morse_code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(text5)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("hash.png")

