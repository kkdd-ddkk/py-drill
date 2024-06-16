#coding=utf-8
from time import sleep
import csv
import sys
import os
from colorama import just_fix_windows_console
from termcolor import colored
import re

key_codes_rnd_jmp = [
    KEY_J := b'j'
]


key_codes_prev = [
    UP     := b'\xe0H',
    LEFT   := b'\xe0K',
    ESCAPE := b'\x1b',
    KEY_R  := b'r',
    KEY_H  := b'h',
    KEY_K  := b'k',
]

key_codes_next = [
    DOWN  := b'\xe0P',
    RIGHT := b'\xe0M',
    # ENTER := b'\r',
    KEY_N  := b'n',
    KEY_L  := b'l',
]

key_codes_repeat = [
    KEY_R   := b'r',
    BKSPACE := b'\x08'
]

key_codes_exit = [
    CTRL_C := b'\x03', 
    CTRL_D := b'\x04', 
    CTRL_Z := b'\x1a',
    CTRL_Q := b'\x11',
    CTRL_ENTER := b'\n',
    KEY_Q := b'q'
]



class biditer:
    def __init__(self, data):
        self.data = data
        self.index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index + 1 >= len(self.data):
            self.index = -1 # let's go from the beginning
            # raise StopIteration
        self.index += 1
        return self.index, self.data[self.index]
    
    def prev(self):
        if self.index - 1 < 0:
            self.index = len (self.data) # lets start from the end
            # raise StopIteration 
        self.index -= 1
        return self.index, self.data[self.index]

    def jmp(self, n):
        self.index = n % len (self.data)
        return self.index, self.data[self.index]



colors = [
    'red',
    'green',
    'yellow',
    'magenta',
    'cyan'
    # 'light_red',
    # 'light_green',
    # 'light_yellow',
    # 'light_blue',
    # 'light_magenta',
    # 'light_cyan'
]

def prev(it):
    return it.prev()



VERBOSE=False
def getch():
    global VERBOSE
    import msvcrt
    if   (inbs := msvcrt.getch()) == b'\xe0': inbs += getch()
    if VERBOSE: print (f"you pressed {inbs}")
    return inbs

def colr (s, col): 
    return colored(s, col,  attrs=['bold'])


def step_str(nrow):
    global WIDTH
    global NROWS
    return "[{{:0{0}d}}/{{:1}}]".format(WIDTH).format(nrow, NROWS)





just_fix_windows_console()

ESP=1
ENG=0

# new_word_re = re.compile (r'\/(?P<new>.+?)\/')
new_word_re = re.compile (r'\{(?P<new>.+?)\}')
from math import log, ceil

from random import randint 

f = 'mi casa.csv_' if len(sys.argv) == 1 else sys.argv[1]
with open(f, encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    
    rows  = [row for row in spamreader]
    NROWS = len(rows)
    WIDTH = ceil(log(10, NROWS)+1)

    rows_iter = biditer(rows)

    import random       
    idx, row = next (rows_iter)
    while True:
        unused = os.system('cls')
        col = random.choice(colors)
        hlgh_eng = new_word_re.sub (colr(r'\1', col), row[ENG])
        print(f'{step_str(idx+1)} {hlgh_eng}')
        
        if   (inbyte := getch()) in key_codes_repeat: continue
        elif (inbyte in key_codes_exit):     exit()
        elif (inbyte in key_codes_prev):     idx, row = prev(rows_iter); continue
        elif (inbyte in key_codes_next):     idx, row = next(rows_iter); continue
        # elif (inbyte in key_codes_rnd_jmp):  idx, row = rows_iter.jmp(randint(1, NROWS)); continue


        hlgh_esp = new_word_re.sub (colr(r'\1', col), row[ESP]); print(f'\n\t{hlgh_esp}')
        
        if   (inbyte := getch()) in key_codes_repeat: continue
        elif (inbyte in key_codes_exit):     exit()
        elif (inbyte in key_codes_prev):     idx, row = prev(rows_iter); continue
        elif (inbyte in key_codes_next):     idx, row = next(rows_iter); continue
        elif (inbyte in key_codes_rnd_jmp):  idx, row = rows_iter.jmp(randint(1, NROWS)); continue

        idx, row = next(rows_iter)