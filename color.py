#!/usr/bin/env python3
end_color = '\033[m'

color_list = {'black': '\033[30m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
            'purple': '\033[35m', 'cyan': '\033[36m', 'white': '\033[37m'}


def colr(color, text):
    com = [v + text + end_color for k, v in color_list.items() if k == color]
    return com
    # return ''.join(com)


test = colr('cyan','some text')
print(*test, end="\n")
