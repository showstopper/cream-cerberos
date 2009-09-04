#!/usr/bin/env python
#coding: utf-8 


import crypto
import database
import secure_store

class NoKeyringSet(Exception):
    pass

class Session(object):

    def __init__(self):
        
        
        self.storage = secure_store.SecureStorage()
        self.db = database.Database()
        self.current_keyring = ""

    def add_secret(self, secret, sec_id, attrib):

        if not self.current_keyring:
            raise NoKeyringSet()
            return()        
        cipher = crypto.encrypt_secret(secret, self.storage.get(self.current_keyring))
        self.db.add_secret(cipher, sec_id, self.current_keyring,attrib)

    def get_secret(self, sec_id):

        cipher = self.db.get_secret(sec_id, self.current_keyring)
        if cipher:
            return crypto.decrypt_secret(cipher, self.storage.get(self.current_keyring))
        else:
            return False

    def delete_secret(self, sec_id):
        
        self.db.delete_secret(sec_id, self.current_keyring)

    def set_current_keyring(self, keyring_id, password):
        self.current_keyring = keyring_id
        self.storage.store(password, self.current_keyring)

    def get_keyrings(self):

        return self.db.get_keyrings()
        
        
        



        
        
        



