#!/usr/bin/env python
# coding: utf-8


import json
import shelve

FILENAME = "password.db"

class NotUnique(Exception):
    pass

def gen_db_str(sec_id, keyr_id):

    return "".join((sec_id, "|", keyr_id))

class Database(object):

    def __init__(self):

        self.db = shelve.open(FILENAME)
        
    def add_secret(self, secret, sec_id, keyr_id, attrib):

        sec = Secret(secret, sec_id, keyr_id, attrib)
        db_str = gen_db_str(sec_id, keyr_id)
        if self.db.get(db_str):
            raise NotUnique()
        else:
            self.db[db_str] = sec

    def get_secret(self, sec_id, keyr_id):

        db_str = gen_db_str(sec_id, keyr_id)
        return self.db.get(db_str)

    def delete_secret(self, sec_id, keyr_id):

        db_str = gen_db_str(sec_id, keyr_id)
        del self.db[db_str]

    def get_keyrings(self):

        return [key.split('|')[1] for key in self.db.keys()]
        



 

class Secret(object):

    def __init__(self, secret, sec_id, keyring_id, attrib):

        self.secret = secret
        self.sec_id = sec_id
        self.keyring_id = keyring_id
        self.attrib = attrib
