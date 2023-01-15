#  Copyright (c) 2022. 保留所有权利.
#  项目 - py_cppstd ==> ==> ==> ==> ==> ==> ==> ==> ==> =>>
#  @Author  : Cyan Changes(DELL)
#  @Email   : 1491326171@qq.com | cyq20100313cC@Gmail.com
#  @Edit    : 2022/7/16 下午8:22
#  @File    : __init__.py
#  @CorpTime: 2022/7/26 上午11:16

import importlib

from .make_depend import shared

import py_cppstd.exceptions as exceptions

class std:
    def __init__(self):
        self.libs = []

    def include(self, file: str):
        try:
            for lib in self.libs:
                if lib.__lib__ == file:
                    return module
            make_depend.shared = {
                '__stdname__': self.__module__,
                '__stdns__': self,
                '_include': self.include
            }
            module = importlib.__import__(f'{self.__module__}.{file}', globals(), locals())
            self.libs.append(module)
            return module
        except ModuleNotFoundError:
            raise exceptions.NoSuchLibraryError(f'Library {file} is not exist!')

    def __getattr__(self, item):
        for lib in self.libs:
            if item in lib.__all__:
                return eval(f'lib.{item}')

        raise NameError(f'No attr named {item}!')

__all__ = ['std']