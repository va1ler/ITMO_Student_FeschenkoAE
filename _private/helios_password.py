#!/usr/bin/env python3
"""Пароль от helios (s561306@helios.cs.ifmo.ru), зашифрованный.

Запуск:  python3 _private/helios_password.py
Спросит мастер-пароль и покажет пароль от helios.
Сам пароль в файле не хранится в открытом виде: только шифр (PBKDF2-SHA256, 600 000 итераций + HMAC).
"""
import base64, getpass, hashlib, hmac, sys

BLOB = "sCSKtff6ywoxqr5jcAZa69rF283anK8RzOcf4be6tsj4L9aIxulzDQU1Pzs5crxsRILkMVH0Ytj4"
ITER = 600000

def main():
    raw = base64.b64decode(BLOB)
    salt, tag, ct = raw[:16], raw[16:48], raw[48:]
    master = getpass.getpass("Мастер-пароль: ").encode()
    key = hashlib.pbkdf2_hmac("sha256", master, salt, ITER, 64)
    ek, mk = key[:32], key[32:]
    if not hmac.compare_digest(hmac.new(mk, salt + ct, hashlib.sha256).digest(), tag):
        sys.exit("❌ Неверный мастер-пароль")
    ks = b"".join(hashlib.sha256(ek + i.to_bytes(4, "big")).digest() for i in range(4))
    print("🔑 helios (s561306):", bytes(a ^ b for a, b in zip(ct, ks)).decode())

if __name__ == "__main__":
    main()
