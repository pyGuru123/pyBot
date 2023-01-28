import sys
import os
import subprocess
from timeit import default_timer as timer
import _thread

import sys
import importlib
import contextlib
import subprocess
from io import StringIO
from wrapt_timeout_decorator import *

class CodeExecutor2:
    @contextlib.contextmanager
    def stdoutIO(self, stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    @timeout(5)
    def execute_python(self, code):
        with self.stdoutIO() as c:
            try:
                exec(code)
            except Exception as e:
                print(e)
        return c.getvalue()