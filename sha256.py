import hashlib as _h

def _x(p):
    return _h.sha256(p.encode()).hexdigest()

def __go():
    p = input("Enter password (visible): ")
    print("Encrypted (SHA-256):", _x(p))

if __name__ == "__main__":
    __go()
