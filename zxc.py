#!/usr/local/bin/python

import os
import sys
import signal


global version, command_list
version = "0.0.1"
command_list = {
    'exit':  {'run': 'cl_exit', 'info': 'Exit from ZXC-shell'},
    'help':  {'run': 'cl_help', 'info': 'Show help page'}
}


def cl_exit():
    print("ZXC shutdown")
    sys.exit(0)


def cl_help():
    zxc_info()
    print("Avalible commands")
    for key in command_list:
        print("\t" + key+"\t"+command_list[key]['info'])
    print("")


def zxc_info():
    print("ZXC v" + version + "   Copyright 2020 AlexMcArrow   Licensed by MIT")


def execute_zxc():
    print("")
    zxc_info()
    print("")
    while(True):
        input = raw_input('zxc-shell$ ')
        input = input.split()
        if 0 < len(input):
            if input[0].lower() in command_list:
                globals()[command_list[input[0].lower()]['run']]()
            else:
                print("unknown command [" + input[0].lower() + "]")


def signal_handler(signal, frame):
    cl_exit()


if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, signal_handler)
    execute_zxc()
