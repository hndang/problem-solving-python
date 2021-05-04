'''
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''


def encode_run_length(text):
    txt_stack = []
    result = ""
    for char in text:
        if len(txt_stack) == 0 or txt_stack[0] == char:
            txt_stack.append(char)
        else:
            result = f"{result}{len(txt_stack)}{txt_stack[0]}"
            txt_stack = [char]
    result = f"{result}{len(txt_stack)}{txt_stack[0]}"
    return result


def run():
    text = "AAAABBBCCDAA"
    print(encode_run_length(text))


if __name__ == '__main__':
    run()