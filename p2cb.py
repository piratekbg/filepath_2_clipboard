#!/usr/bin/env python3

#the script takes one argument, the file name, from the user and returns a it concatenated with its current folder path as a string readily copied in the clipboard

import os, sys, clipboard

path = os.getcwd()
f_name = sys.argv[1]

full_file_path = path+'/'+f_name
clipboard.copy(full_file_path)
print(f"full file path: {full_file_path}\ncopied to clipboard! just paste it :)")
