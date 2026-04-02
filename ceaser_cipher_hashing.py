def hashing(text, length=12):
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    p = 31
    m = 2305843009213693951
    hash_value = 0
    p_pow = 1
    
    for i in text:
        hash_value = (hash_value + ord(i) * p_pow) % m
        p_pow = (p_pow * p) % m
        
    result = []
    
    if hash_value == 0:
        return chars[0] * length

    while hash_value > 0:
        hash_value, remainder = divmod(hash_value, 62)
        result.append(chars[remainder])
    
    hash_str = "".join(result[::-1])
    
    if len(hash_str) < length:
        return hash_str.ljust(length, '0')
    return hash_str[:length]

def caeser(text, n):
    word=''
    for i in text:
        if i.isdigit():
            new_i = chr(((ord(i) - ord('0')) + n) % 10 + ord('0'))

        elif i.islower():
            new_i = chr((ord(i) - ord('a') + n) % 26 + ord('a'))

        elif i.isupper():
            new_i = chr((ord(i) - ord('A') + n) % 26 + ord('A'))

        else:
            new_i=i
        word+=new_i

    return word


plain_text=input("Enter your plain text:")
n=len(plain_text)
key=int(input("Enter your shift value(key):"))

#ENCRYPTION
caeser_text=caeser(plain_text,key)
hash_value=hashing(caeser_text)
encrypted_text=caeser_text+hash_value
print("message after encryption:",encrypted_text)
print("Encryption Done..")

#DECRYPTION
retrieved_text=encrypted_text[:n]
print("Text retrieved:",retrieved_text)
decrypted_text=caeser(retrieved_text,-key)
if(encrypted_text[n:]==hashing(retrieved_text)):
    print("Hashing value Matches..")
    print("Text after decrypting the retrieved text:",decrypted_text)
else:
    print("error")
