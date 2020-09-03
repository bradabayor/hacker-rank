a = [1, 4, 3 ,2]

def reverseArray():
    i = 0
    for num in a:
        print(a[len(a) - 1 - i])
        i += 1


reverseArray()