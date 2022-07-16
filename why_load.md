## Why std become instance after std.load()
`std.load` is a static func in class std.  
`std.load()` is using black magic.
## What did `std.load()` do
`std.load()` get call_frame first.  
then, create a *std instance* and 
set f_locals[var] to it.
### Achieve

*Go to *
<a href='py_cppstd/__init__.py'> py_cppstd/__init__.py </a>
