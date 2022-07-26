#  Copyright (c) 2022. 保留所有权利.
#  项目 - py_cppstd ==> ==> ==> ==> ==> ==> ==> ==> ==> =>>
#  @Author  : Cyan Changes(DELL)
#  @Email   : 1491326171@qq.com | cyq20100313cC@Gmail.com
#  @Edit    : 2022/7/13 下午6:16
#  @File    : ios_base.py
#  @CorpTime: 2022/7/26 上午11:16

# <ios_base.h>
from enum import Enum

__INT_MAX__ = 2 ** 31 - 1


class _Ios_Fmtflags(Enum):
    _S_boolalpha = 1 << 0
    _S_dec = 1 << 1
    _S_fixed = 1 << 2
    _S_hex = 1 << 3
    _S_internal = 1 << 4
    _S_left = 1 << 5
    _S_oct = 1 << 6
    _S_right = 1 << 7
    _S_scientific = 1 << 8
    _S_showbase = 1 << 9
    _S_showpoint = 1 << 10
    _S_showpos = 1 << 11
    _S_skipws = 1 << 12
    _S_unitbuf = 1 << 13
    _S_uppercase = 1 << 14
    _S_adjustfield = _S_left | _S_right | _S_internal
    _S_basefield = _S_dec | _S_oct | _S_hex
    _S_floatfield = _S_scientific | _S_fixed
    _S_ios_fmtflags_end = 1 << 16
    _S_ios_fmtflags_max = __INT_MAX__
    _S_ios_fmtflags_min = ~__INT_MAX__


class _Ios_Openmode(Enum):
    _S_app = 1 << 0
    _S_ate = 1 << 1
    _S_bin = 1 << 2
    _S_in = 1 << 3
    _S_out = 1 << 4
    _S_trunc = 1 << 5
    _S_ios_openmode_end = 1 << 6
    _S_ios_openmode_max = __INT_MAX__
    _S_ios_openmode_min = ~__INT_MAX__


class _Ios_Iostate(Enum):
    _S_goodbit = 0
    _S_badbit = 1 << 0
    _S_eofbit = 1 << 1
    _S_failbit = 1 << 2
    _S_ios_iostate_end = 1 << 3
    _S_ios_iostate_max = __INT_MAX__
    _S_ios_iostate_min = ~__INT_MAX__


class _Ios_Seekdir(Enum):
    _S_beg = 0,
    _S_cur = 1,
    _S_end = 2,
    _S_ios_seekdir_end = 1 << 16


fmtFlags = _Ios_Fmtflags

boolalpha: fmtFlags = fmtFlags._S_boolalpha

dec: fmtFlags = fmtFlags._S_dec

fixed: fmtFlags = fmtFlags._S_fixed

hex: fmtFlags = fmtFlags._S_hex

internal: fmtFlags = fmtFlags._S_internal

left: fmtFlags = fmtFlags._S_left

oct: fmtFlags = fmtFlags._S_oct

right: fmtFlags = fmtFlags._S_right

scientific: fmtFlags = fmtFlags._S_scientific

showbase: fmtFlags = fmtFlags._S_showbase

showpoint: fmtFlags = fmtFlags._S_showpoint

showpos: fmtFlags = fmtFlags._S_showpos

skipws: fmtFlags = fmtFlags._S_skipws

unitbuf: fmtFlags = fmtFlags._S_unitbuf

uppercase: fmtFlags = fmtFlags._S_uppercase

adjustfield: fmtFlags = fmtFlags._S_adjustfield

basefield: fmtFlags = fmtFlags._S_basefield

floatfield: fmtFlags = fmtFlags._S_floatfield

iostate = _Ios_Iostate

badbit: iostate = iostate._S_badbit

eofbit: iostate = iostate._S_eofbit

failbit: iostate = iostate._S_failbit

goodbit: iostate = iostate._S_goodbit

openmode = _Ios_Openmode

o_app: openmode = openmode._S_app

o_ate: openmode = openmode._S_ate

o_bin: openmode = openmode._S_bin

# openmode prefix o_ beacause in is keyword in py
o_in: openmode = openmode._S_in

o_out: openmode = openmode._S_out

o_trunc: openmode = openmode._S_trunc

seekdir = _Ios_Seekdir

beg: seekdir = seekdir._S_beg

cur: seekdir = seekdir._S_cur

end: seekdir = seekdir._S_end
