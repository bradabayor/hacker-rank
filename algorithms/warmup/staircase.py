n = 20

def staircase():
    x = n
    y = 1
    while x > 0:
        print(' ' * (x - 1), end='')
        print('#' * y)
        x -= 1
        y += 1

staircase()