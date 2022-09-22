#!/usr/bin/python3

import hidden_4

def main():
    for item in dir(hidden_4):
        if item[0:2] != "__":
            print("{:s}".format(item))

if __name__ == "__main__":
    main()
