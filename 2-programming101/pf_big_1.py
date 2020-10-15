# 1. Triangle Numbers
# Print the first 100 triangle numbers.

n=1
while n < 101:
    x = n * (n + 1)/2
    print(int(x))
    n += 1