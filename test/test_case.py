import unittest
import api


class TestApi(unittest.TestCase):
    def test_get_user_grade(self):
        obtained_result = user.username
        expected_result = "hola"
        self.assertEqual(expected_result, obtained_result)


if __name__ == "__main__":
    unittest.main()
