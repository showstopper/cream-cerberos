#!/usr/bin/env python
# coding: utf-8 

import json
import session
import database

def main():

        
    keyring_id = "Test_Keyring"
    password = "Test_Passwort"
    #storage = SecureStorage()
    my_session = session.Session()
    my_session.set_current_keyring(keyring_id, password)
    
    secret = "I've got a secret"
    sec_id = "Chelsea_Smile"
    attrib1 = json.dumps({"user":"songe", "server":"blub.org"})
    sec_id2 = "Glasgow_Smile"
    try:
        my_session.add_secret(secret, sec_id, attrib1)
    except database.NotUnique:
        pass
    
    my_session.add_secret(secret[0:4], sec_id2, attrib1)
    print my_session.get_secret("Chelsea_Smile")
    print my_session.get_secret("Glasgow_Smile")
    my_session.delete_secret("Glasgow_Smile")

    print my_session.get_secret("Glasgow_Smile")
    print my_session.get_keyrings()

    
if __name__ == '__main__':
    main()
    


