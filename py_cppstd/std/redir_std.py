#  Copyright (c) 2022. 保留所有权利.
#  项目 - py_cppstd ==> ==> ==> ==> ==> ==> ==> ==> ==> =>>
#  @Author  : Cyan Changes(DELL)
#  @Email   : 1491326171@qq.com | cyq20100313cC@Gmail.com
#  @Edit    : 2022/7/16 下午9:12
#  @File    : redir_std.py
#  @CorpTime: 2022/7/26 上午11:16

import inspect

import objprint.frame_analyzer as frame_a  # 再白嫖一下应该还是没事吧(
import py_cppstd.std.iostream


def freopen(Filename: str, mode: str,
            stream: py_cppstd.cppstd.iostream._iostream) -> bool:
    try:
        import io
        import tokenize
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
        exec(f'{var}{sub}={new_stream}',
             call_frame.f_globals, call_frame.f_locals)
        return True
    except Exception:
        return False


__all__ = ['freopen']
