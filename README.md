# Caesar Cipher Encryption & Manual Hashing Program

## What is caesar cipher?

One of the simplest and oldest encryption technique

Encryption: shifts each character of the message or the text by fixed no of character (key)  
Decryption: shifts each character of the message or the text by the same fixed no of character but in the opposite direction (negative of the key)

## Polynomial Rolling Hash Function

Converts the given input to a fixed length hash string

Base p = 31  
Large modulus m = 2^61 - 1 (a prime number)

### How it works:

- Each character is converted to its ASCII value  
- Multiplied by increasing powers of p  
- The sum is taken modulo m to avoid overflow  
- Result is converted into a base-62 string  
- Output is padded or trimmed to a fixed length (default = 12)

## Flow of the Program

- Input: Plain text is given as input  
- Hash value generation: Plain text is passed to the hashing function which returns the respective hash value  
- Appending: Plain text and Hash value are concatenated  
- Encryption: The concatenated string is passed to the caesar cipher encryption function along with the shift key  
- Decryption: The Encrypted text is decrypted using the negative of the shift key  
- Retrieving: The Plain text is retrieved from the decrypted string  
- Integrity Check: The initial hash value is compared with hashed value of the retrived text as a check for integrity  

## Use of LLM in this

1) Analysis of the existing options of hash function available
   - Consideration of using an existing hash functions
   - Looking on the possibilities of using SHA-256 as secure hash function  
   - Skipped due to complex steps of manual implementation  

2) Generation of the custom hash function  
   Polynomial rolling hash function
