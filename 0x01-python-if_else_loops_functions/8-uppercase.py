#!/usr/bin/python3

def uppercase(str):
     for char in str:
         if ord(char) in range(97, 123):
             new_ord = ord(char)-32
         else:
             new_ord = ord(char)

         print(chr(new_ord), end='')
     print("\n", end='')
