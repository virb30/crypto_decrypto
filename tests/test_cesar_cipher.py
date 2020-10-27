from unittest import TestCase
from cesar_cipher import enc_cesar, dec_cesar, shift_cesar


class TestCesarCipher(TestCase):
    def test_encrypt(self):
        """Must encrypt a string using cesar cipher"""
        encryption = [(1, 'B'), (2, 'C'), (26, 'A'), (27, 'B')]
        with self.subTest():
            for salt, expected in encryption:
                self.assertEqual(enc_cesar('a', salt), expected)

    def test_decrypt(self):
        """Must decrypt a cesar cipher"""
        decryption = [(1, 'Z'), (2, 'Y'), (26, 'A'), (27, 'Z'), (28, 'Y')]
        with self.subTest():
            for salt, expected in decryption:
                self.assertEqual(dec_cesar('a', salt), expected)

    def test_shift(self):
        """Must show all cesar cipher decryption posibilites"""
        self.assertIsInstance(shift_cesar('d', 'a'), str)
