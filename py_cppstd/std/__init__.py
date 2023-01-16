#  Copyright (c) 2022. 保留所有权利.
#  项目 - py_cppstd ==> ==> ==> ==> ==> ==> ==> ==> ==> =>>
#  @Author  : Cyan Changes(DELL)
#  @Email   : 1491326171@qq.com | cyq20100313cC@Gmail.com
#  @Edit    : 2022/7/16 下午8:22
#  @File    : __init__.py
#  @CorpTime: 2022/7/26 上午11:16

import importlib
from types import ModuleType

import py_cppstd.exceptions as exceptions

from typing import List

class Std:
    def __init__(self):
        from .make_depend import depends
        depends.stdname = self.__module__
        depends.stdns = self
        depends.include = self.include
        self.libs = []

    def include(self, file: str) -> "ModuleType":
        try:
            for lib in self.libs:
                if lib.__lib__ == file:
                    return lib
            module = importlib.import_module(f'{self.__module__}.{file}')
            self.libs.append(module)
            return module
        except ModuleNotFoundError:
            raise exceptions.NoSuchLibraryError(f'Library {file} is not exist!')

    def __getattr__(self, item) -> "ModuleType":
        for lib in self.libs:
            if item in dir(lib):
                return eval(f'lib.{item}')

        raise NameError(f'No attr named {item}!')


__all__ = ['Std']
