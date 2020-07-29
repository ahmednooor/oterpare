# OTERPARE

(One Time Encrypted Remote Password Authenticated Resource Exchange) 

A PAKE like protocol for client authentication and resource exchange without explicitly sharing password.

> **NOTE & DISCLAIMER: This is a hobby project and certainly not meant for anything serious.**

### Explanation

![https://raw.githubusercontent.com/ahmednooor/oterpare/master/oterpare_diagram.svg?token=AEHI32EVJWDXOH6YL3CJO5K7FHTIO](https://raw.githubusercontent.com/ahmednooor/oterpare/master/oterpare_diagram.svg?token=AEHI32EVJWDXOH6YL3CJO5K7FHTIO)

### Demo Code Output [1]

```
PS C:\...\oterpare> python .\oterpare_demo.py

[j, m, e, x, v, r] will be different on each iteration, but the RESOURCE will remain same

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
j : aa44b4b74fab2cdb21d84761be7983dfffe0966b7d4c430d408fc8014d5ca318
m : da9c4d193f65f1bd8b0147762cc7ae6110126dc35ff65f2be27aaa339c31f970

[AUTHENTICATE & EXCHANGE]
RESOURCE [S]: 3c50524f5445435445445f5245534f555243452e2e2e2f3e
[C -> S]
u : 6d61727469616e333637
e : 779cb1bd4fdea7e3eb6eb26cfa9716763efc97dcadacc9d6d419242045515bff
x : fcf8a81b0a5d2e73c7e3c38a7b76d657ee1054e442bfeed1c40b3a554adb8ca7
[S -> C]
v : 72bfc5b814ad48212019f23d6d8bcadca8e1af4d483efd85b1c0c76f7e69d224
r : d73c02808e939b466fee6e20218b1691dd81179e954b77e8

[EXCHANGED]
RESOURCE [C]: 3c50524f5445435445445f5245534f555243452e2e2e2f3e

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

[j, m, e, x, v, r] will be different on each iteration, but the RESOURCE will remain same

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
j : 8392532f1570a01eadcac38c245b49c8ddfeca38a2d4e0166f329d826b57b8d6
m : bfd115e33c21e72ce0b76e7d05e264cc78db6bd12956e20bc9269f338136879a

[AUTHENTICATE & EXCHANGE]
RESOURCE [S]: 3c50524f5445435445445f5245534f555243452e2e2e2f3e
[C -> S]
u : 6d61727469616e333637
e : 795600d251340755b333c215dc7345eb9a2682fca472552fbdf98f6f69eca456
x : b04fc66b44ec7e4ceb7f983f426ad9b60fa9e1c26c876e704f60ea2c4f726c1f
[S -> C]
v : a3f1a4a3da738bc616b9c1bce3228743c3ce98394aba85383d5edb0e910cbfe9
r : 63d291d6c0ba73373b427ea5acc7794ae72409be50c5165c

[EXCHANGED]
RESOURCE [C]: 3c50524f5445435445445f5245534f555243452e2e2e2f3e

[IS_REGISTERED]
True

[IS_AUTHENTICATED i.e. n == decrypt(text=v, key=k)]
True

[IS_RESOURCE_SAME i.e. client.RESOURCE == decrypt(text=r, key=k) == server.RESOURCE]
True

```

### Meta

> Author: Ahmed Noor E Alam (https://github.com/ahmednooor)
