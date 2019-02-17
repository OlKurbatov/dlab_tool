import hashlib

from bitcoin import *
from bitcoin.core import *
from bitcoin.core.script import *
from bitcoin.core.scripteval import *
from bitcoin.wallet import *

SelectParams('regtest')

hash = hashlib.sha256(b'hate doing stuff that I don`t know how to do').digest()
priv_key = CBitcoinSecret.from_secret_bytes(hash)

TXID = lx("cd49be9fd1dcda32627ebba528530e74dcbcd7756df4b9be506ec9ac9c5d0f6f")
vout_id = 0 #mb

tx_inputs = CMutableTxIn(COutPoint(TXID, vout_id))

tx_outputs = CMutableTxOut(1*COIN, CScript([OP_RETURN, b'123453']))

tx_inputs_scriptPubKey = CScript([OP_DUP, OP_HASH160, Hash160(priv_key.pub), OP_EQUALVERIFY, OP_CHECKSIG])

tx = CMutableTransaction([tx_inputs], [tx_outputs]) #raw unssigned

hash_to_sign = SignatureHash(tx_inputs_scriptPubKey, tx, 0, SIGHASH_ALL)

signed_hash = priv_key.sign(hash_to_sign) + bytes([SIGHASH_ALL])

tx_inputs.scriptSig = CScript([signed_hash, priv_key.pub])

VerifyScript(tx_inputs.scriptSig, tx_inputs_scriptPubKey, tx, 0, (SCRIPT_VERIFY_P2SH,))

print(b2lx(tx.serialize()))
