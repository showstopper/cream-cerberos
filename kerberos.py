#! /usr/bin/python
# -*- coding: utf-8 -*-

import cream
import cream.ipc
import session
import json
from hashlib import sha256



class Kerberos(cream.Module):

    def __init__(self):

        cream.Module.__init__(self)
        self.my_session = session.Session()
          
    """ 
    @cream.ipc.method('ss', 'b')
    def add_keyring(self, name, password):

       # Password is held internally 
       # if not
    """    


    @cream.ipc.method('s', 'b')
    def delete_keyring(self, id):

        pass


    @cream.ipc.method('', 'aa(is)')
    def get_keyrings(self):

        return self.my_session.get_keyrings()


    @cream.ipc.method('ssi', 'b')
    def add_secret(self, key, value):

        self.my_session.add_secret(value, key)
    
    @cream.ipc.method('s', 's')
    def get_secret(self, key):

        # If the keyring holding the secret is locked, ask for a password.
        return self.my_session.get_secret(key)
        
    @cream.ipc.method('s', 'b')
    def delete_secret(self, key):

        self.my_session.delete_secret(key)


kerberos = Kerberos()
kerberos.main()
