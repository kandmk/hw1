with open('links.txt') as f1:
    links = f1.read()
    leng = len(links) / 2
    number = 0
    link_dic = {}
    for line in f1:
        links = line.split()
        for link in links:
            if link == number:
                link_dic[number] = link_dic[number] + link
            elif links[2*x] != number:
                number += 1
                link_dic[number] = link_dic[number] + link
    print(link_dic)
    

with open('pages.txt') as f2:
    pages = f2.read().split()
def Find_number(start):
    start_num = 0
    for w in range(11955):
        if pages[1] == start:
            break
        elif pages[2*w+1] == start:
            start_num = w+1
            break
    return(start_num) 
    

def Find_root(start, end):
    stack = [start]
    check = []
    while stack:
        label = stack.pop(0)
        if label == end:
            stack.append(label)
            return stack
        if label not in check:
            check.append(label)
            stack = link_dic.get(label, []) + stack
            return stack

while True:
    print("Please write 'start'")
    start = input()
    print("please write 'end'")
    end = input()
    start_num = Find_number(start)
    end_num = Find_number(end)
    print(Find_root(start_num, end_num))
