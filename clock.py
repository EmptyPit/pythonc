#!/usr/bin/env python3
import threading
import time


letters_list = {
    '1': """ \
   #
  # #
 #  #
    #
    #""",

'7': """\
####
   #
  # 
 #  
#   
""",

'2': """\
####
   #
  # 
 #  
####""",

'3': """\
####
   #
####
   #
####""",

'4': """\
 #  #
 #  #
 ####
    #
    #""",

'5': """\
####
#   
####
   #
####""",

'6': """\
####
#   
####
#  #
####""",

'8': """\
####
#  #
####
#  #
####""",

'9': """\
####
#  #
####
   #
   #""",

'0': """\
####
#  #
#  #
#  #
####""",

':': """\
  # 
  # 
    
  # 
  # """}

s = 0
m = 0
h = 0

def sec_min_hour():
    global s
    global m
    global h
    while s < 60:
        time.sleep(1)
        # print('second: ', s)
        s += 1
        # print('{} {} {}'.format(h, m, s))
        if s > 59:
            m += 1
            s = 0
            # print('Minutes :', m)
            if m == 60:
                h += 1
                m = 0
                # print('Hours', h)
                if h == 24:
                    h = 0

sec_min_hour()

time_list = [h, m, s]

def clock(chars):
    letters = []
    output = []
    for i in chars:
        try:
            letters.append(letters_list[i].split('\n'))
        except KeyError:
            pass

    for r in range(5):
        tmp = []
        for letter in letters:
            tmp.append(letter[r])
        output.append("  ".join(tmp))

    print('\n'.join(output))



def working_clock():
    while True:
        # d = time.strftime('%H %M %S', time.localtime())
        clock(" ".join([str(i) for i in time_list]))
        # time.sleep(1)
        print('\033[H\033[J')

working_clock()