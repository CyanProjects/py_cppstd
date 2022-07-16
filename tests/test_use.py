import unittest


class TestStd(unittest.TestCase):
    def test_init(self):
        from py_cppstd import std

    def test_loads(self):
        from py_cppstd import std
        tp_std = type(std)
        std.load()
        del std
        import py_cppstd
        py_cppstd.std.load()

    def test_wrong_includes(self):
        from py_cppstd import std, exceptions
        with self.assertRaises(exceptions.NoLibraryError):
            std.include('iosteam')
            std.include('stdbuggy')

    def test_includes(self):
        from py_cppstd import std
        std = std()
        std.include('iostream')
        self.assertIsInstance(std, object)

    def test_iostream(self):
        from py_cppstd import std
        std = std()
        std.include('iostream')
        self.assertIs(std.cout << 114514 << '\n', std.cout) # Test integer
        self.assertIs(std.cout << '114514', std.cout) # Test string


if __name__ == '__main__':
    unittest.main()
