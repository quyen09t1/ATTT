#!/usr/bin/python3
import os
plain = open('plain.txt', 'r').read().strip().encode()


class Encryption:
    def __init__(self):
        self.key = os.urandom(5)

    def encrypt(self, data: bytes) -> bytes:
        c = b''
        for i in range(len(data)):
            c += bytes([data[i] ^ self.key[i % len(self.key)]])
        return c


def main():
    global plain
    crypto = Encryption()
    print('Cipher:', crypto.encrypt(plain).hex())


if __name__ == '__main__':
    main()
