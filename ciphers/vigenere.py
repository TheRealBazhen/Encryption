from utils.iostream import InputStream, OutputStream
from utils import text


def encode(in_stream: InputStream, out_stream: OutputStream, key: str):
    if not key.isalpha():
        return
    key = key.upper()
    key_pos = 0
    key_len = len(key)
    for line in in_stream:
        out_line = ''
        for symb in line:
            if symb.isalpha():
                symb = text.shift_letter(symb, ord(key[key_pos]) - ord('A'))
                key_pos = (key_pos + 1) % key_len
            out_line += symb
        out_stream.write(out_line)


def decode(in_stream: InputStream, out_stream: OutputStream, key: str):
    if not key.isalpha():
        return
    key = key.upper()
    key_pos = 0
    key_len = len(key)
    for line in in_stream:
        out_line = ''
        for symb in line:          \

            
            if symb.isalpha():
                symb = text.shift_letter(symb, ord('A') - ord(key[key_pos]))
                key_pos = (key_pos + 1) % key_len
            out_line += symb
        out_stream.write(out_line)
