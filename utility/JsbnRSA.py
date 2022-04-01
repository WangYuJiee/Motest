import base64
import json

from Crypto.PublicKey import RSA
from Crypto.Util.py3compat import tobytes
from flask import session
from jsbn import RSAKey


class JsbnRSA:
    """ To decrypt JS encryption data

    """

    def __init__(self, key, is_public=False):
        """ use Crypto RSA to import private_key, use JsbnRSA to decrypt

        :param private_key:
        """
        self.rsa = RSA.importKey(key)
        self.jsbn_rsa = RSAKey()
        self.jsbn_rsa.n = self.rsa.n
        self.jsbn_rsa.e = self.rsa.e
        if not is_public:
            self.jsbn_rsa.d = self.rsa.d
            self.jsbn_rsa.p = self.rsa.p
            self.jsbn_rsa.q = self.rsa.q

    def decrypt(self, encrypted):
        """

        :param encrypted: str
        :return:
        """
        decoded = base64.b64decode(tobytes(encrypted)).hex()
        return self.jsbn_rsa.decrypt(decoded)

    def encrypt(self, text):
        """

        :param text: str
        :return:
        """
        encrypted = self.jsbn_rsa.encrypt(text)
        return base64.b64encode(bytearray.fromhex(encrypted)).decode('latin-1')


def regenerate_rsa_keys(resp):
    private_key = RSA.generate(1024)
    public_key = private_key.publickey()
    public_key_str = public_key.exportKey().decode('latin-1')
    resp.set_cookie('public_key', json.dumps(public_key_str),
                    max_age=60 * 60 * 24 * 7)
    session['private_key'] = private_key.exportKey()
