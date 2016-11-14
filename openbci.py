#!/usr/bin/python

import numpy as np
import multiprocessing as q
from stream_data import stream_data
from plot_data import plot_data

def streaming_plotter(source_fd, output_fd, init_interval, update_interval):

    def stream_data_nonblocking(source_fd, output_fd, update_interval):
        p = q.Process(target=stream_data, args=(source_fd, output_fd, update_interval))
        p.start()

    def plot_data_nonblocking(fd, init_interval, update_interval):
        p = q.Process(target=plot_data, args=(fd, init_interval, update_interval))
        p.start()

    stream_data_nonblocking(source_fd, output_fd, update_interval)
    plot_data_nonblocking(output_fd, init_interval, update_interval)
