#!/usr/local/bin/python

import os
import sys
import signal


global version, command_list
version = "0.0.1"
command_list = {
    'exit':  'cl_exit',
    'help':  'cl_help'
}


def cl_exit():
    print("ZXC shutdown")
    sys.exit(0)


def cl_help():
    print("")
    print("ZXC command list")
    for key in command_list:
        print("\t" + key)
    print("")


def execute_zxc():
    print("")
    print("ZXC v" + version)
    print("Copyright 2020 AlexMcArrow")
    print("Licensed by MIT")
    print("")
    while(True):
        input = raw_input('zxc-shell$ ')
        input = input.split()
        if 0 < len(input):
            if input[0].lower() in command_list:
                globals()[command_list[input[0].lower()]]()
            else:
                print("unknown command [" + input[0].lower() + "]")


def signal_handler(signal, frame):
    cl_exit()


if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, signal_handler)
    execute_zxc()
