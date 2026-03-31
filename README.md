**CAESER CIPHER**
  
  One of the simplest and oldest encryption technique
  Encryption: shifts each character of the message or the text by fixed no of character (key)
  Decryption: shifts each character of the message or the text by the same fixed no of character but in the opposite direction (negative of the key)

**POLYNOMIAL ROLLING HASH FUNCTION**

  converts the given input to fixed length hash string
  Base p=31
  Large modulus m = 2^61 - 1 (a prime number)

  how it works:
    Each character is converted to its ASCII value.
    Multiplied by increasing powers of p.
    Sum is taken modulo m to avoid overflow.
    Result is converted into a base-62 string.
    Output is padded or trimmed to a fixed length (default = 12)

**FLOW OF THE PROGRAM**

  Input: Plain text is given as input
  Hash Value generation: Plain text is passed to the hashing function which returns the respective hash value
  Appending: Plain text and Hash value are concatenated 
  Encryption: The concatnated string is passed to the caeser cipher encryption function along with the shift key
  Decryption: The Encrypted text is decrypted using the negative of the shift key
  Retriving: The Plain text is retrived from the decrypted string
  Integrity Check: The initial hash value is compared with hashed value of the retrived text as check for integrity

**USE OF LLM IN THIS**
  1) Analysis on the existing options of hash function available 
    Looking on the possibilities of using SHA-256 or AES kind of secure hash function 
    Complex steps of manual implementation
  2) Generation the custom hash function
    Polynomial Rolling hash function
