from utils.iostream import InputStream, OutputStream
from utils import text


def encode(in_stream: InputStream, out_stream: OutputStream, offset: int):
    for line in in_stream:
        out_line = ''
        for symb in line:
            symb = text.shift_letter(symb, offset)
            out_line += symb
        out_stream.write(out_line)


def decode(in_stream: InputStream, out_stream: OutputStream, offset: int):
    encode(in_stream, out_stream, -offset)


def hack(in_stream: InputStream, out_stream: OutputStream):
    freq = text.letters_count(in_stream)
    e_index = freq.index(max(freq))
    offset = ord('e') - ord('a') - e_index
    encode(in_stream, out_stream, offset)
