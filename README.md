## Python C++ std iostream
Using C++ std lib iostream in py  

[![OSCS Status](https://www.oscs1024.com/platform/badge/Chinese-Cyq20100313/py_cppstd.svg?size=small)](https://www.oscs1024.com/project/Chinese-Cyq20100313/py_cppstd?ref=badge_small)

### Installtion
    pip install py_cppstd

### Import
    from py_cppstd import std  
__then__:  
`std.load()` 
[variables are different after uses?](why_load.md)  
__or__  
`std = std()`

### *iostream* Usage

**recommend** to use ***;*** when end line.  

    std.include('iostream') # include <iostream>  
    # outputs 114514 and '\n' and flush the stream  
    std.cout << 114514 << std.endl  
    num: int  
    std.cin >> num # input a number to num
