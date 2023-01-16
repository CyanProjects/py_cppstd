from .make_depend import depends

from sys import __stdout__, __stdin__, __stderr__
from ctypes import c_char
import io
from typing import Self

import objprint.frame_analyzer as frame_a
from objprint import objstr

ios = depends.include('ios')
depends.include('iodirect')


# class not complete now
# only simple (cout, cin) can use
class _IOStream:
    __split__ = (' ', '\n')  # pass chars

    # init io.TextIOWrapper
    def __init__(self, _internal_io_obj: io.TextIOWrapper):
        self._std_iostream = _internal_io_obj
        self.o_trunc = ios.o_trunc
        self.o_out = ios.o_out
        self.o_in = ios.o_out

    def __lshift__(self, data: type) -> Self:
        """
        using cout << val
        put value in val to stdout
        :param data: got and attr __str__ or magic method __lshift__
        :return: self
        """
        if self._std_iostream.writable():
            try:
                self._std_iostream.write(data.__str__())
            except (AttributeError, IOError, ValueError):
                try:
                    data.__dict__["__lshift__"](self, data)
                except AttributeError:
                    raise NotImplementedError(
                        "Can't find magic method __lshift__!"
                    )
        else:
            raise IOError("un-writable iostream!")
        return self

    def seekp(self, index: int, sdir: ios.seekdir) -> int:
        if self._std_iostream.seekable():
            if sdir == ios.beg:
                return self._std_iostream.seek(index, __whence=io.SEEK_SET)
            elif sdir == ios.cur:
                return self._std_iostream.seek(index, __whence=io.SEEK_CUR)
            elif sdir == ios.end:
                return self._std_iostream.seek(index, __whence=io.SEEK_END)
            else:
                raise ValueError(f"Invalid Seekdir {objstr(sdir)}!")
        else:
            raise IOError("un-seekable iostream!")

    def tellp(self) -> int:
        return self._std_iostream.tell()

    def flush(self) -> None:
        self._std_iostream.flush()

    def good(self) -> bool:
        return self._std_iostream.closed

    def __rshift__(self, mutable: type) -> Self:
        """
        using std.cin >> var
        read var in stdout and put value into var
        :param mutable: a mutable object
        :return: self
        """
        if self._std_iostream.readable():
            str1: str = ''
            char: c_char = ''

            while char not in self.__class__.__split__:
                char = self._std_iostream.read(1)
                str1 += char

            for _strips in self.__class__.__split__:
                str1 = str1.strip(_strips)

            try:
                if isinstance(mutable, str):
                    mutable = str1
                else:
                    mutable = eval(str1)
                import inspect
                import tokenize
                call_frame = inspect.currentframe().f_back
                call = frame_a.FrameAnalyzer() \
                    .get_executing_function_call_str(call_frame)
                func_call_io = io.StringIO(call)
                tokens = tokenize.generate_tokens(func_call_io.readline)
                next_var = False
                var = ''
                tokens = tuple(tokens)
                for token in tokens:
                    if (token.type == tokenize.NAME or
                        token.type == tokenize.OP) \
                            and (token.string == '__rshift__'
                                 or token.string == '>>'):
                        next_var = True
                        continue
                    if next_var:
                        var += token.string
                if isinstance(mutable, str):
                    exec(f'{var}="{mutable}"',
                         call_frame.f_globals, call_frame.f_locals)
                else:
                    exec(f'{var}={mutable}',
                         call_frame.f_globals, call_frame.f_locals)
            except AttributeError:
                try:
                    mutable.__dict__["__rshift__"](self, mutable)
                except KeyError:
                    raise NotImplementedError(
                        "Can't find magic method __rshift__ "
                        "or type isn't mutable"
                    )
            return self
        else:
            raise IOError("un-readable iostream!")

    # @property
    # def inter_iostream(self):
    #     return self._std_iostream


class _Flush:
    @staticmethod
    def __lshift__(stream: "_IOStream", other):
        stream.flush()


class _EndL:
    @staticmethod
    def __lshift__(stream: "_IOStream", other):
        (stream << '\n').flush()


cout = _IOStream(_internal_io_obj=__stdout__)
cin = _IOStream(_internal_io_obj=__stdin__)
cerr = _IOStream(_internal_io_obj=__stderr__)

flush = _Flush
EndL = _EndL

__stdns__ = None
__lib__ = "iostream"


class CreateAll:
    all = ['cin', 'cout', 'cerr', 'flush', 'endl', "__lib__", "_IOStream"]

    def __getitem__(self, item):
        return self.__class__.all[item]


__all__ = CreateAll()
