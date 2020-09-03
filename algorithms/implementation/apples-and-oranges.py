s = 7
t = 11
a = 3
b = 2
apples = [-2, 2, 1]
oranges = [5 ,6]

def countApplesAndOranges():
    fruit = [0, 0]

    apple_drop = [(a + i) for i in apples]
    orange_drop = [(b + i) for i in oranges]

    for apple in apple_drop:
        if s <= apple <= t:
            fruit[0] += 1

    for orange in orange_drop:
        if s <= orange <= t:
            fruit[1] += 1

    print(fruit[0])
    print(fruit[1])


print(countApplesAndOranges())