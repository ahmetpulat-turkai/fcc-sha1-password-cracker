import hashlib


def _load(name):
    with open(name) as f:
        return [line.strip() for line in f if line.strip()]


def crack_sha1_hash(hash, use_salts=False):
    passwords = _load("top-10000-passwords.txt")
    salts = _load("known-salts.txt") if use_salts else []
    for pw in passwords:
        if hashlib.sha1(pw.encode()).hexdigest() == hash:
            return pw
        for salt in salts:
            for cand in (salt + pw, pw + salt):
                if hashlib.sha1(cand.encode()).hexdigest() == hash:
                    return pw
    return "PASSWORD NOT IN DATABASE"
