from hashlib import sha256

text = "I am excited to learn about blockchain"

# encode the string before passing to sha256
hash_result = sha256(text.encode())

# hash into 16 bits
print(hash_result.hexidigest())