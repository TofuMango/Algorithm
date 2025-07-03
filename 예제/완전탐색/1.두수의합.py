def two_sum(arr, target):
    fin = len(arr)
    for i in range(fin):
        for j in range(i+1, fin):
            if (arr[i]+arr[j] == target):
                print(f"({arr[i]}, {arr[j]})")


arr = [2, 7, 4, 9, 1]
target = 10
two_sum(arr, target)
