class Encryptor:

    def __init__(self):
        self.crypto_key = "g"
        self.mode = 1

    def _xor_help(self,value: str):
        array_xor = "".join([chr(ord(self.crypto_key) ^ ord(i) + (65 * self.mode)) for i in value])
        return array_xor

    def xor(self,data: dict):
        encrypted_data = {}
        for key_window,value in data["data"].items():
            new_window = self._xor_help(key_window,)
            encrypted_data[new_window] = {}
            for key_date,value_str in value.items():
                new_date = self._xor_help(key_date,)
                new_str = self._xor_help(value_str,)
                encrypted_data[new_window][new_date] = new_str
        return encrypted_data

    def _decryptor_xor(self,data):
        self.mode = -1
        decrypted_data = self.xor(data)
        self.mode = 1
        return  decrypted_data

