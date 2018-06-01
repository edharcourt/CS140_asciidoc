import string, random

def encrypt(cleartext, otp):

    alphabet = string.printable
    ciphertext = ''

    for i in range(len(cleartext)):
        ciphertext += alphabet[(alphabet.find(cleartext[i]) +
                                alphabet.find(otp[i])) % len(alphabet)]

    return ciphertext

def decrypt(ciphertext, otp):

    alphabet = string.printable
    cleartext = ''

    for i in range(len(ciphertext)):
        cleartext += alphabet[(alphabet.find(ciphertext[i]) -
                               alphabet.find(otp[i])) % len(alphabet)]

    return cleartext

def GenOneTimePad(n):
    pad = ''
    alphabet = string.printable

    for i in range(n):
        pad += alphabet[random.randrange(len(string.printable))]

    return pad

otp = GenOneTimePad(20)
print(decrypt(encrypt('Hello!', otp), otp))