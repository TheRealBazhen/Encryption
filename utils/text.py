from utils.iostream import InputStream


def shift_letter(letter: str, offset: int):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in upper_alphabet:
        index = (upper_alphabet.index(letter) + offset) % len(upper_alphabet)
        letter = upper_alphabet[index]
    elif letter in lower_alphabet:
        index = (lower_alphabet.index(letter) + offset) % len(lower_alphabet)
        letter = lower_alphabet[index]
    return letter


def letters_count(in_stream: InputStream):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cnt = [0 for i in alphabet]
    for line in in_stream:
        for symb in line:
            symb = symb.lower()
            if symb in alphabet:
                cnt[ord(symb) - ord(alphabet[0])] += 1
    return cnt
