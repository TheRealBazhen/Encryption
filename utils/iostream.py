import sys


class InputStream:
    def __init__(self, inp, binary=False):
        self.__data = None
        if inp == sys.stdin:
            self.__data = sys.stdin.readlines()
        else:
            # inp is interpreted as input file name
            mode = 'rb' if binary else 'rt'
            with open(inp, mode=mode) as f:
                self.__data = f.readlines()

    def __iter__(self):
        return iter(self.__data)


class OutputStream:
    def __init__(self, out, binary=False):
        self.is_stdout = False
        if out == sys.stdout:
            self.__out = out
            self.is_stdout = True
        else:
            try:
                mode = 'wb' if binary else 'wt'
                self.__out = open(out, mode=mode)
            except IOError:
                self.__out = sys.stdout
                self.is_stdout = True

    def write(self, line):
        self.__out.write(line)

    def close(self):
        if not self.is_stdout:
            self.__out.close()
            self.__out = None
