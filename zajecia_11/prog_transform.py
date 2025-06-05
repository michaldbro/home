import sys
from file_handler import FileHandler   #pamietać o dużych i małych literach!!! w nazwach klas

arguments = sys.argv[1:]

file_handler = FileHandler(input_file1=arguments[0], output_file1=arguments[1], transform1=arguments[2:])
print(file_handler.ldata)
file_handler.load()
print(file_handler.transform)
file_handler.save()

