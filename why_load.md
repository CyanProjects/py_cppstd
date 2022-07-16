## Why std become instance after std.load()
This is because `std.load()` is using black magic to modify local variables.
## What did `std.load()` do
`std.load` is a static func in class std.  
`std.load()` get call_frame first.  
Next, create a *std instance* and 
set f_locals[var] to it.
### Achieve

**Go to** 
<a href='py_cppstd/__init__.py'> py_cppstd/\_\_init\_\_.py </a>
