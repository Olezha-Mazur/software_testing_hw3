import json
import unittest
from urllib.request import urlopen


class JsonPlaceholderApiTest(unittest.TestCase):
    def test_todo_endpoint_returns_expected_record(self):
        with urlopen("https://jsonplaceholder.typicode.com/todos/1", timeout=15) as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(response.headers.get_content_type(), "application/json")
            payload = json.load(response)

        self.assertEqual(payload["id"], 1)
        self.assertEqual(payload["userId"], 1)
        self.assertIsInstance(payload["title"], str)
        self.assertTrue(payload["title"])
        self.assertIs(payload["completed"], False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
