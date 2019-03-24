import sys
import argparse
from utils.iostream import InputStream, OutputStream
from ciphers import caesar, vigenere, vernam


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['encode', 'decode', 'hack'],
                        required=True)
    parser.add_argument('--cipher', choices=['caesar', 'vigenere', 'vernam'],
                        required=True)
    parser.add_argument('--in-file', dest='in_file',
                        help='File to read from. If not specified,'
                             ' reading from stdin')
    parser.add_argument('--out-file', dest='out_file',
                        help='File to write to. If not specified,'
                             ' writing to stdout')
    parser.add_argument('--offset', type=int, default=13, help='Offset for '
                                                               'Caesar cipher')
    parser.add_argument('--key', default='CGSGFOREVER',
                        help='Key for Vigenere and Vernam ciphers')
    parser.add_argument('--key-path', dest='key_path',
                        help='Key path for ciphers, overrides'
                             ' --key if specified')
    args = parser.parse_args()

    binary_mode_inp = (args.cipher == 'vernam' and args.mode == 'decode')
    binary_mode_out = (args.cipher == 'vernam' and args.mode == 'encode')
    if binary_mode_inp and not args.in_file:
        print('Not able to use stdin in binary mode. '
              'Please, use file for input.')
        return
    if binary_mode_out and not args.out_file:
        print('Not able to use stdout in binary mode. '
              'Please, use file for output.')
        return
    if not args.in_file:
        print('Input text to process, press Ctrl+D to finish input:')
    try:
        in_stream = InputStream(args.in_file if args.in_file
                                else sys.stdin, binary_mode_inp)
    except (FileNotFoundError, IOError):
        print('Could not open file \'{}\''.format(args.in_file))
        return
    out_stream = OutputStream(args.out_file if args.out_file
                              else sys.stdout, binary_mode_out)

    if args.key_path:
        try:
            key_stream = InputStream(args.key_path)
        except (FileNotFoundError, IOError):
            print('Could not open file \'{}\''.format(args.key_path))
            return
        args.key = ''
        for line in key_stream:
            args.key += line

    if args.mode == 'encode':
        if args.cipher == 'caesar':
            caesar.encode(in_stream, out_stream, args.offset)
        elif args.cipher == 'vigenere':
            vigenere.encode(in_stream, out_stream, args.key)
        else:
            vernam.encode(in_stream, out_stream, args.key)
    elif args.mode == 'decode':
        if args.cipher == 'caesar':
            caesar.decode(in_stream, out_stream, args.offset)
        elif args.cipher == 'vigenere':
            vigenere.decode(in_stream, out_stream, args.key)
        else:
            vernam.decode(in_stream, out_stream, args.key)
    else:
        if args.cipher == 'caesar':
            caesar.hack(in_stream, out_stream)
        else:
            print('Sorry, this hack is not currently supported')

    out_stream.close()


if __name__ == '__main__':
    main()
