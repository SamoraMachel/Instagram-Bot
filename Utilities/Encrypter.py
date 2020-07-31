# %% Importing the neccessary packages 
import pickle
import cryptography.fernet as xcrypt
import json
import os


# %% Encrypts data to a file 
def Encrypt(data: any, KeyFile: __file__ = ".Data/.encryptionKey", DataFile: __file__ = ".Data/.encrypted" ) -> None:

    # Adds the directory .Data incase it is not present 
    if not os.path.exists("./.Data"):
        os.mkdir(".Data")
    # check if data is a dictionary and convert it
    # to a json type otherwise let it reamin as string
    if (type(data) == dict):
        data = json.dumps(data)
        
    # generate the key and then dump the key to a file 
    key = xcrypt.Fernet.generate_key()
    keyFile = open(KeyFile, 'wb')
    pickle.dump(key, keyFile)
    keyFile.close()

    # Use the key generated to encrypt the data 
    encryptionType = xcrypt.Fernet(key)

    # Change the data to BYTES since the eencryption supports
    # only bytes
    dataBytes = bytes(str(data), 'utf-8')
    encryptedData = encryptionType.encrypt(b'%b'%(dataBytes))

    # dumping the data in a file 
    cryptoFile = open(DataFile, 'wb')
    pickle.dump(encryptedData, cryptoFile)


# %%
