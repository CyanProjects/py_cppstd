import py_cppstd.cppstd.iostream

import inspect
import objprint.frame_analyzer as frame_a # 再白嫖一下应该还是没事吧(

def freopen(Filename: str, mode: str, stream: py_cppstd.cppstd.iostream._iostream) -> bool:
    try:
        import io, tokenize
        new_stream = open(Filename, mode, encoding=stream.encoding)
        call_frame = inspect.currentframe().f_back
        args = frame_a.FrameAnalyzer().get_args(call_frame)
        arg_stream_io = io.StringIO(args[2])
        tokens = tokenize.generate_tokens(arg_stream_io.readline)
        sub = ''
        tokens = tuple(tokens)
        var = tokens[0].string
        for token in tokens[1:]:
        sub += token.string
        exec(f'{var}{sub}={new_stream}', call_frame.f_globals, call_frame.f_locals)
        return True
    except:
        return False

__all__ = ['freopen']