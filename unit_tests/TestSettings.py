import unittest

from test_settings import my_secret_test_password


class TestSettings(unittest.TestCase):

    def test_password_setting(self):
        result = my_secret_test_password
        self.assertEqual(result, 'secret_test_password1')


if __name__ == '__main__':
    unittest.main()
