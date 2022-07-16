from py_cppstd import std

if __name__ == '__main__':
    std = std()
    std.include('iostream')
    std.cout << "enter sth. here\n"
    sth: str = ''
    std.cin >> sth
    std.cout << sth << std.endl