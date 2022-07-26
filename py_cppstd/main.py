#  Copyright (c) 2022. 保留所有权利.
#  项目 - py_cppstd ==> ==> ==> ==> ==> ==> ==> ==> ==> =>>
#  @Author  : Cyan Changes(DELL)
#  @Email   : 1491326171@qq.com | cyq20100313cC@Gmail.com
#  @Edit    : 2022/7/16 下午10:02
#  @File    : main.py
#  @CorpTime: 2022/7/26 上午11:16

from py_cppstd import std

if __name__ == '__main__':
    std = std()
    std.include('iostream')
    std.cout << "enter sth. here\n"
    sth: str = ''
    std.cin >> sth
    std.cout << sth << std.endl