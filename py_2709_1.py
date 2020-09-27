'''Write a function that takes a list of strings an prints them, one per line, in a rectangular frame.

Sample:

["Hello", "World", "in", "a", "frame"] -->

 *********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
'''
import sys
from io import StringIO
sys.stdin = StringIO('''3
Hello
world
you
''')



def box_printer(words_list):
    max_length = max([len(p) for p in words_list])
    box_length = max_length+2
    print('*'*box_length)
    for i in words_list:
        print('*'+i+' '*(max_length-1-len(i))+'*')
    print('*'*box_length)

a = []
count = 0
n = int(input("No of words:\n"))
for i in range(n):
    a.append(input())
    
box_printer(a)



'''
The best solution that i have seen :omg:
def star_template(words):
    width = max([len(x) for x in words])

    return "\n".join([
        "*" * (width + 4),
        *map(lambda x: f'* {x.ljust(width)} *', words),
        "*" * (width + 4)
    ]);
'''