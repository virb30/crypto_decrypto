from unittest import TestCase
from base64_cipher import enc_base64, dec_base64


class TestBase64(TestCase):
    def test_encrypt(self):
        """Must encrypt a string using base64"""
        encryption = [('a', 'YQ=='), ('ab', 'YWI='), ('abc', 'YWJj')]
        with self.subTest():
            for input_, expected in encryption:
                self.assertEqual(enc_base64(input_), expected)

    def test_decrypt(self):
        """Must decrypt a base64 string"""
        decryption = [('YQ==', 'a'), ('YWI=', 'ab'), ('YWJj', 'abc')]
        with self.subTest():
            for input_, expected in decryption:
                self.assertEqual(dec_base64(input_), expected)
