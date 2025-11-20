# sha-256-encryptor🔐 Heavily Obfuscated SHA-256 Password Hasher
Made by Bhargav Rodimea

This section provides a heavily obfuscated Python script that securely collects a password from the user and encrypts it using SHA-256.
The script is deeply obfuscated using compression and Base64 packing for demonstration, protection, or security research purposes.

🚀 Features

Password input hidden using getpass

Secure SHA-256 hashing via hashlib

Strongly obfuscated (compressed + encoded)

One-line executable payload using exec

Fully compatible with Python 3+

📌 Obfuscated Script
import zlib,base64
exec(zlib.decompress(base64.b64decode(
b'eJx1kE1OwzAMhv/KMt0A4QmIW6AKAl2kbcZp2gMNIKGkZBf9+2cJNVVTSaRb+PP55zvxf/nS6RUOu'
b'JKyVJAi4ImuVx7sXMI0qk4Td6ShQdQ8a9yAJSKcb9pRT8NXQ3Q7Oy9kEnp9skMhu4vYvVmvzH8m0+'
b'FTB4LkdCvMApVpWd0p6UQ5YEUg63h8b4P5niPFeQv2N3cx7Xuizd5tv6hBQ76g3kVBSZ0ynUkZpW'
b'8HAnSmeYbL3+3owLckS2nHYt6NhWMCQv6rjJ4Q2KJGW0xEi0yXWv5mNMsYIuHq5hIg6TgWo5JrNV'
b'M1waCiJJv9f5MZ1scf9w7uq0p1n9t90t7X8A7iB5Cg=='
)))

🧩 Internal Logic (De-Obfuscated)

The hidden payload performs:

import hashlib as H
import getpass as G

p = G.getpass("Enter password: ")
print("Encrypted (SHA-256):", H.sha256(p.encode()).hexdigest())

📦 How to Run
python obfuscated_sha256.py


Output:

Enter password:
Encrypted (SHA-256): <hash>

🏷 Author

Bhargav Rodimea
Developer • Student • Tech Enthusiast
