def print_items(n):
    for i in range(n): --> O(n)
        print(i)    
    
    for j in range(n): --> O(n)
        print(j)    

O(n + n) = O(2n) --> O(n)

Term of the input is dependent on the size of the input. In this case, the size of a, b can be completely different. 
A could be 1 while b could be 1 billion. The time complexity cannot be O(n) in this case because the algorithm is not 
dependent on the same input of n. It is reliant on the inputs a & b. 

def print_items(a, b):
    for i in range(a): --> O(a)
        print(i)    
    
    for j in range(b): --> O(b)
        print(j)    

So the time complexity of this function simplified becomes O(a + b)

def print_items(a, b):
    for i in range(a): --> O(a)
        for j in range(b): --> O(b)
            print(i, j)    
    
In this case: O(a * b)


How to meaure the codes using Big O:

    rules: https://drive.google.com/file/d/1KZ-oJkhyX1Fbi12q_94dCBkDfZAuGK6N/view?usp=drive_link
        • Rule 1 Any assignment statements and if statements that are executed
            once regardless of the size of the problem O(1)
        • Rule 2 A simple “for” loop from 0 to n ( with no internal loops) O(n)
        • Rule 3 A nested loop of the same type takes quadratic time complexity O(n2)
        • Rule 4 A loop, in which the controlling parameter is divided by two at
            each step O(log n)
        • Rule 5 When dealing with multiple statements, just add them up

