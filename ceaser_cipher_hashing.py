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

plain_text=input("Enter the Plain text:")
n=len(plain_text)
hash_value=hashing(plain_text)
hash_text=plain_text+hash_value
print(hash_text)
n=int(input("Enter the no.of.characters to shift (key):"))
encrypted=caeser(hash_text, n)
print(encrypted,"Encryption process is over..",'\n')

decrypt=caeser(encrypted,-n)
retrived_text=decrypt[:n+1]
print("Text after decrypting the encrypted text:",retrived_text)
if(hash_value==hashing(retrived_text)):
    print("Text after decrypted is same as plain text")
else:
    print("some error")