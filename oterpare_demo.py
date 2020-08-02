""" OTERPARE Protocol
(One Time Encrypted Remote Password Authenticated Resource Exchange) 
or just Otto
A PAKE like protocol for client authentication and resource exchange without 
explicitly sharing password.
Author: Ahmed Noor E Alam (https://github.com/ahmednooor)
"""

import uuid
import hashlib
from Cryptodome.Cipher import AES # pip install pycryptodomex


def hash(text: bytes, salt: bytes) -> bytes:
    hasher = hashlib.new("SHA256")
    hasher.update(text)
    hasher.update(hasher.digest() + salt)
    return hasher.digest()

def encrypt(text: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CFB, key[:16][::-1])
    return cipher.encrypt(text)

def decrypt(text: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CFB, key[:16][::-1])
    return cipher.decrypt(text)

def uuid4() -> bytes:
    return bytes(str(uuid.uuid4()), "utf-8")


class Server:
    _clients = {} # u: g, ...
    _rand_nums = {} # i: w, ...
    RESOURCE = b"<PROTECTED_RESOURCE.../>"
    s = b""

    def __init__(self, s):
        self.s = hash(text=s, salt=uuid4())

    def register(self, u, p):
        if u in self._clients:
            return False
        
        h = hash(text=u+p, salt=u+p)
        g = encrypt(text=h, key=self.s)
        self._clients[u] = g

        print()
        print("[REGISTRATION] " + \
              "should only be done on a MITM-proof secured channel")
        print("[C -> S]")
        print("u : " + u.hex())
        print("p : " + p.hex())

        return True

    def init_session(self, u):
        if u not in self._clients:
            return (None, None)

        n = hash(text=uuid4(), salt=uuid4())
        i = hash(text=uuid4(), salt=uuid4())
        w = encrypt(text=n, key=self.s)

        self._rand_nums[i] = w

        g = self._clients[u]
        h = decrypt(text=g, key=self.s)

        j = encrypt(text=i, key=n)
        m = encrypt(text=n, key=h)

        print()
        print("[INIT]")
        print("[C -> S]")
        print("u : " + u.hex())
        print("[S -> C]")
        print("j : " + j.hex())
        print("m : " + m.hex())

        return (j, m)

    def authenticate_and_exchange(self, u, e, x):
        if u not in self._clients:
            return (None, None)
        
        g = self._clients[u]
        h = decrypt(text=g, key=self.s)
        i = decrypt(text=e, key=h)

        if i not in self._rand_nums:
            return (None, None)
        
        w = self._rand_nums[i]
        n = decrypt(text=w, key=self.s)
        
        k = hash(text=h+n, salt=h+n)
        y = decrypt(text=x, key=k)

        if y != k:
            return (None, None)

        v = encrypt(text=n, key=k)
        r = encrypt(text=self.RESOURCE, key=k)

        del self._rand_nums[i]

        print()
        print("[AUTHENTICATE & EXCHANGE]")
        print("RESOURCE [S]: " + self.RESOURCE.hex())
        print("[C -> S]")
        print("u : " + u.hex())
        print("e : " + e.hex())
        print("x : " + x.hex())
        print("[S -> C]")
        print("v : " + v.hex())
        print("r : " + r.hex())

        return (v, r)


class Client:
    def __init__(self, u, p):
        self.u = u
        self.p = p
        self.is_registered = False
        self.RESOURCE = b""

    def register_with(self, server: Server):
        self.is_registered = server.register(self.u, self.p)
        print("[S -> C]")
        print(self.is_registered)
        return self.is_registered

    def authenticate_and_exchange_with(self, server: Server):
        (j, m) = server.init_session(self.u)
        
        if j is None or m is None:
            return False

        h = hash(text=self.u+self.p, salt=self.u+self.p)
        n = decrypt(text=m, key=h)
        i = decrypt(text=j, key=n)
        e = encrypt(text=i, key=h)
        
        k = hash(text=h+n, salt=h+n)
        x = encrypt(text=k, key=k)

        (v, r) = server.authenticate_and_exchange(self.u, e, x)

        if v is None or r is None:
            return False

        if n != decrypt(text=v, key=k):
            return False

        self.RESOURCE = decrypt(text=r, key=k)

        print()
        print("[EXCHANGED]")
        print("RESOURCE [C]: " + self.RESOURCE.hex())
        print("k [KEY C, S]: " + k.hex())

        return True


def main():
    client = Client(b"martian367", b"p@55w0rd")
    server = Server(b"_server_private_key_not_shared_with_anyone")

    print()
    print("[j, m, e, x, v, r, k] will be different on each iteration, but the " + \
          "RESOURCE will remain same")

    is_registered = client.register_with(server)
    # ^ this operation should only be done on a MITM-proof secured channel
    is_authenticated = client.authenticate_and_exchange_with(server)

    print()
    print("[IS_REGISTERED]")
    print(is_registered)
    print()
    print("[IS_AUTHENTICATED i.e. n == decrypt(text=v, key=k)]")
    print(is_authenticated)
    print()
    print("[IS_RESOURCE_SAME " + \
          "i.e. client.RESOURCE == decrypt(text=r, key=k) == server.RESOURCE]")
    print(client.RESOURCE == server.RESOURCE)
    print()

if __name__ == "__main__":
    main()
