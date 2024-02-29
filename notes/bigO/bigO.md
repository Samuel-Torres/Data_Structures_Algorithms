Big O is the language & metreic we use to describe the efficiency of algorithms. 

Time Complexity: A way of showing how the runtime of a function increases as the size of the input increases. 

Every algorithm has an upper, lower, and mid bound performance. These are known as best, average, and worse case
scenarios of an algorithms runtime complexity. Worse case is Big-O.

Big Theta, Omega, and Omicron.

Best Case aka Big Omega
Average Case aka Big Theta
Worse Case aka Big-O or Big Omicron

Common Runtime Complexities:

O(1)     | Constant      | A simple add number function
    amount of operation is simply 1. 
    adding numbers, declaring variables, getting single item from list where index is known.

O(n)     | Linear        | Loop through number from 1 to n
    Number of operations grows in direct propertion with the size of n aka input.
    example: Looping through list with n number of items and printing the number will print exactly to the number of n.
    When you have to loop through an array operations grow proportionally to the size of the array. 

    vvv

    def print(n): --> O(1)
        for i in range(n): --> O(n)
        print(i) --> O(1)
        
        for j in range(n): --> O(n)
        print(i) --> O(1)


Drop Constants Asymptotic Analyses
    1 + 1 + 1 + O(n) + O(n)
    simplifies down to:
    3 + O(n) + O(n)
    simplifies down to:
    3 + O(2n)
    simplifies down to: drop first constant:
    O(2n)
    simplifies down to: drop second constant:
    O(n)

    
O(n^2)   | Quadratic     | Nested Loops

    def print(n): 
        for i in range(n): ---> O(n)
            for j in range(n): ---> O(n)
                 print(i, j) O(1)

    O(n) * O(n) + O(1)
    simplify:
    multiplied experessions like O(n) * O(n)  can be expressed as O(n^2) 10 * 10 == 10^2
    O(n^2) + O(1)
    drop constant:
    O(n^2)

    Drop Non-Dominant Term:

    def print(n): --> O(1)
        for i in range(n): --> O(n)
            for j in range(n):  --> O(n)
                 print(i, j) O(1)

        for k in range(n): --> O(n)
            print(k) --> O(1)

        1 + 1 + O(n) * O(n) + O(n) + 1
        simplify
        2 + 0(n) * O(n) + O(n) + 1
        drop constants:
        O(n) * O(n) + O(n)
        simplify:
        O(n^2) + O(n)
        simplify
        O(n^2 + n) --> Drop non-dominant term being the smaller term or n in this case:
        O(n^2)

O(log n) | Logarithmic   | Find an element in sorted array

Divide array in 2... divide and conquer approach. Log removes half the equation

logarithmic equations: 

in an array with 8 items we would need to divide the array in 2, 3 times giving us this equation.

2^3 = 8
log2^8 = ? --> == 3

when looking for 1. | = divide

list = [ 1, 2, 3, 4, | 5, 6, 7, 8] step 1
list = [ 1, 2, |  3, 4 ] step 2 
list = [ 1, 2 ] step 3
list = [ 1 ] found

O(2^n)   | Exponential   | Double recursion in Fibonacci

Space Complexity:
