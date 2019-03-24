# Code review #1

Андрей Баженов, гр. Б05-812

Comand line parameters for `encryption.py`:
* `[-h/--help]`&nbsp;&mdash; list of all command line arguments.
* `--mode {encode,decode,hack}`&nbsp;&mdash; work mode (encode text, decode text, hack encoded text - supported only for Caesar cipher).
* `--cipher {caesar,vigenere,vernam}`&nbsp;&mdash; cipher to use.
* `[--in-file IN_FILE_NAME]`&nbsp;&mdash; input file. If not specified, reading from `stdin` (doesn`t work for binary input, so this parameter must be specified to decode using Vernam cipher).
* `[--out-file OUT_FILE_NAME]`&nbsp;&mdash; output file. If not specified, writing to `stdout` (doesn`t work for binary input, so this parameter must be specified to encode using Vernam cipher).
* `[--offset OFFSET_VALUE]`&nbsp;&mdash; offset for Caesar cipher. Default is 13.
* `[--key KEY_VALUE]`&nbsp;&mdash; key for Vigenere and Vernam ciphers. For Vernam cipher it is better to use `--key-path` parameter. Set to `CGSGFOREVER` by default.
* `[--key-path KEY_FILE_NAME]`&nbsp;&mdash; jey path for Vigenere and Vernam ciphers. Overrides `--key` option if specified.