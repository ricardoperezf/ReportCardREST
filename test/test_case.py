import sys

sys.path.append('/home/ricardo/ws/ReportCard/ReportCard')
import unittest
import api


class TestApi(unittest.TestCase):
    obtained_result = ""
    expected_result = ""

    def test_get_user_grade(self):
        obtained_result = api.hello_world()
        expected_result = 'Hello from Flask! Im RicDev'
        self.assertEqual(expected_result, obtained_result)


if __name__ == "__main__":
    unittest.main()
