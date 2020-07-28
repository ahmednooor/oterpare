# OTERPARE

(One Time Encrypted Remote Password Authenticated Resource Exchange) 

A PAKE like protocol for client authentication and resource exchange without explicitly sharing password.

> **NOTE & DISCLAIMER: This is a hobby project and certainly not meant for anything serious.**

### Explanation

![https://raw.githubusercontent.com/ahmednooor/oterpare/master/oterpare_diagram.svg?token=AEHI32EVJWDXOH6YL3CJO5K7FHTIO](https://raw.githubusercontent.com/ahmednooor/oterpare/master/oterpare_diagram.svg?token=AEHI32EVJWDXOH6YL3CJO5K7FHTIO)

### Demo Code Output

```
PS C:\...\oterpare> python .\oterpare_demo.py

[j, m, e, x, v, r] will be different on each iteration

[REGISTRATION] should only be done on a MITM-proof secured channel
[C -> S]
u : 6d61727469616e333637
p : 7040353577307264
[S -> C]
True

[INIT_AUTH]
[C -> S]
u : 6d61727469616e333637
[S -> C]
j : c7ba5aedfb106d9a14aacf8ca1b85fb6ef51a075b50ecd970df8d90fa763fe10
m : d3452ba8daa974d911857e06cf97346d8be4595be079f92a0e6e23aa8ab8d5ec

[AUTHENTICATE]
RESOURCE [S]: 3c50524f5445435445445f5245534f555243452e2e2e2f3e
[C -> S]
u : 6d61727469616e333637
e : f04dd2d3406d7edf798afbe1c085675c2a931b0c25cde184bea55f60ddc57d73
x : 4ba9978f9e232a54443df2c2afd73f02086b6fd095bfd073f7112ea32ec453dd
[S -> C]
v : 9a8256bd990b3c521c9950d90fa549da36a24c7e743ec23ff583fa82407f36ac
r : 36d2562667e5f33b03aeaa8f71aa135e68799e895a016a03

[AUTHENTICATED]
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
