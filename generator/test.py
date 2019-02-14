import hashlib
from bitcoin.wallet import *
from bitcoin.core import b2lx
h = hashlib.sha256(b'horse feed bug glass sand stone').digest()
secret = CBitcoinSecret.from_secret_bytes(h)
address = CBitcoinAddress.from_scriptPubKey(secret.pub)
print(secret, b2lx(secret.pub))
