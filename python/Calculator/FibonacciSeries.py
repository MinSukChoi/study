# Fibonacci Series:
# the sum of two elements defines the next
a, b = 0, 1  # multiple assignment
while b < 10 : # non zero value is true like in C, string or list value with non-zero length is ture
    print(b) # indented : indentation is Python's way of grouping statements
    a, b = b, a + b

i = 256 * 256
print('The value of i is',i)

a, b = 0, 1
while b < 1000 :
    print(b, end=',') # the keyword argument end can be used to avoid the newline after the output, or end the output with a different string
    a,b = b, a+b