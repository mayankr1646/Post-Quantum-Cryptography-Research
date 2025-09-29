# Post-Quantum Cryptography Research

This repository contains the Python code I wrote for my Class 12 research project:  
**"Quantum-Proofing the Internet: A Performance Study of RSA vs. Simulated Kyber"**.

I wanted to explore what happens when future quantum computers threaten current internet encryption and check if post-quantum algorithms (like Kyber) are actually faster in practice. This project is mostly a simulation, but it helped me understand the core concepts and performance differences.

---

## Features
- RSA key generation, encryption, and decryption using PyCryptodome.
- PQC-like key generation, encapsulation, and decapsulation using Python’s `secrets` and `hashlib`.
- Performance benchmarking with multiple trial runs.
- Visual plot of average encryption/decryption times.

---

## My Setup
- Laptop: Acer Aspire AL14  
- CPU: AMD Ryzen 5 5500U  
- RAM: 16GB  
- OS: Windows 11  
- Python version: 3.11

> This might affect the exact timing, but the relative difference between RSA and PQC should be similar on other machines.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mayankr1646/Post-Quantum-Cryptography-Research.git
cd Post-Quantum-Cryptography-Research
