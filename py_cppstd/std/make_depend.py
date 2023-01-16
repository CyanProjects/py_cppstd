#  Copyright (c) 2022. 保留所有权利.
#  项目 - py_cppstd ==> ==> ==> ==> ==> ==> ==> ==> ==> =>>
#  @Author  : Cyan Changes(DELL)
#  @Email   : 1491326171@qq.com | cyq20100313cC@Gmail.com
#  @Edit    : 2022/7/13 下午8:49
#  @File    : make_depend.py
#  @CorpTime: 2022/7/26 上午11:16

from typing import Dict, Union, Any
from types import ModuleType

shared: dict = {}


def updates_depend(depends: Dict[str, Union[str, Union[str, Any]]]) -> None:
    shared.update(depends)


class _Depends:
    def __init__(self):
        self.stdns: ModuleType = None
        self.stdname = "py_cppstd.std"
        self.include = None

    def __getattr__(self, item):
        return shared[item]

    def __setattr__(self, key, value):
        shared[key] = value


depends = _Depends()
