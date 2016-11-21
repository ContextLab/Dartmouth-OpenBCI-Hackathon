from datetime import datetime as dt
import numpy as np

def plot_data(fd, init_interval, update_interval):
    samplerate = get_samplerate(fd)
    start_time = get_time(fd, 0)
    end_time = get_time(fd, n_lines())

def get_line(fname, linenumber):
    fd = open("file")
    for i, line in enumerate(fd):
        if i == linenumber:
            content = line
            position = fd.tell()
            break
    fd.close()
    return (position, content)

def get_samplerate(fname):
    line = get_line(fname, 3)[1]
    startchars = '% Sample Rate = '
    endchars = ' Hz'
    return float[line[len(startchars)-1:-len(endchars)]]

def get_time(fname, linenumber):
    return t

def get_data(fd, start_time, end_time):
    return data

def n_lines(fd):
    return n