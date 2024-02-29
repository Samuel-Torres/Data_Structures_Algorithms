How much space in the worse case is needed. Is measured in the same way. 

def sum(n):
    if n <= 0:
        return 0
    return n + sum(n - 1)


    • Every time the function is called the function call is added to the memStack so it is taking up memory. Memory call
        is measured as O(n) since the function is called relative to the size of n.


