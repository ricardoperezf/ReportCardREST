import sys

sys.path.append('/home/ricardo/ws/ReportCard/ReportCard/reportcard/endpoints')
import grades_endpoint
import helloworld_endpoint


class TestApi(unittest.TestCase):
    obtained_result = ""
    expected_result = ""

    def test_get_user_grade(self):
        obtained_result = helloworld_endpoint.hello_world()
        expected_result = 'Hello from Flask! Im RicDev'
        self.assertEqual(expected_result, obtained_result)

    def test_get_grades(self):
        obtained_result = grades_endpoint.register_new_user()
        expected_result = 'Hello from Flask! Im RicDev'
        self.assertEqual(expected_result, obtained_result)


if __name__ == "__main__":
    unittest.main()
