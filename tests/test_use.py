#  Copyright (c) 2022. 保留所有权利.
#  项目 - py_cppstd ==> ==> ==> ==> ==> ==> ==> ==> ==> =>>
#  @Author  : Cyan Changes(DELL)
#  @Email   : 1491326171@qq.com | cyq20100313cC@Gmail.com
#  @Edit    : 2022/7/20 下午1:16
#  @File    : test_use.py
#  @CorpTime: 2022/7/26 上午11:16

import unittest
from py_cppstd import std as cppstd, exceptions


class TestStd(unittest.TestCase):
    def test_wrong_includes(self):
        with self.assertRaises(exceptions.NoSuchLibraryError):
            std.include('iosteam')
            std.include('stdbuggy')

    def test_includes(self):
        std.include('iostream')
        self.assertIsInstance(std, object)

    def test_iostream(self):
        std.include('iostream')
        self.assertIs(std.cout << 114514 << '\n', std.cout)  # Test integer
        self.assertIs(std.cout << '114514', std.cout)  # Test string


if __name__ == '__main__':
    unittest.main()
