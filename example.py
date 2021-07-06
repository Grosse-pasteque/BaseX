import BaseX

config = {
    2: 64,
    3: 32
}

encrypted = BaseX.encrypt(b"hello", config)
decrypted = BaseX.decrypt(encrypted, config)

print(encrypted)
print(decrypted)