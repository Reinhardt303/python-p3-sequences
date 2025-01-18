#!/usr/bin/env python3

def print_fibonacci(length):
    
    new_list = []
    fib_list = []
    for n in range(length):
        new_list.append(n)
    if length < 3:
        print(new_list)
    elif length >= 3:
        for i in new_list:
            if i < 2:
                fib_list.append(i)
            elif i >= 2:
                fib_list.append((fib_list[i-1])+(fib_list[i-2]))
        print(fib_list)




            
