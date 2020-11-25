import unittest

from identity_number_validator import identity_number_validator


class TestEcuador(unittest.TestCase):
    def test_valid_identity_number(self):
        """
        Should return True if a valid identity number is passed
        """
        self.assertEqual(identity_number_validator("0922553508", "EC"), True)


if __name__ == "__main__":
    unittest.main()