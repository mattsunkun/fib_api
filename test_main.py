import unittest

from fastapi.testclient import TestClient

from main import FIB_PATH, MAX_N, MIN_N, app

client = TestClient(app)

class TestFibonacciAPI(unittest.TestCase):

    def _test_fibonacci(self, n:int, result:int):
        response = client.get(f"{FIB_PATH}?n={n}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], result)
    def test_fibonacci_1(self):self._test_fibonacci(1, 1)
    def test_fibonacci_2(self):self._test_fibonacci(2, 1)
    def test_fibonacci_3(self):self._test_fibonacci(3, 2)
    def test_fibonacci_4(self):self._test_fibonacci(4, 3)
    def test_fibonacci_5(self):self._test_fibonacci(5, 5)
    def test_fibonacci_10(self):self._test_fibonacci(10, 55)
    def test_fibonacci_100(self):self._test_fibonacci(100, 354224848179261915075)


    def test_min_boundary(self):
        response = client.get(f"{FIB_PATH}?n={MIN_N}")
        self.assertEqual(response.status_code, 200)

    def test_max_boundary(self):
        response = client.get(f"{FIB_PATH}?n={MAX_N}")
        self.assertEqual(response.status_code, 200)

    def test_below_min(self):
        response = client.get(f"{FIB_PATH}?n={MIN_N - 1}")
        self.assertEqual(response.status_code, 400)
        self.assertIn("nは", response.json()["detail"])

    def test_above_max(self):
        response = client.get(f"{FIB_PATH}?n={MAX_N + 1}")
        self.assertEqual(response.status_code, 400)
        self.assertIn("nは", response.json()["detail"])

    def test_method_not_allowed(self):
        response = client.post(FIB_PATH, json={"n": 5})
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json()["error"], "Method Not Allowed")

    def test_not_found(self):
        response = client.get("/undefined-path")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "404 Not Found")

    def test_missing_parameter(self):
        response = client.get(FIB_PATH)
        self.assertEqual(response.status_code, 422)
        self.assertIn("detail", response.json())

if __name__ == "__main__":
    unittest.main()
