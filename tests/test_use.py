import unittest
import py_cppstd as cppstd
from py_cppstd import exceptions

class TestStd(unittest.TestCase):
    def test_wrong_includes(self):
        std = cppstd.std()
        with self.assertRaises(exceptions.NoLibraryError):
            std.include('iosteam')
            std.include('stdbuggy')

    def test_includes(self):
        std = cppstd.std()
        std.include('iostream')
        self.assertIsInstance(std, object)

    def test_iostream(self):
        std = cppstd.std()
        std.include('iostream')
        self.assertIs(std.cout << 114514 << '\n', std.cout)  # Test integer
        self.assertIs(std.cout << '114514', std.cout)  # Test string


if __name__ == '__main__':
    unittest.main()
