## Python C++ std iostream
Using C++ std lib iostream in py  

[![OSCS Status](https://www.oscs1024.com/platform/badge/Chinese-Cyq20100313/py_cppstd.svg?size=small)](https://www.oscs1024.com/project/Chinese-Cyq20100313/py_cppstd?ref=badge_small)

### Installtion
    pip install py_cppstd

### Import
    from py_cppstd import _std  

### Example

    std.include('iostream')
    std.cout << 114514 << std.endl # output 114514 <newline>
    num: int  
    std.cin >> num # read a int
