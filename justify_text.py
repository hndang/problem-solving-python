import collections
import math

# TODO fix
def justify_text(text, max_width):
    word_list = collections.deque()
    line_len = 0
    for word in text:
        line_len = line_len + len(word) + 1
        if line_len > max_width or word == text[-1]:
            line_words_count = len(word_list)
            space = max_width - (line_len - len(word) - 1 - line_words_count)
            line_len = 0
            if line_words_count == 1:
                space_pad = space * " "
                result = f"{word_list.pop()}{space_pad}"
            else:
                word_left = line_words_count - 1 # last word don't need
                result = ""
                for x in word_list:
                    pad = math.ceil(space/word_left) if word_left > 0 else 0
                    word_left -= 1
                    space = space - pad
                    space_pad = pad * " "
                    result = f"{result}{x}{space_pad}"
            word_list.clear()
            print(result)
        word_list.append(word)



def run():
    text = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    max_width = 16
    justify_text(text, max_width)

if __name__ == '__main__':
    run()