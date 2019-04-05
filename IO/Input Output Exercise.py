'''
test.txt
What is Python language?
Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.
Its design philosophy emphasizes code readability, and its syntax allows programmers to express 
concepts in fewer lines of code than possible in languages such as C++ or Java. 

Python supports multiple programming paradigms, including object-oriented, imperative and functional
programming or procedural styles. It features a dynamic type system and automatic memory management 
and has a large and comprehensive standard library.The best way we learn anything is by practice 
and exercise questions. We  have started this section for those (beginner to intermediate) who are 
familiar with Python.
'''

# 1: Write a Python program to read an entire text file
# Name: read_file
# Input: fname - name of the file
def read_file(fname):
  txt = open(fname)
  print(txt.read())
  
if __name__ == '__main__':
  read_file('test.txt')
  
# 2: Write a Python program to read first n lines of a file
# Name: read_file_n_lines
# Input: fname - the name of the file
#        nlines - the number of lines
from itertools import islice
def read_file_n_lines(fname, nlines):
    with open(fname) as f:
        for line in islice(f,nlines):
            print(line)
            
if __name__ == "__main__":
    read_file_n_lines('test.txt',2)
    
# 3: Write a Python program to append text to a file and display the text
# Name: read_file
# Input: fname - the name of the file
def read_file(fname):
  with open(fname, 'w') as myfile:
    myfile.write('Python Exercise\n')
    myfile.write('Java Exercises')
  
  txt = open(fname)
  print(txt.read())
  
if __name__ == "__main__":
  read_file('test.txt')
  
# 4: Write a Python program to read last n lines of a file
# Name: read_file_from_last
# Input: fname - the name of the file
#        nlines - the number of lines
def read_file_from_last(fname,nlines):
    with open(fname) as f:
        newline = f.readlines()[-nlines:]
        for line in newline:
            print(line)
            
if __name__ == "__main__":
    read_file_from_last('test1.txt',2)
