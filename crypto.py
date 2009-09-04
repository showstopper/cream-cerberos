#!/usr/bin/env python
# coding: utf-8


from Crypto.Cipher import AES
from hashlib import md5, sha256
import json
import base64

def hash_password(password):

    hash1 = sha256(password).hexdigest()
    return md5(hash1).hexdigest()

def fix_secret_length(secret):

    sec_length = len(secret) % 16
    if sec_length:
        secret = "".join((secret, " "*(16-sec_length)))
    return secret

def gen_key(password):

    return AES.new(password, AES.MODE_ECB)

def encrypt_secret(secret, password):

    key = gen_key(hash_password(password))
    cipher_string = create_cipher_string(secret)

    tmp = key.encrypt(fix_secret_length(cipher_string))
   
    return base64.b64encode(tmp)

def decrypt_secret(cipher, password):

    cipher_str = base64.b64decode(cipher.secret)
    key = gen_key(hash_password(password))
    tmp = key.decrypt(cipher_str)
    cipher_dict = unpack_cipher_string(tmp)
    
    return cipher_dict["sec"]
    
    #secret = base64.b64decode(cipher.secret)
def create_cipher_string(secret):

    sec_hash = md5(secret).hexdigest()
    return json.dumps({'hash':sec_hash, 'sec':secret})  

def unpack_cipher_string(cipher_string):

    
    return json.loads(cipher_string)

def verify_secret_content(cipher_dict):

    return cipher_dict["hash"] == md5(cipher_dict["sec"]).hexdigest()


