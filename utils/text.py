from utils.iostream import InputStream


def shift_letter(letter: str, offset: int):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter.isupper():
        index = (upper_alphabet.index(letter) + offset) % len(upper_alphabet)
        letter = upper_alphabet[index]
    elif letter.islower():
        index = (lower_alphabet.index(letter) + offset) % len(lower_alphabet)
        letter = lower_alphabet[index]
    return letter


def letters_count(in_stream: InputStream):
    cnt = [0 for i in range(26)]
    for line in in_stream:
        for symb in line:
            if symb.islower():
                cnt[ord(symb) - ord('a')] += 1
            elif symb.isupper():
                cnt[ord(symb) - ord('A')] += 1
    return cnt
