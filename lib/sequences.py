#!/usr/bin/env python3

#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    
    n1 = 0
    n2 = 1
    fibonacci_list = [n1, n2]
    
    for i in range(2, length):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        fibonacci_list.append(n3)
    
    print(fibonacci_list)

        
