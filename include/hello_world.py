import sys

def hello_world():
    print("hello the world !")

def print_path():
    j = 0
    for i in sys.path:
        print(values=j, end="\t" + i)
        j += 1
