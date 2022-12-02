import json
import encryption

# Reads data file and loads into json format
dataFile = open("data.json")
data = json.load(dataFile)

# Instance of Encrypt class
encryptionObj = encryption.Encrypt()

# Lists for Keys and Values of JSON
keysList = list(data.keys())
valuesList = list(data.values())

# Assemble encrypted JSON
encryptedJson = encryptionObj.assembleJson(keysList, valuesList, "encrypt")

# Save encrypted JSON to encrypted_data file. Simulates the sending of encrypted data
with open("encrypted_data.json", "w") as outfile:
    json.dump(encryptedJson, outfile)
    
# Opens encrypted data and loads into JSON format. Simulates the receiving of encrypted data
encFile = open("encrypted_data.json")
encData = json.load(encFile)

# Lists for Keys and Values of JSON
keysList = list(encData.keys())
valuesList = list(encData.values())

# Assemble decrypted JSON - back to original format
decryptedJson = encryptionObj.assembleJson(keysList, valuesList, "decrypt")

# Save decrypted JSON to decrypted_data file
with open("decrypted_data.json", "w") as outfile:
    json.dump(decryptedJson, outfile)