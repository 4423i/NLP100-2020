def cipher(w):
    if w == " ":
        return w
    elif w == w.lower():
        return chr(219 - ord(w))
    else:
        return w

cleartext = "I am a cipher"
ciphertext = ""
for i in cleartext:
    ciphertext += cipher(i)
print("cleartext  :",cleartext)
print("ciphertext :",ciphertext)

recovertext = ""
for i in ciphertext:
    recovertext += cipher(i)
print("recovertext :",recovertext)