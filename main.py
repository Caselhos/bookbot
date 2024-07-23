
from collections import OrderedDict


def main():
    with open("books/frankenstein.txt")as f:
        file_contents = f.read()
        
    count_chars(file_contents)
    # get_chars_dict(file_contents)

def count_chars(file_contents):
    number = len(file_contents.split())
    file_contents_lowered = file_contents.lower()
    char_int_count = {('a'):(0),('b'):(0),('c'):(0),('d'):(0),('e'):(0),('f'):(0),('g'):(0),('h'):(0),('i'):(0),('j'):(0),('k'):(0),('l'):(0),('m'):(0),('n'):(0),('o'):(0),('p'):(0),('q'):(0),('r'):(0),('s'):(0),('t'):(0),
                      ('u'):(0),('v'):(0),('w'):(0),('x'):(0),('y'):(0),('z'):(0)}
    for char in char_int_count:
         char_int_count[char] = file_contents_lowered.count(char)
         
    print_dict(char_int_count,number)


def print_dict(my_dict,number):
    print(number)
    test_dict = sorted(my_dict.items(),key=lambda x:x[1],reverse=True)
    for item in test_dict:
        print(f"The '{item[0]} ' was found {item[1]} times")
main()
