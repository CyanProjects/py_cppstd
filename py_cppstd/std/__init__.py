#  Copyright (c) 2022. 保留所有权利.
#  项目 - py_cppstd ==> ==> ==> ==> ==> ==> ==> ==> ==> =>>
#  @Author  : Cyan Changes(DELL)
#  @Email   : 1491326171@qq.com | cyq20100313cC@Gmail.com
#  @Edit    : 2022/7/16 下午8:22
#  @File    : __init__.py
#  @CorpTime: 2022/7/26 上午11:16

import importlib

import py_cppstd.exceptions as exceptions

class std:
    def __init__(self):
        self.libs = []

    def include(self, file: str):
        try:
            module = importlib.import_module(f'.std.{file}', package='py_cppstd')
            module.__man__ = self
            self.libs.append(module)
        except ModuleNotFoundError:
            raise exceptions.NoSuchLibraryError(f'Library {file} is not exist!')

    def __getattr__(self, item):
        for lib in self.libs:
            if item in lib.__all__:
                return eval(f'lib.{item}')

        raise NameError(f'No attr named {item}!')

__all__ = ['std']
#  Copyright (c) 2022. 保留所有权利.
#  项目 - py_cppstd ==> ==> ==> ==> ==> ==> ==> ==> ==> =>>
#  @Author  : Cyan Changes(DELL)
#  @Email   : 1491326171@qq.com | cyq20100313cC@Gmail.com
#  @Edit    : 2022/7/13 下午8:45
#  @File    : __init__.py
#  @CorpTime: 2022/7/26 上午11:16