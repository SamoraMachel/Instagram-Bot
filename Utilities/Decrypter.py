# %% Importing the neccessary packages 
import pickle
import cryptography.fernet as xcrypt
import json

# %% Decrypts the data from the files
def Decrypt(KeyFile :__file__ = ".Data/.encryptionKey", DataFile :__file__ = ".Data/.encrypted") -> dict or str :
    # get the ecryption key
    keyFile = open(KeyFile, 'rb')
    keyBytes = pickle.load(keyFile) # the unpickled data is in bytes
    key = str(keyBytes, 'utf-8')
    keyFile.close()
    
    # get the Encrypted data
    dataFile = open(DataFile, 'rb')
    dataBytes = pickle.load(dataFile)  # the unpickled data is in bytes
    dataFile.close()
    
    # Decrypt the data
    encryptionType = xcrypt.Fernet(key)
    data = encryptionType.decrypt(dataBytes)
    dataString = str(data, 'utf-8')
    return dataString

# %% check if its a json file 
def isJson(data: dict) -> bool:
    try:
        jsonData = json.loads(data)
        return True
    except:
        return False

# %% Gets the encrypted data 
def getData(keyFile :__file__ = ".Data/.encryptionKey", dataFile :__file__ = ".Data/.encrypted") -> dict or str:
    data = Decrypt(keyFile, dataFile)
    if isJson(data):
        fetchedData = json.loads(data)
        return fetchedData  # returns a dictionary
    else:
        return data         # returns a string 
    

# %%
