encrypted_text = list()
with open('p059.txt') as f:
    encrypted_text.extend(f.read().split(','))
encrypted_text = [int(i) for i in encrypted_text]

# find the key using frequency search
key = [0, 0, 0]
for i in range(0, 3):
    for j in range(i, len(encrypted_text), 3):
        for k in range(97, 123):
            if encrypted_text[j] ^ k == 32:
                key[i] = k


def decrypt(encrp_txt, key):
    output = len(encrypted_text) * [0]
    for i in range(0, len(key)):
        for j in range(i, len(encrypted_text), len(key)):
            output[j] = encrypted_text[j] ^ key[i]
    return output


decrypted_text_ascii = decrypt(encrypted_text, key)
print(sum(decrypted_text_ascii))

decrypted_text = ''.join(chr(i) for i in decrypted_text_ascii)
print(decrypted_text)
