
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:30:53 2019

@author: rameelaazeez
"""

import glob
import os



directory =  os.path.dirname(os.path.realpath(__file__))


def get_num_of_words(fname):
    num_words = 0
    
    with open(fname, 'r',encoding="utf-8") as f:
        for line in f:
            words = line.split()
            num_words += len(words)
    print("Number of words:")
    print(num_words)

def get_num_of_sentences(fname):
    num_s = 0
    
    with open(fname, 'r',encoding="utf-8") as f:
        for line in f:
            num_s += 1
    print("Number of sentences of :"+fname+"\n")
    print(num_s)
    
def generate_unique_files():
    for filename in glob.glob('*.txt'):
        with open(filename, 'r',encoding="utf-8"):
            get_unique_file(filename,filename[:-4]+"_unique.txt")
            get_num_of_sentences(filename[:-4]+"_unique.txt")
     
                
def get_unique_file(input_filename, output_filename):
    input_file = open(input_filename, 'r',encoding="utf-8")
    file_contents = input_file.read()
    input_file.close()
    word_list = file_contents.split()

    file = open(output_filename, 'w',encoding="utf-8")

    unique_words = set(word_list)
    unique_words = sorted(unique_words)
    for word in unique_words:
        file.write(str(word) + "\n")
    
    file.close()

   
generate_unique_files()



