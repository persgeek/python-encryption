from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class Encryption:

    privateKey = None
    IV = None

    mode = AES.MODE_OFB

    def __init__(self, privateKey, IV):

        self.privateKey = privateKey[:16]
        self.IV = IV

    def encrypt(self, data):

        data = self.encode(data)

        encrypted = self.getCipher().encrypt(data)

        return self.decode(b64encode(encrypted))

    def decrypt(self, data):

        data = b64decode(data)

        decrypted = self.getCipher().decrypt(data)

        return self.decode(decrypted)

    def getCipher(self):

        return AES.new(self.encode(self.privateKey), self.mode, self.encode(self.IV))

    def encode(self, data):

        return data.encode('UTF-8')

    def decode(self, data):

        return data.decode('UTF-8')
