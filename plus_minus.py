num = 6
arr = [[-4, 3, -9, 0, 4, 1]]

def plusMinus():
    pm_arr = [0, 0, 0]

    for x in range(len(arr)):
        if arr[x] > 0: pm_arr[0] += 1
        if arr[x] < 0: pm_arr[1] += 1
        if arr[x] == 0: pm_arr[2] += 1

    print(pm_arr[0], pm_arr[1], pm_arr[2])

    for i, x in enumerate(pm_arr):
        print(pm_arr[i] / len(arr))

plusMinus()
