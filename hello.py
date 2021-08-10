#!/usr/bin/env Python3

import argparse

def get_args():
    """
    Get the command-line arguments
    """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Names to greet')
    return parser.parse_args()


def main():
    """
    This is the main
    :return: None
    """
    args = get_args()
    print('hello, ' + args.name + '!')



if __name__ == '__main__':
    main()

#print(__name__)
# Purpose: Say hello
 #print("hello World")

