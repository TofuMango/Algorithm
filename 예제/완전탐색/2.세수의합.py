def three_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i]+arr[j]+arr[k] == target:
                    print(f"({arr[i]}, {arr[j]}, {arr[k]})")


arr = [2, 3, 5, 7, 8]
target = 15
three_sum(arr, target)
