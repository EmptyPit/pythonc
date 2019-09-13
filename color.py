#!/usr/bin/env python3
end_color = '\033[0m'

color_list = {'black': '\033[30m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
            'purple': '\033[35m', 'cyan': '\033[36m', 'white': '\033[37m'}


def colr(color, text):
    if color in color_list:
        return color_list[color] + text + end_color
    elif color not in color_list:
        return text


test = colr('purple', 'some text')
print(test)