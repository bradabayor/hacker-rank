arr = [[3], [11, 2, 4], [4, 5, 6], [10, 8, -12]]

def diagonalDifference(arr):
    primary = []
    secondary = []
    width = len(max(arr, key=len))

    y = 0
    while y < len(arr):
        if len(arr[y]) > width:
            primary.append(arr[y][y - 1])
            secondary.append(arr[y][width])
        y += 1
        width -= 1

    return abs(sum(primary) - sum(secondary))

print(diagonalDifference(arr))

