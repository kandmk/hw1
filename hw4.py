# coding: utf-8
import sys

with open("links.txt", "r") as f1:
    links = f1.read()
#link_bef = 0
#while links:
#    link_num = links[0]
#    if link_bef == link_num:
f1.close()

#def Find_number(start):
with open('pages.txt') as f2:
    pages = f2.read().split()
    f2.close()
    start = 'あおきてつお'
    start_num = 0
    for w in range(11955):
        if pages[1] == start:
            break
        elif pages[2*w+1] == start:
            start_num = w+1
            break
    print(start_num)
    

#def Find_root(start, end):
#    stack = []
#    check = []
#    stack.append(start)
#    while (label != end):
#        if label == end:
#            stack.append(label)
#            return stack
#        else:
#            return stack
            
            
