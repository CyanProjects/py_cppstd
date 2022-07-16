from py_cppstd import std
std.load()
std.include('iostream')
std.cout << "enter sth. here\n"
sth: str = ''
std.cin >> sth
std.cout << sth << std.endl