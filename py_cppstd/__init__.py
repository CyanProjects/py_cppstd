import importlib

import py_cppstd.exceptions as exceptions
import py_cppstd.cppstd.iostream

class std:
    @staticmethod
    def load():
        import inspect
        import io
        import tokenize

        call_frame = inspect.currentframe().f_back
        import objprint.frame_analyzer as frame_a  # 再再白嫖一下应该还是没事吧(

        call = frame_a.FrameAnalyzer().get_executing_function_call_str(call_frame)
        func_call_io = io.StringIO(call)
        var_name: str = None
        tokens = tokenize.generate_tokens(func_call_io.readline)
        first = True
        var = None
        sub = ''
        tokens = tuple(tokens)
        for token in tokens:
            if token.type == tokenize.NAME and token.string == 'load':
                sub = sub[:-1]
                break
            if first:
                var = token.string.strip()
                first = False
            else:
                sub += token.string
        exec(f'{var}{sub}={var}{sub}()', call_frame.f_globals, call_frame.f_locals)

    def __init__(self):
        self.libs = []

    def include(self, file: str):
        try:
            module = importlib.import_module(f'.cppstd.{file}', package='py_cppstd')
            module.__man__ = self
            self.libs.append(module)
        except ModuleNotFoundError:
            raise exceptions.NoLibraryError(f'Library {file} is not exist!')


    def __getattr__(self, item):
        for lib in self.libs:
            if item in lib.__all__:
                return eval(f'lib.{item}')

        raise NameError(f'No attr named {item}!')

__all__ = ['std']