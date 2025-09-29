import secrets
import hashlib

# --- PQC-like key generation (simulate lattice randomness) ---
def pqc_keygen():
    sk = secrets.token_bytes(32)   # secret key
    pk = hashlib.sha3_256(sk).digest()  # public key (hash of sk)
    return pk, sk

# --- Encapsulation (encryption) ---
def pqc_encapsulate(pk):
    random_secret = secrets.token_bytes(32)
    ciphertext = hashlib.sha3_256(pk + random_secret).digest()
    return ciphertext, random_secret

# --- Decapsulation (decryption) ---
def pqc_decapsulate(sk, ciphertext):
    # Normally lattice math, here just simulate
    pk = hashlib.sha3_256(sk).digest()
    return hashlib.sha3_256(pk + b"recover").digest()

# Demo
pk, sk = pqc_keygen()
ct, ss = pqc_encapsulate(pk)
print("Ciphertext:", ct[:20], "...")
print("Shared Secret (simulated):", ss[:20], "...")


import time
import secrets
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import matplotlib.pyplot as plt

# --- RSA Setup ---
def rsa_test():
    key = RSA.generate(2048)
    public_key = key.publickey()
    cipher = PKCS1_OAEP.new(public_key)
    decryptor = PKCS1_OAEP.new(key)

    message = b"Hello Mayank Quantum World"

    # Encrypt
    start = time.time()
    encrypted = cipher.encrypt(message)
    enc_time = time.time() - start

    # Decrypt
    start = time.time()
    decrypted = decryptor.decrypt(encrypted)
    dec_time = time.time() - start

    return enc_time, dec_time

# --- PQC Simulated Setup ---
def pqc_keygen():
    sk = secrets.token_bytes(32)
    pk = hashlib.sha3_256(sk).digest()
    return pk, sk

def pqc_encapsulate(pk):
    random_secret = secrets.token_bytes(32)
    ciphertext = hashlib.sha3_256(pk + random_secret).digest()
    return ciphertext, random_secret

def pqc_decapsulate(sk, ciphertext):
    pk = hashlib.sha3_256(sk).digest()
    return hashlib.sha3_256(pk + b"recover").digest()

def pqc_test():
    pk, sk = pqc_keygen()

    # Encrypt
    start = time.time()
    ct, ss = pqc_encapsulate(pk)
    enc_time = time.time() - start

    # Decrypt
    start = time.time()
    recovered = pqc_decapsulate(sk, ct)
    dec_time = time.time() - start

    return enc_time, dec_time

# --- Run Tests Multiple Times ---
rsa_enc, rsa_dec, pqc_enc, pqc_dec = [], [], [], []

for _ in range(10):  # repeat 10 times
    e, d = rsa_test()
    rsa_enc.append(e)
    rsa_dec.append(d)

    e, d = pqc_test()
    pqc_enc.append(e)
    pqc_dec.append(d)

# --- Plot Results ---
labels = ["RSA Encrypt", "RSA Decrypt", "PQC Encrypt", "PQC Decrypt"]
times = [sum(rsa_enc)/len(rsa_enc), sum(rsa_dec)/len(rsa_dec),
         sum(pqc_enc)/len(pqc_enc), sum(pqc_dec)/len(pqc_dec)]

plt.bar(labels, times)
plt.ylabel("Time (seconds)")
plt.title("RSA vs PQC Performance (Avg over 10 runs)")
plt.show()

