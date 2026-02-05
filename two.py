import random
import time

cipher_hex = "f60d1ef6307bc56ed4f3f8fe41ea9bcf87ec76fb88dccfd418b7083b601303b923ebba81ca"
cipher = bytes.fromhex(cipher_hex)
n = len(cipher)

now = int(time.time())

for seed in range(now - 86400, now + 5):  # last 24 hours
    random.seed(seed)
    keystream = bytearray(int(random.random() * 256) for _ in range(n))
    flag = bytes(c ^ k for c, k in zip(cipher, keystream))

    if all(32 <= b <= 126 for b in flag):
        print("SEED:", seed)
        print("FLAG:", flag.decode())
        break
