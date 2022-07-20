import unittest
from py_cppstd import std as cppstd, exceptions

class TestStd(unittest.TestCase):
    def test_wrong_includes(self):
        std = cppstd()
        with self.assertRaises(exceptions.NoLibraryError):
            std.include('iosteam')
            std.include('stdbuggy')

    def test_includes(self):
        std = cppstd()
        std.include('iostream')
        self.assertIsInstance(std, object)

    def test_iostream(self):
        std = cppstd()
        std.include('iostream')
        self.assertIs(std.cout << 114514 << '\n', std.cout)  # Test integer
        self.assertIs(std.cout << '114514', std.cout)  # Test string


if __name__ == '__main__':
    unittest.main()
