# Stage 4 cipher generator - built by Sewmina G.D.D. (IT24103936)
import base64

plaintext = "the evidence file is named incident_report_final.dd check the auth log for 03:14 flag is AEGIS{layers_of_the_vault}"

def caesar_encrypt(text, shift):
    result = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)
    return ''.join(result)

SHIFT = 13
ciphertext = caesar_encrypt(plaintext, SHIFT)
encoded = base64.b64encode(ciphertext.encode()).decode()
print("Base64(Caesar) blob to paste into Stage 3 dashboard:")
print(encoded)
