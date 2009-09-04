#!/usr/bin/env python
#coding: utf-8

import ctypes

LIBNAME = "C/libsecuremem.so"

class SecureStorage(object):

    def __init__(self):
        
        self.lib = ctypes.CDLL(LIBNAME)
        

    def store(self, secret, secret_id):

        secret_buf = ctypes.create_string_buffer(secret)
        secret_id_buf = ctypes.create_string_buffer(secret_id)
        self.lib.store(secret_buf, secret_id_buf)
        self.lib.zero_me(secret_buf)
        self.lib.zero_me(secret_id_buf)

    def get(self, secret_id):

        buf = ctypes.create_string_buffer(secret_id)
        res = self.lib.get(buf)
        self.lib.zero_me(buf)
        return ctypes.c_char_p(res).value
        
    def delete(self, secret_id):

        buf = ctypes.create_string_buffer(secret_id)
        self.lib.delete(buf)
        self.lib.zero_me(buf)

if __name__ == '__main__':
    store = SecureStorage()
    store.store("secret", "id")
    print store.get("id")
    store.delete("id")
    print store.get("id")
