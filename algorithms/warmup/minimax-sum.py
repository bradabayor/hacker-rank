arr = [1, 3, 5, 7, 9]

def miniMaxSum():
    arr.sort()
    max_sum = 0
    min_sum = 0
    
    for i in range(4):
        max_sum += arr[len(arr) - (i + 1)]
        min_sum += arr[i]

    print(f"{min_sum} {max_sum}")    


miniMaxSum()