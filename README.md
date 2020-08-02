# OTERPARE

(One Time Encrypted Remote Password Authenticated Resource Exchange) 

A PAKE like protocol for client authentication and resource exchange without explicitly sharing password.

> **NOTE & DISCLAIMER: This is a hobby project and certainly not meant for anything serious.**

### Explanation

![https://raw.githubusercontent.com/ahmednooor/oterpare/master/oterpare_diagram.svg?token=AEHI32EVJWDXOH6YL3CJO5K7FHTIO](https://raw.githubusercontent.com/ahmednooor/oterpare/master/oterpare_diagram.svg?token=AEHI32EVJWDXOH6YL3CJO5K7FHTIO)

**Key Intents**
- Something that can be implemented over HTTP e.g. for REST APIs.
- Use of Diffie-Hellman was avoided because of big numbers, fancy maths and scripting languages.

**Features**
- Since each exchange's key depends upon a random value that gets deleted upon successful exchange, it maintains forward secrecy this way. It also prevents a request payload to be used more than once.

**Quirks**
- If the server changes its private key, then it will have to decrypt all the password hashes and random values in its storage and re-encrypt them with the new private key.
- A third party with a valid username can send INIT messages over and over again to create stored random values which might cause storage problems for the server. One option is to have an expiry for each random value and a cron job that clears all the expired ones.

### Demo Code Output [1]

```
PS C:\...\oterpare> python .\oterpare_demo.py

[j, m, e, x, v, r, k] will be different on each iteration, but the RESOURCE will remain same

[REGISTRATION] should only be done on a MITM-proof secured channel
[C -> S]
u : 6d61727469616e333637
p : 7040353577307264
[S -> C]
True

[INIT]
[C -> S]
u : 6d61727469616e333637
[S -> C]
j : 6fe543d25fd8215df8f98fe43fc06669c0c6e9bfc2d91596edca3944d827ac30
m : 5880c9588a5f4aec59539f2e7b9e78621529f13c6df36f7625e7cffd84862e64

[AUTHENTICATE & EXCHANGE]
RESOURCE [S]: 3c50524f5445435445445f5245534f555243452e2e2e2f3e
[C -> S]
u : 6d61727469616e333637
e : b1d7efd04456ff3a976995c31373c1ce79858782292633017bcff85d8c33a9e8
x : eab57fb3e189e3a03d1e1bda4a8ae69b62013e1785b2e3558eb78a616106f3df
[S -> C]
v : f424d559dc1bc92dae1137bdd43cffefb58c668de06c4ec66e9717ca82058024
r : d32f26eff6cb1cfe1f42f22c65a5783b42cdf2e5db1aa0c3

[EXCHANGED]
RESOURCE [C]: 3c50524f5445435445445f5245534f555243452e2e2e2f3e
k [KEY C, S]: 05520ad89bf97666470cd080db3f5ff09b9f61b4d87ab92cc110fbb45556aa2e

[IS_REGISTERED]
True

[IS_AUTHENTICATED i.e. n == decrypt(text=v, key=k)]
True

[IS_RESOURCE_SAME i.e. client.RESOURCE == decrypt(text=r, key=k) == server.RESOURCE]
True

```

### Demo Code Output [2]

```
PS C:\...\oterpare> python .\oterpare_demo.py

[j, m, e, x, v, r, k] will be different on each iteration, but the RESOURCE will remain same

[REGISTRATION] should only be done on a MITM-proof secured channel
[C -> S]
u : 6d61727469616e333637
p : 7040353577307264
[S -> C]
True

[INIT]
[C -> S]
u : 6d61727469616e333637
[S -> C]
j : ca59397d5d6705018963f3005090c3c73bd56d103dcb0a1c4c2572be671cefd1
m : a0609d60811b5789498f3bdaded380a569f3860a23fdddd62008413b730d9a1c

[AUTHENTICATE & EXCHANGE]
RESOURCE [S]: 3c50524f5445435445445f5245534f555243452e2e2e2f3e
[C -> S]
u : 6d61727469616e333637
e : b9135f061b9b217a05cb1fa5d46c08acfa4f909e7f09a0e136ddbbd2440c230a
x : d7648cc233a09f95f81f2bda961b99ae6959f580a34a7a82159af5b90e42e384
[S -> C]
v : c5db3c87ea4434e906ee566d78fdc705a53b836a620a370ab1749ffebce3eab5
r : 1a20e2362ac95f7907f52363a837e4c7507cd6a1955d61c2

[EXCHANGED]
RESOURCE [C]: 3c50524f5445435445445f5245534f555243452e2e2e2f3e
k [KEY C, S]: f1cbcdb2f2286575602b79ecbc78300d20128348e3906ddb18f30abd6b7c021f

[IS_REGISTERED]
True

[IS_AUTHENTICATED i.e. n == decrypt(text=v, key=k)]
True

[IS_RESOURCE_SAME i.e. client.RESOURCE == decrypt(text=r, key=k) == server.RESOURCE]
True

```

### Meta

> Author: Ahmed Noor E Alam (https://github.com/ahmednooor)
