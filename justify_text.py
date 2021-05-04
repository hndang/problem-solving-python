import collections
import math


def justify_text(text, max_width):
    def justify_line(w, max_w, cur_len):
        space = max_w - (cur_len - len(w))
        if len(w) == 1:
            space_pad = (space + 1) * " "
            return f"{word_list[0]}{space_pad}"
        else:
            r = ""
            base_space_pad, extra = divmod(space, len(w)-1)
            for x in w:
                space_pad_num = (base_space_pad + 1) if extra > 0 else base_space_pad
                space_pad = space_pad_num * " "
                extra -= 1
                if x == w[-1]:
                    space_pad = ""
                r = f"{r}{x}{space_pad}"
            return r

    word_list = []
    line_len = 0
    result = []
    for word in text:
        if (len(word) + line_len) <= max_width:
            word_list.append(word)
            line_len += len(word) + 1
        else:
            result.append(justify_line(word_list, max_width, line_len))
            word_list = [word]
            line_len = len(word) + 1
    result.append(justify_line(word_list, max_width, line_len))
    return result


def run():
    text = ["thee", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    max_width = 16
    print(justify_text(text, max_width))

if __name__ == '__main__':
    run()