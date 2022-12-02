import string

class Encrypt:
    def __init__(self):
        # List for letters on alphabet
        self.alphabet = list(string.ascii_lowercase)

    def encrypt(self, inputList=[]):
        """
        Description:
            Encrypts elements of given list. Replace character by the character 5 positions ahead (eg. a -> f, x -> c) or adds 5 to integer (eg, 2 -> 7, 7 -> 12).

        Args:
            inputList (list, optional): List of elements (keys/values) to be encrypted. Defaults to [].

        Returns:
            _list_: List of encrypted elements
        """
        aux = ''
        encrypted = []
        letterIndex = 0
        
        # Loop to iterate through elements of the list
        for values in inputList:
            # Loop to iterate through letters of the elements
            for char in str(values):
                # If it's a number, adds 5
                if char.isnumeric():
                    aux += str(int(char) + 5)
                # If it's a letter, replace by the character 5 positions ahead
                else:
                    letterIndex = self.alphabet.index(char) + 5
                    if letterIndex > 25:        # treat case in which "5 letters ahead" surpasses letter 'z'
                        letterIndex -= 26
                    aux += self.alphabet[letterIndex]
            encrypted.append(aux)
            aux = ""
        return encrypted

    def decrypt(self, inputList=[]):
        """
        Description:
            Decrypts elements of given list. Replace character by the character 5 positions behind (eg. f -> a, c -> x) or subtracts 5 to integer (eg, 7 -> 2, 12 -> 7).

        Args:
            inputList (list, optional): List of elements (keys/values) to be decrypted. Defaults to [].

        Returns:
            _list_: List of decrypted elements
        """
        aux = ''
        decrypted = []
        letterIndex = 0
        flag = False
        
        # Loop to iterate through elements of the list
        for values in inputList:
            # Loop to iterate through characters of the elements
            for char in str(values):
                # If it's a number, subtracts 5
                if char.isnumeric():
                    if char == "1":         # checks if it's a double-digit number
                        flag = True
                        continue
                    if not flag:
                        aux += str(int(char) - 5)       # subtracts current number of 5
                    else:
                        aux += str(int("1" + char) - 5)     # subtracts double-digit number of 5
                    flag = False
                        
                # If it's a letter, replace by the character 5 positions behind
                else:
                    letterIndex = self.alphabet.index(char) - 5
                    if letterIndex < 0:        # treat case in which "5 letters behind" is before letter 'a'
                        letterIndex += 26
                    aux += self.alphabet[letterIndex]
            decrypted.append(aux)
            aux = ""
        return decrypted

    def assembleJson(self, keysList, valuesList, type="encrypt"):
        """
        Description:
            Assemble JSON after encryption or decryption of keys and values.

        Args:
            keysList (list): encrypted or decrypted list of keys
            valuesList (list): encrypted or decrypted list of values
            type (str): Type of operation executed before. Defaults to "encrypt".

        Returns:
            _dict_: Returns assembled JSON
        """                
        # Initialize auxiliary lists
        keys = []
        params = []
        secLevelKeys = []
        secLevelValues = []
        
        if type == "encrypt":
            # Encrypt first level keys
            keys = self.encrypt(keysList)

            # Loop for encrypting second level keys and values
            for values in valuesList:
                encList = list(values.keys())
                secLevelKeys.append(self.encrypt(encList))
                
                encList = list(values.values())
                secLevelValues.append(self.encrypt(encList))
            # Loop to turn second level keys and values back to dict
            for a,b in zip(secLevelKeys, secLevelValues):
                params.append(dict(zip(a,b)))

            # Assemble data to original dictionary format
            fullJson = dict(zip(keys, params))
                
        elif type == "decrypt":
            # Decrypt first level keys
            keys = self.decrypt(keysList)

            # Loop for decrypting second level keys and values
            for values in valuesList:
                decList = list(values.keys())
                secLevelKeys.append(self.decrypt(decList))
                
                decList = list(values.values())
                secLevelValues.append(self.decrypt(decList))
            
            # Loop to turn second level keys and values back to dict
            for a,b in zip(secLevelKeys, secLevelValues):
                params.append(dict(zip(a,b)))

            # Assemble data to original dictionary format
            fullJson = dict(zip(keys, params))

        return fullJson        
